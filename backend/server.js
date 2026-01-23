const express = require('express');
const cors = require('cors');
const nodemailer = require('nodemailer');
const dotenv = require('dotenv');
const path = require('path');
const fs = require('fs');

dotenv.config();

const app = express();

// Middleware
app.use(cors());
app.use(express.json());
app.use(express.static(path.join(__dirname, '../')));

// Configure email transporter
const transporter = nodemailer.createTransport({
  service: process.env.EMAIL_SERVICE || 'gmail',
  auth: {
    user: process.env.EMAIL_USER,
    pass: process.env.EMAIL_PASSWORD,
  },
});

// File path for storing messages
const messagesFile = path.join(__dirname, 'messages.json');

// Load messages from file
function loadMessages() {
  try {
    if (fs.existsSync(messagesFile)) {
      const data = fs.readFileSync(messagesFile, 'utf8');
      return JSON.parse(data);
    }
  } catch (error) {
    console.log('No messages file found, starting fresh');
  }
  return [];
}

// Save messages to file
function saveMessages(messages) {
  try {
    fs.writeFileSync(messagesFile, JSON.stringify(messages, null, 2), 'utf8');
  } catch (error) {
    console.error('Error saving messages:', error.message);
  }
}

// Load messages at startup
let messages = loadMessages();

// API endpoint to send message and notify
app.post('/api/send-message', async (req, res) => {
  try {
    const { name, email, message } = req.body;

    // Validate input
    if (!name || !email || !message) {
      return res.status(400).json({ error: 'All fields are required' });
    }

    // Store message locally
    const messageData = {
      id: Date.now(),
      name,
      email,
      message,
      timestamp: new Date().toISOString(),
    };

    messages.push(messageData);
    
    // Save messages to file immediately
    saveMessages(messages);

    // Try to send email notification to you
    try {
      await transporter.sendMail({
        from: process.env.EMAIL_USER,
        to: process.env.NOTIFY_EMAIL,
        subject: `New Portfolio Message from ${name}`,
        html: `
          <h2>New Message from Your Portfolio</h2>
          <p><strong>Name:</strong> ${name}</p>
          <p><strong>Email:</strong> ${email}</p>
          <p><strong>Message:</strong></p>
          <p>${message.replace(/\n/g, '<br>')}</p>
          <p><strong>Received at:</strong> ${new Date().toLocaleString()}</p>
        `,
      });

      console.log(`✅ Email notification sent for message from ${name}`);
    } catch (emailError) {
      console.log(`⚠️ Could not send email notification: ${emailError.message}`);
      console.log(`Message stored locally: ${JSON.stringify(messageData)}`);
    }

    res.json({
      success: true,
      message: 'Your message has been received! I will get back to you soon.',
      messageId: messageData.id,
    });
  } catch (error) {
    console.error('Error processing message:', error);
    res.status(500).json({ error: 'Failed to process message' });
  }
});

// API endpoint to get all messages (protected - can add auth later)
app.get('/api/messages', (req, res) => {
  res.json({
    total: messages.length,
    messages: messages.sort((a, b) => b.timestamp - a.timestamp),
  });
});

// API endpoint to get message by ID
app.get('/api/messages/:id', (req, res) => {
  const messageId = parseInt(req.params.id);
  const message = messages.find((m) => m.id === messageId);

  if (!message) {
    return res.status(404).json({ error: 'Message not found' });
  }

  res.json(message);
});

// Health check endpoint
app.get('/api/health', (req, res) => {
  res.json({
    status: 'Server is running ✅',
    timestamp: new Date().toISOString(),
    messagesCount: messages.length,
  });
});

// Serve portfolio HTML
app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, '../index.html'));
});

// 404 handler
app.use((req, res) => {
  res.status(404).json({ error: 'Endpoint not found' });
});

// Error handler
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ error: 'Internal server error' });
});

const PORT = process.env.PORT || 3000;

app.listen(PORT, () => {
  console.log(`\n🚀 Portfolio server running at http://localhost:${PORT}`);
  console.log(`📧 Email notifications will be sent to: ${process.env.NOTIFY_EMAIL || 'not configured'}`);
  console.log(`\n📝 Configure .env file for email notifications\n`);
});
