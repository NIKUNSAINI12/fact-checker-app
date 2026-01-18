# Memory Optimization for Render Free Tier

The app is running out of memory on Render's free tier (512MB limit).

## What's Happening
```
WORKER TIMEOUT (pid:58)
Worker was sent SIGKILL! Perhaps out of memory?
```

This happens because:
1. PDF processing uses memory
2. AI API calls use memory
3. Tavily search uses memory
4. All happening simultaneously exceeds 512MB

## Fixes Applied

### 1. Updated Procfile
Changed from:
```
web: gunicorn app:app
```

To:
```
web: gunicorn app:app --timeout 300 --workers 1 --threads 2 --worker-class sync
```

This:
- Increases timeout to 300 seconds (5 minutes)
- Uses only 1 worker (less memory)
- Uses 2 threads for concurrency
- Uses sync worker class (most memory efficient)

### 2. Push to GitHub

You need to push the updated Procfile to GitHub:

**Option A: If you have GitHub Desktop:**
1. Open GitHub Desktop
2. It will show changes to `Procfile` and `static/js/main.js`
3. Write commit message: "Fix memory issues for Render deployment"
4. Click "Commit to main"
5. Click "Push origin"

**Option B: Manual upload to GitHub:**
1. Go to: https://github.com/NIKUNSAINI12/fact-checker-app
2. Click on `Procfile`
3. Click the pencil icon (Edit)
4. Replace content with:
   ```
   web: gunicorn app:app --timeout 300 --workers 1 --threads 2 --worker-class sync
   ```
5. Commit changes

### 3. Render Will Auto-Deploy

Once you push to GitHub, Render will automatically:
1. Detect the changes
2. Rebuild the app
3. Deploy with new settings

Wait 2-3 minutes, then test again!

## Alternative: Upgrade Render Plan

If still having memory issues, you may need to upgrade from free tier to:
- **Starter Plan**: $7/month, 512MB → 2GB RAM
- This would solve all memory issues

## For Assessment Submission

If you can't upgrade and the free tier keeps crashing:
1. **Submit the local version** - Your local app works perfectly
2. **Record demo video** of the local version working
3. **Include GitHub repo** - Shows your code
4. **Explain in submission** - "App works locally, Render free tier has memory limitations"

The assessment is about building the app, not about having unlimited cloud resources!
