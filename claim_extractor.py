import os
import json
from openai import OpenAI
from config import Config

class ClaimExtractor:
    """Extract factual claims from text using LLM"""
    
    def __init__(self):
        """Initialize the claim extractor with OpenRouter API"""
        if not Config.OPENROUTER_API_KEY:
            raise ValueError("OPENROUTER_API_KEY not set in environment variables")
        
        self.client = OpenAI(
            base_url=Config.OPENROUTER_BASE_URL,
            api_key=Config.OPENROUTER_API_KEY,
            default_headers={
                "HTTP-Referer": "http://localhost:5000",
                "X-Title": "Fact Checker App"
            }
        )
        self.model = Config.OPENROUTER_MODEL
    
    def extract_claims(self, text):
        """
        Extract verifiable factual claims from text
        
        Args:
            text (str): The text to extract claims from
            
        Returns:
            list: List of dictionaries containing claims
        """
        prompt = f"""You are a fact-checking assistant. Extract ALL specific, verifiable factual claims from the following text.

Focus on:
- Statistics and numbers (prices, percentages, growth rates)
- Dates and timelines
- Financial figures (GDP, market values, prices)
- Technical specifications
- Company announcements and product releases
- Economic indicators
- Specific events and their outcomes

For each claim, provide:
1. The exact claim as stated in the text
2. The category (e.g., "cryptocurrency", "AI", "economics", "aerospace")
3. Key entities mentioned (companies, products, numbers)

Return ONLY a valid JSON array of claims in this exact format:
[
  {{
    "claim": "exact claim text",
    "category": "category name",
    "entities": ["entity1", "entity2"]
  }}
]

Text to analyze:
{text}

Return ONLY the JSON array, no other text."""

        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": prompt}
                ],
                temperature=0.3,
                max_tokens=2000
            )
            
            result = response.choices[0].message.content.strip()
            
            # Try to parse JSON
            # Remove markdown code blocks if present
            if result.startswith("```"):
                result = result.split("```")[1]
                if result.startswith("json"):
                    result = result[4:]
            
            claims = json.loads(result)
            
            return claims
            
        except json.JSONDecodeError as e:
            print(f"JSON parsing error: {e}")
            print(f"Response: {result}")
            # Fallback: return empty list
            return []
        except Exception as e:
            print(f"Error extracting claims: {e}")
            raise Exception(f"Failed to extract claims: {str(e)}")
