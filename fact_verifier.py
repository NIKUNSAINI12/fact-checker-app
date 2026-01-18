import os
import json
from tavily import TavilyClient
from openai import OpenAI
from config import Config

class FactVerifier:
    """Verify claims against live web data"""
    
    def __init__(self):
        """Initialize the fact verifier with Tavily and OpenRouter"""
        if not Config.TAVILY_API_KEY:
            raise ValueError("TAVILY_API_KEY not set in environment variables")
        if not Config.OPENROUTER_API_KEY:
            raise ValueError("OPENROUTER_API_KEY not set in environment variables")
            
        self.tavily_client = TavilyClient(api_key=Config.TAVILY_API_KEY)
        self.llm_client = OpenAI(
            base_url=Config.OPENROUTER_BASE_URL,
            api_key=Config.OPENROUTER_API_KEY,
            default_headers={
                "HTTP-Referer": "http://localhost:5000",
                "X-Title": "Fact Checker App"
            }
        )
        self.model = Config.OPENROUTER_MODEL
    
    def search_web(self, query):
        """
        Search the web for information about a claim
        
        Args:
            query (str): Search query
            
        Returns:
            list: Search results
        """
        try:
            response = self.tavily_client.search(
                query=query,
                search_depth="advanced",
                max_results=5
            )
            return response.get('results', [])
        except Exception as e:
            print(f"Search error: {e}")
            return []
    
    def verify_claim(self, claim_data):
        """
        Verify a single claim against web search results
        
        Args:
            claim_data (dict): Claim information
            
        Returns:
            dict: Verification result
        """
        claim = claim_data.get('claim', '')
        category = claim_data.get('category', '')
        
        # Search for the claim
        search_query = f"{claim} {category} latest news 2026"
        search_results = self.search_web(search_query)
        
        if not search_results:
            return {
                'claim': claim,
                'status': 'False',
                'reason': 'No evidence found on the web',
                'sources': [],
                'evidence': 'No search results available'
            }
        
        # Prepare context from search results
        context = "\n\n".join([
            f"Source {i+1}: {result.get('title', '')}\n{result.get('content', '')}"
            for i, result in enumerate(search_results[:3])
        ])
        
        sources = [
            {
                'title': result.get('title', ''),
                'url': result.get('url', ''),
                'snippet': result.get('content', '')[:200]
            }
            for result in search_results[:3]
        ]
        
        # Use LLM to verify the claim
        verification_prompt = f"""You are a fact-checker. Verify the following claim against current web data.

Claim to verify: "{claim}"

Current web search results (January 2026):
{context}

Analyze the claim and categorize it as:
- "Verified": The claim is accurate and matches current data
- "Inaccurate": The claim is partially correct but contains outdated or slightly wrong information
- "False": The claim is incorrect or contradicts current evidence

Provide your response in this EXACT JSON format:
{{
  "status": "Verified" or "Inaccurate" or "False",
  "reason": "brief explanation of why",
  "evidence": "specific evidence from the search results"
}}

Return ONLY the JSON, no other text."""

        try:
            response = self.llm_client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": verification_prompt}
                ],
                temperature=0.2,
                max_tokens=500
            )
            
            result = response.choices[0].message.content.strip()
            
            # Parse JSON response
            if result.startswith("```"):
                result = result.split("```")[1]
                if result.startswith("json"):
                    result = result[4:]
            
            verification = json.loads(result)
            
            return {
                'claim': claim,
                'status': verification.get('status', 'False'),
                'reason': verification.get('reason', ''),
                'evidence': verification.get('evidence', ''),
                'sources': sources
            }
            
        except Exception as e:
            print(f"Verification error: {e}")
            return {
                'claim': claim,
                'status': 'False',
                'reason': f'Error during verification: {str(e)}',
                'sources': sources,
                'evidence': 'Verification failed'
            }
    
    def verify_all_claims(self, claims):
        """
        Verify all extracted claims
        
        Args:
            claims (list): List of claim dictionaries
            
        Returns:
            dict: Categorized verification results
        """
        results = {
            'verified': [],
            'inaccurate': [],
            'false': []
        }
        
        for claim_data in claims:
            verification = self.verify_claim(claim_data)
            
            status = verification['status'].lower()
            if 'verified' in status or 'true' in status:
                results['verified'].append(verification)
            elif 'inaccurate' in status or 'outdated' in status:
                results['inaccurate'].append(verification)
            else:
                results['false'].append(verification)
        
        return results
