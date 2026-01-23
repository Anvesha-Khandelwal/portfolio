# Portfolio Backend Setup Guide

## Features

✨ **Interactive Portfolio** with fun animations:
- Confetti effects when clicking stats
- Easter eggs and emoji interactions
- Typing animations
- Smooth scroll animations
- Canvas-based animated character

📧 **Email Notifications** when someone messages:
- Automatic email sent to your inbox
- Messages stored locally on server
- RESTful API endpoints to retrieve messages

## Prerequisites

- Node.js (v14 or higher)
- npm or yarn
- Gmail account (for email notifications)

## Installation

### 1. Install Backend Dependencies

```bash
cd backend
npm install
```

### 2. Configure Email Notifications

#### Option A: Using Gmail (Recommended)

1. Go to [Google Account Settings](https://myaccount.google.com/apppasswords)
2. Select your Gmail account
3. Generate an App Password for "Mail" and "Windows"
4. Copy the 16-character password

#### Option B: Using Other Email Services

Update the `EMAIL_SERVICE` in `.env` with your provider (e.g., 'outlook', 'yahoo', etc.)

### 3. Setup .env File

Create/update `backend/.env`:

```env
EMAIL_SERVICE=gmail
EMAIL_USER=your-email@gmail.com
EMAIL_PASSWORD=your-16-char-app-password
NOTIFY_EMAIL=your-email@gmail.com
PORT=3000
NODE_ENV=development
```

**Important:** 
- Do NOT use your regular Gmail password
- Use the App Password generated in step 2
- Keep this file private and never commit it to git

## Running the Server

### Development Mode (with auto-restart)

```bash
cd backend
npm run dev
```

### Production Mode

```bash
cd backend
npm start
```

The server will start at `http://localhost:3000`

## API Endpoints

### Send Message
```
POST /api/send-message
Content-Type: application/json

{
  "name": "John Doe",
  "email": "john@example.com",
  "message": "I'd like to work with you..."
}
```

**Response:**
```json
{
  "success": true,
  "message": "Your message has been received!",
  "messageId": 1234567890
}
```

### Get All Messages
```
GET /api/messages
```

Returns all stored messages sorted by newest first.

### Get Single Message
```
GET /api/messages/:id
```

Returns a specific message by ID.

### Health Check
```
GET /api/health
```

Returns server status.

## Troubleshooting

### Email Not Sending?

1. **Check .env configuration:**
   ```bash
   - EMAIL_SERVICE is set correctly
   - EMAIL_USER is your full Gmail address
   - EMAIL_PASSWORD is the 16-char App Password (not regular password)
   - NOTIFY_EMAIL is set to receive notifications
   ```

2. **Less Secure Apps:**
   - If using regular Gmail password, enable [Less Secure App Access](https://myaccount.google.com/lesssecureapps)
   - App Passwords are more secure and recommended

3. **Server Logs:**
   - Check console for error messages
   - Messages will still be stored locally even if email fails

### Port Already in Use?

```bash
# Windows
netstat -ano | findstr :3000

# Change PORT in .env
PORT=3001
```

### CORS Issues?

Already configured in `server.js`. If issues persist:
- Check browser console for errors
- Ensure server is running
- Verify URL matches exactly

## Features Explained

### 🎉 Fun Animations

- **Confetti Effect:** Click on stats to trigger confetti
- **Easter Egg:** Click on the name "Hi, I'm Anvesha 👋" repeatedly for surprises
- **Emoji Interactions:** Hover over fun emojis for animations
- **Pulse Animation:** Stats pulse when clicked
- **Typing Animation:** Subtitle has a typing effect

### 📧 Message Notifications

When someone submits the contact form:
1. Form data is validated
2. Email notification is sent to you
3. Message is stored locally
4. User sees success confirmation with confetti
5. You can retrieve all messages via API

## Deployment

### Heroku Deployment

1. Create `Procfile` in backend folder:
   ```
   web: node server.js
   ```

2. Deploy:
   ```bash
   heroku create portfolio-backend
   heroku config:set EMAIL_USER=your-email@gmail.com
   heroku config:set EMAIL_PASSWORD=your-app-password
   heroku config:set NOTIFY_EMAIL=your-email@gmail.com
   git push heroku main
   ```

3. Update portfolio HTML to use deployed URL:
   ```javascript
   fetch('https://your-heroku-app.herokuapp.com/api/send-message', ...)
   ```

### Other Platforms

- **Vercel:** Add backend as serverless functions
- **Railway:** Similar to Heroku, easy deployment
- **AWS EC2:** Traditional server deployment

## Security Notes

⚠️ **Important:**
- Never commit `.env` to git
- Use environment variables in production
- Add authentication for `/api/messages` endpoint
- Implement rate limiting for production
- Validate all email inputs
- Consider adding reCAPTCHA for form

## Future Enhancements

- [ ] Add database (MongoDB, PostgreSQL)
- [ ] Implement authentication
- [ ] Add message dashboard
- [ ] File uploads in messages
- [ ] Admin panel for managing messages
- [ ] Analytics and metrics
- [ ] Message templates

## Support

If email isn't working:
1. Check browser console (F12)
2. Check server console for errors
3. Verify .env variables are set correctly
4. Messages are ALWAYS stored locally, even if email fails

## License

MIT
