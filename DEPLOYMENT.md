# Deployment Guide

## ✅ Tested Successfully
The application has been tested locally and successfully verified claims from the assessment PDF.

---

## 🚀 Deployment Options

### Option 1: Deploy to Render (Recommended)

1. **Create a GitHub Repository**
   ```bash
   git init
   git add .
   git commit -m "Initial commit - Fact Checker App"
   git branch -M main
   git remote add origin YOUR_GITHUB_REPO_URL
   git push -u origin main
   ```

2. **Sign up at Render**
   - Go to https://render.com/
   - Sign up with GitHub

3. **Create New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name**: fact-checker-app
     - **Environment**: Python 3
     - **Build Command**: `pip install -r requirements.txt`
     - **Start Command**: `gunicorn app:app`

4. **Add Environment Variables**
   - Go to "Environment" tab
   - Add:
     - `OPENROUTER_API_KEY`: your-openrouter-key
     - `TAVILY_API_KEY`: your-tavily-key
     - `FLASK_SECRET_KEY`: random-secret-string

5. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment (2-3 minutes)
   - Your app will be live at: `https://fact-checker-app.onrender.com`

---

### Option 2: Deploy to Railway

1. **Create GitHub Repository** (same as above)

2. **Sign up at Railway**
   - Go to https://railway.app/
   - Sign up with GitHub

3. **Deploy**
   - Click "New Project" → "Deploy from GitHub repo"
   - Select your repository
   - Railway auto-detects Python and deploys

4. **Add Environment Variables**
   - Go to "Variables" tab
   - Add the same environment variables as above

5. **Get URL**
   - Railway provides a URL automatically
   - Click "Generate Domain" if needed

---

### Option 3: Deploy to PythonAnywhere

1. **Sign up at PythonAnywhere**
   - Go to https://www.pythonanywhere.com/
   - Create free account

2. **Upload Code**
   - Go to "Files" tab
   - Upload all your project files
   - Or use Git to clone your repository

3. **Install Dependencies**
   - Go to "Consoles" → "Bash"
   - Run: `pip install --user -r requirements.txt`

4. **Configure Web App**
   - Go to "Web" tab
   - Click "Add a new web app"
   - Choose "Flask"
   - Set WSGI file to point to your `app.py`

5. **Set Environment Variables**
   - In "Web" tab, scroll to "Environment variables"
   - Add your API keys

6. **Reload**
   - Click "Reload" button
   - Your app will be live at: `https://yourusername.pythonanywhere.com`

---

## 📝 Final Deliverables Checklist

- [ ] **Live Deployed URL** - Deploy using one of the options above
- [x] **GitHub Repository** - Create and push code
- [ ] **Demo Video** - Record 30-second screen recording showing:
  - Uploading the assessment PDF
  - Processing animation
  - Results page with verified/inaccurate/false claims highlighted
  - Use OBS Studio, Loom, or Windows Game Bar to record

---

## 🎥 Recording Demo Video

**Using Windows Game Bar:**
1. Press `Win + G` to open Game Bar
2. Click the record button (or `Win + Alt + R`)
3. Open http://localhost:5000 in browser
4. Upload the assessment PDF
5. Show the results page
6. Stop recording (`Win + Alt + R`)
7. Video saved to: `C:\Users\[YourName]\Videos\Captures`

**What to Show (30 seconds):**
- 0-5s: Show the upload interface
- 5-10s: Drag and drop PDF
- 10-20s: Show processing animation
- 20-30s: Show results with false claims highlighted

---

## ✅ Submission

Once deployed, submit:
1. **Live URL**: `https://your-app-url.com`
2. **GitHub Repo**: `https://github.com/yourusername/fact-checker`
3. **Demo Video**: Upload to Google Drive/YouTube and share link
