# 🚀 Quick Start Guide

## What's New?

Your portfolio now has:
✨ **Fun & Interactive** - Confetti, emojis, animations, Easter eggs
📧 **Email Notifications** - Get notified when someone messages you
🎉 **Engaging UI** - Click everything! Try the stats, skills, and name

## Quick Setup (5 minutes)

### Step 1: Install Dependencies
```bash
cd backend
npm install
```

### Step 2: Configure Email (Optional but Recommended)

**Get Gmail App Password:**
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows"
3. Google will generate a 16-character password
4. Copy it

**Update backend/.env:**
```
EMAIL_SERVICE=gmail
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=paste-16-char-password-here
NOTIFY_EMAIL=your-email@gmail.com
```

### Step 3: Run the Server
```bash
npm start
# or for development with auto-reload:
npm run dev
```

Server will run at: `http://localhost:3000`

## Try It Out!

### Frontend (Works even without backend)
- **Click your name** "Hi, I'm Anvesha 👋" - Easter eggs!
- **Click stat cards** - Triggers confetti animation
- **Click skill cards** - Wobble animation
- **Fill contact form** - Green success notification

### With Backend Running
- Contact form sends real email notification
- Messages stored in server
- View all messages at: `http://localhost:3000/api/messages`

## Features Overview

### 🎊 Interactive Elements
- **Confetti Effects** - Click stats to celebrate
- **Easter Eggs** - Click the name multiple times
- **Typing Animation** - Subtitle has typewriter effect
- **Pulse & Wobble** - Cards react to clicks
- **Smooth Animations** - Everything animates on scroll

### 💬 Contact Form
- Validates all fields
- Shows success message with confetti
- Sends email notification (if backend configured)
- Stores message locally

### 📊 API Endpoints
```
POST   /api/send-message     - Send a message
GET    /api/messages         - Get all messages  
GET    /api/messages/:id     - Get specific message
GET    /api/health           - Check server status
```

## Troubleshooting

### Email Not Working?
- Check .env is in `backend/` folder
- Make sure you used the 16-char App Password, not Gmail password
- Check server console for errors
- Messages still save locally even if email fails

### Server Won't Start?
```bash
# Check if port 3000 is in use
netstat -ano | findstr :3000

# If yes, change PORT in .env to 3001
PORT=3001
```

### Port 3000 in Use?
```bash
# Kill the process (Windows)
taskkill /PID <process-id> /F

# Or change PORT in .env
PORT=3001
```

## File Structure

```
portfolio/
├── index.html                 ← Your portfolio (enhanced with fun stuff)
├── backend/
│   ├── server.js             ← Express server
│   ├── package.json          ← Dependencies
│   ├── .env                  ← Your email config (⚠️ keep private!)
│   ├── .gitignore            ← Don't commit .env!
│   └── README.md             ← Full documentation
```

## Next Steps

### To Deploy:
1. **Heroku:** `heroku create` and `git push heroku`
2. **Railway:** Drag and drop folder
3. **Replit:** Import from GitHub
4. **AWS/Digital Ocean:** Follow their Node.js guides

### To Enhance:
- Add database for messages
- Create admin dashboard
- Add more Easter eggs
- Customize animations
- Add sound effects

## Commands Reference

```bash
# Install dependencies
npm install

# Start server
npm start

# Development with auto-reload
npm run dev

# Check server health
curl http://localhost:3000/api/health

# View all messages
curl http://localhost:3000/api/messages

# Send test message
curl -X POST http://localhost:3000/api/send-message \
  -H "Content-Type: application/json" \
  -d '{"name":"Test","email":"test@example.com","message":"Hello!"}'
```

## Have Fun! 🎉

Your portfolio now:
- ✨ Looks professional & minimal
- 🎊 Is super fun to interact with
- 📧 Notifies you of messages
- 💾 Stores everything locally
- 🚀 Ready to deploy

Start the server and click around! 🚀
