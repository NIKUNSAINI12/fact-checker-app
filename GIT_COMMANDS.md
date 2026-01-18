# Git Commands Reference for PowerShell

## ✅ Git Setup Complete!

**Your Configuration:**
- **Username:** NIKUNSAINI12
- **Email:** saininikunj81@gmail.com
- **Repository:** https://github.com/NIKUNSAINI12/fact-checker-app.git
- **Branch:** main

---

## 🚀 Common Git Commands

### Check Status
```powershell
git status
```

### Add Files
```powershell
# Add all files
git add .

# Add specific file
git add filename.py
```

### Commit Changes
```powershell
git commit -m "Your commit message here"
```

### Push to GitHub
```powershell
# Push to main branch
git push origin main

# Force push (use carefully!)
git push origin main --force
```

### Pull from GitHub
```powershell
git pull origin main
```

### View Commit History
```powershell
# View last 5 commits
git log --oneline -n 5

# View detailed history
git log
```

### Check Remote Repository
```powershell
git remote -v
```

### Create a New Branch
```powershell
# Create and switch to new branch
git checkout -b feature-name

# Switch to existing branch
git checkout main
```

### View Branches
```powershell
git branch -a
```

---

## 📝 Typical Workflow

1. **Make changes to your files**
2. **Check what changed:**
   ```powershell
   git status
   ```

3. **Add files to staging:**
   ```powershell
   git add .
   ```

4. **Commit your changes:**
   ```powershell
   git commit -m "Description of changes"
   ```

5. **Push to GitHub:**
   ```powershell
   git push origin main
   ```

---

## 🔧 Useful Commands

### Undo Changes
```powershell
# Discard changes in working directory
git checkout -- filename.py

# Unstage a file
git reset HEAD filename.py
```

### View Differences
```powershell
# See what changed
git diff

# See staged changes
git diff --staged
```

### Clone a Repository
```powershell
git clone https://github.com/username/repo-name.git
```

---

## ⚠️ Important Notes

1. **Always pull before pushing** if working with others:
   ```powershell
   git pull origin main
   git push origin main
   ```

2. **Never commit sensitive files** like `.env` (already in `.gitignore`)

3. **Write meaningful commit messages** that describe what changed

4. **To restart PowerShell with Git in PATH permanently:**
   - Close and reopen PowerShell/VS Code terminal
   - Git will be automatically available

---

## 🎯 Quick Reference

| Command | Description |
|---------|-------------|
| `git status` | Check current status |
| `git add .` | Stage all changes |
| `git commit -m "msg"` | Commit with message |
| `git push origin main` | Push to GitHub |
| `git pull origin main` | Pull from GitHub |
| `git log --oneline` | View commit history |
| `git branch` | List branches |
| `git checkout -b name` | Create new branch |

---

## 🌐 Your Repository

**GitHub URL:** https://github.com/NIKUNSAINI12/fact-checker-app

You can view your code online at this URL!
