# Render Deployment Troubleshooting

## Current Issue
Getting 500 Internal Server Error when uploading files.

## Most Likely Cause
Environment variables are not being read properly on Render.

## Solution Steps

### 1. Verify Environment Variables in Render

Go to your Render dashboard and check:

**Navigate to:**
https://dashboard.render.com/web/srv-d5mg1jhr0fns73ev5hqg

**Check Environment Variables:**
1. Click "Environment" in the left sidebar
2. Verify these variables exist:
   - `OPENROUTER_API_KEY`
   - `TAVILY_API_KEY`
   - `FLASK_SECRET_KEY`

3. **IMPORTANT**: Make sure there are NO quotes around the values
   - ❌ Wrong: `"sk-or-v1-..."`
   - ✅ Correct: `sk-or-v1-...`

### 2. Check the Values

**OPENROUTER_API_KEY should be:**
```
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
```

**TAVILY_API_KEY should be:**
```
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
```

**FLASK_SECRET_KEY can be:**
```
fact-checker-secret-2026
```

### 3. After Updating

1. Click "Save Changes"
2. Render will automatically redeploy (wait 2-3 minutes)
3. Test the app again

### 4. Test Environment Variables

Visit this URL to check if env vars are loaded:
```
https://fact-checker-app-j73m.onrender.com/health
```

Should return: `{"status": "healthy"}`

### 5. Check Logs

If still not working:
1. Go to Render dashboard
2. Click "Logs" tab
3. Look for any Python errors or tracebacks
4. Share the error message

## Alternative: Use Render's Secret Files

If environment variables don't work, you can use Render's secret files feature:

1. In Render dashboard, go to "Environment"
2. Scroll to "Secret Files"
3. Add a file named `.env`
4. Content:
```
OPENROUTER_API_KEY=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
TAVILY_API_KEY=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
FLASK_SECRET_KEY=fact-checker-secret-2026
```
5. Save and redeploy
