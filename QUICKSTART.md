# Portfolio Setup & Quick Start

## ⚡ Quick Start (2 minutes)

### Windows Users:
```
1. Double-click: setup.bat
2. Double-click: start.bat
3. Open: http://localhost:3000
```

### Mac/Linux Users:
```bash
cd backend
npm install
npm start
```

Then open: **http://localhost:3000**

---

## 🎊 Features

✨ **Interactive Animations**
- Click your name for easter eggs
- Click stat cards for confetti
- Smooth scroll animations
- Professional minimal design

📧 **Contact Form with Notifications**
- Form submissions are saved to `backend/messages.json`
- Optional: Email notifications (see setup below)
- Messages persist even after server restart

---

## 📧 Email Notifications Setup (Optional)

Want email notifications when someone submits the form?

### Step 1: Get Gmail App Password
1. Go to https://myaccount.google.com/apppasswords
2. Select "Mail" and "Windows"
3. Copy the 16-character password

### Step 2: Edit backend/.env
```
EMAIL_SERVICE=gmail
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=paste-16-char-password-here
NOTIFY_EMAIL=your-email@gmail.com
```

### Step 3: Restart Server
```bash
npm start
```

Done! 📧

---

## 🗂️ File Structure

```
portfolio/
├── index.html                    ← Your portfolio
├── SETUP.md                      ← This file
├── setup.bat                     ← Windows setup
├── start.bat                     ← Windows launcher
│
└── backend/
    ├── server.js                 ← Express server
    ├── package.json              ← Dependencies
    ├── .env                      ← Configuration
    ├── .gitignore                ← Git ignore
    ├── messages.json             ← Saved messages
    └── README.md                 ← API documentation
```

---

## 🎯 Try These Features

- **Click your name** → Easter eggs appear
- **Click stat cards** → Confetti animation
- **Click skill cards** → Wobble effect
- **Scroll down** → Cards fade in
- **Fill contact form** → Message gets saved & success notification

---

## 🆘 Troubleshooting

**Server won't start?**
```bash
cd backend
npm install
npm start
```

**Port 3000 in use?**
```
Edit backend/.env:
PORT=3001
```

**Messages not saving?**
- Check that `backend/messages.json` exists
- Restart the server
- Check server console for errors

**Email not working?**
- Check `.env` has correct Gmail credentials
- Use 16-char App Password (not regular password)
- Messages still save even if email fails

---

## 📊 View Saved Messages

**In your browser:**
```
http://localhost:3000/api/messages
```

**In terminal:**
```bash
cat backend/messages.json
```

---

## 📚 More Info

See `backend/README.md` for full API documentation.

---

## 🚀 Ready to Deploy?

1. Update contact info in `index.html`
2. Deploy backend to Heroku/Railway
3. Deploy frontend to Vercel/Netlify
4. Configure email credentials in production

See `backend/README.md` for deployment guides.

---

**Enjoy your portfolio!** 🎉
