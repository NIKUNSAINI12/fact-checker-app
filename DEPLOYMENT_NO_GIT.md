# Quick Deployment Guide (No Git Installed)

Since Git is not installed on your system, here's the easiest way to deploy:

## Option 1: GitHub Desktop (Recommended)

1. **Download GitHub Desktop**
   - Go to: https://desktop.github.com/
   - Install GitHub Desktop

2. **Create Repository**
   - Open GitHub Desktop
   - File → New Repository
   - Name: `fact-checker-app`
   - Local Path: `c:\Users\USER\Desktop\Cog Culture`
   - Click "Create Repository"

3. **Publish to GitHub**
   - Click "Publish repository"
   - Uncheck "Keep this code private" (or keep it private)
   - Click "Publish repository"

4. **Deploy to Render**
   - Go to: https://render.com/
   - Sign up with GitHub
   - New → Web Service
   - Connect your `fact-checker-app` repository
   - Configure:
     - Build Command: `pip install -r requirements.txt`
     - Start Command: `gunicorn app:app`
   - Add Environment Variables:
     - `OPENROUTER_API_KEY`: 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
     - `TAVILY_API_KEY`: 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
     - `FLASK_SECRET_KEY`: random-secret-string
   - Click "Create Web Service"

---

## Option 2: Direct Upload to GitHub (No Git Required)

1. **Create New Repository**
   - Go to: https://github.com/new
   - Repository name: `fact-checker-app`
   - Description: "AI-powered fact-checking web application"
   - Click "Create repository"

2. **Upload Files**
   - Click "uploading an existing file"
   - Drag and drop ALL files from `c:\Users\USER\Desktop\Cog Culture`
   - EXCEPT: `.env` file (keep your API keys private!)
   - Commit message: "Initial commit"
   - Click "Commit changes"

3. **Deploy to Render** (same as above)

---

## Option 3: Use Render's GitHub Integration

1. **Create GitHub Account** (if you don't have one)
   - Go to: https://github.com/signup

2. **Create Repository via Browser**
   - Follow Option 2 above

3. **Deploy**
   - Go to: https://render.com/
   - Sign up with GitHub
   - Follow deployment steps from Option 1

---

## ⚡ Fastest Option: Deploy Without GitHub

**Use PythonAnywhere (No GitHub Required)**

1. Go to: https://www.pythonanywhere.com/registration/register/beginner/
2. Create free account
3. Go to "Files" tab
4. Click "Upload a file"
5. Upload all your Python files (app.py, config.py, etc.)
6. Go to "Web" tab → "Add a new web app"
7. Choose Flask
8. Configure WSGI file
9. Add environment variables
10. Reload

Your app will be live at: `https://yourusername.pythonanywhere.com`

---

## 🎥 After Deployment

1. **Test the live URL**
2. **Record demo video** (Win + G)
3. **Submit**:
   - Live URL
   - GitHub link (if created)
   - Demo video
