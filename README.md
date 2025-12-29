# Daily Career Focus Email

A simple automation that sends **one clear career focus reminder every morning at 8:00 AM (IST)**.  
Built to eliminate distraction and enforce **single-goal discipline**.

This project is designed to run as a **serverless Python function on Vercel**, using Vercel Cron to trigger daily emails.

---

## Why This Exists

Most people fail not because of lack of knowledge, but because:
- They chase too many goals at once
- They start the day without direction
- They react instead of executing

This tool enforces:
- One goal
- One direction
- Daily accountability

---

## Features

- 📌 Single career goal focus (no distractions)
- ⏰ Automated daily email at 8:00 AM IST
- 📬 SMTP-based email delivery
- ⚡ Serverless & lightweight
- 🔒 No database, no tracking, no noise

---

## Tech Stack

- **Python**
- **Vercel Serverless Functions**
- **Vercel Cron**
- **SMTP (Gmail / Zoho / SendGrid)**

---

## Project Structure
```.
├── api/
│ └── focus.py 
├── focus.py 
├── mailer.py # SMTP email sender
├── vercel.json # Cron configuration
└── README.md
```

---

## 🔄 How It Works

1. You define **ONE career goal** in the code
2. Vercel Cron triggers the function every morning
3. The function:
   - Generates a strict daily focus message
   - Sends it to your email
4. You start the day with clarity instead of chaos

---

## ⚙️ Setup Guide

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/daily-career-focus.git
cd daily-career-focus
```
---
### 2️⃣ Configure Environment Variables (Vercel)

In your Vercel Dashboard → Project → Settings → Environment Variables, add:
```
EMAIL_FROM=your_email@example.com
EMAIL_TO=your_email@example.com
SMTP_HOST=smtp.gmail.com
SMTP_USER=your_email@example.com
SMTP_PASS=your_app_password

GOAL=your_goal
```

### 4️⃣ Cron Schedule (8:00 AM IST)

Configured in vercel.json:

```
{
  "crons": [
    {
      "path": "/api/focus",
      "schedule": "30 2 * * *"
    }
  ]
}
```


🕒 02:30 UTC = 08:00 IST

### 🚀 Deployment

Install Vercel CLI (once):

```
npm install -g vercel
```

Deploy:

```
vercel deploy
```
