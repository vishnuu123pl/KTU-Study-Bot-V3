# 🎓 KTU Study Bot V3

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python" />
  <img src="https://img.shields.io/badge/Pyrogram-2.x-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Telegram-Bot-blue?style=for-the-badge&logo=telegram" />
  <img src="https://img.shields.io/badge/License-MIT-yellow?style=for-the-badge" />
</p>

A **Telegram bot** built for **KTU (APJ Abdul Kalam Technological University) B.Tech students** to access study materials, previous year questions, model papers, and more — all organized by branch, scheme, and semester.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📚 Study Materials / Notes | Access semester-wise notes for all branches |
| 📝 Previous Year Questions (PYQ) | Browse subject-wise PYQs |
| 📖 Model Papers | Download model exam papers |
| 🎥 Video Resources | Links to helpful video content |
| 🏫 Multi-Branch Support | CSE, ECE, EEE, ME, Civil, ICE |
| 📅 Scheme Support | 2019 and 2024 KTU schemes |
| 🗂 Semester-wise Navigation | Semesters 1–8, fully organized |
| 📢 Admin Broadcast | Send announcements to all users |
| 🛠 Admin Upload Panel | Upload, list, and delete resources via Telegram |
| 👥 User Tracking | Tracks registered users for broadcasts |

---
## ⚠ Known Limitations

Current version uses local JSON storage (`storage.json`, `users.json`) instead of a dedicated database.

### Limitations

- Data may reset after some redeployments or server resets
- Not recommended for large-scale public usage
- Uploaded resources depend on local file storage
- No persistent cloud database integration yet
- Designed for testing / beta usage currently

For better stability in production, migrate to:

- MongoDB
- PostgreSQL
- Redis
- Supabase

## 🗂 Project Structure

```
KTU-Study-Bot-V3/
├── bot.py                  # Pyrogram client setup and entry point
├── web.py                  # Flask web server + bot launcher (for deployment)
├── config.py               # Loads environment variables
├── requirements.txt        # Python dependencies
├── Dockerfile              # Docker container config
├── Procfile                # For Heroku / Railway deployment
├── runtime.txt             # Python version for Heroku
├── start.sh                # Shell startup script
├── storage.json            # Stores uploaded file IDs (auto-created)
├── users.json              # Tracks bot users (auto-created)
├── .env.example            # Sample environment file
│
├── data/                   # Subject lists per branch
│   ├── __init__.py         # Exports combined DATA dict
│   ├── cse.py
│   ├── ece.py
│   ├── eee.py
│   ├── me.py
│   ├── civil.py
│   └── ice.py
│
└── plugins/                # Bot command and callback handlers
    ├── start.py            # /start command, welcome message
    ├── scheme.py           # Scheme selection (2019 / 2024)
    ├── semester.py         # Semester selection
    ├── branch.py           # Branch selection
    ├── subject.py          # Subject listing
    ├── resources.py        # Resource type selector (notes/pyq/model/video)
    ├── filesender.py       # Sends files from storage.json
    ├── back.py             # Back navigation
    ├── about.py            # About section
    ├── admin.py            # Admin help panel (/admin)
    ├── admin_upload.py     # Upload/delete/list/stats commands
    ├── broadcast.py        # Broadcast messages to all users
    └── getid.py            # (Commented) Helper to get file IDs
```

---

## ⚙️ Environment Variables

Create a `.env` file in the root directory using `.env.example` as a template:

```env
API_ID=your_telegram_api_id
API_HASH=your_telegram_api_hash
BOT_TOKEN=your_bot_token
ADMINS=123456789
```

| Variable | Description | Where to Get |
|---|---|---|
| `API_ID` | Telegram API ID | [my.telegram.org](https://my.telegram.org) |
| `API_HASH` | Telegram API Hash | [my.telegram.org](https://my.telegram.org) |
| `BOT_TOKEN` | Bot token | [@BotFather](https://t.me/BotFather) on Telegram |
| `ADMINS` | Your Telegram user ID (integer) | [@userinfobot](https://t.me/userinfobot) |

---

## 🚀 Local Setup & Run

### Prerequisites

- Python 3.11+
- pip

### Steps

```bash
# 1. Clone the repository
git clone https://github.com/YOUR_USERNAME/KTU-Study-Bot-V3.git
cd KTU-Study-Bot-V3

# 2. Install dependencies
pip install -r requirements.txt

# 3. Create your .env file
cp .env.example .env
# Edit .env and fill in your credentials

# 4. Run the bot
python web.py
```

The bot will start and the Flask health endpoint will be available at `http://localhost:8000`.

---

## 🐳 Docker Setup

```bash
# Build the image
docker build -t ktu-study-bot .

# Run with environment variables
docker run -d \
  -e API_ID=your_api_id \
  -e API_HASH=your_api_hash \
  -e BOT_TOKEN=your_bot_token \
  -e ADMINS=your_user_id \
  -p 8000:8000 \
  ktu-study-bot
```

---

## ☁️ Deployment Guide

### 🟢 Free Platforms

#### 1. Koyeb (Recommended – Free Tier Available)

1. Create an account at [koyeb.com](https://www.koyeb.com)
2. Click **Create App** → **Deploy from GitHub**
3. Connect your repository
4. Set **Run command** to `python web.py`
5. Add environment variables under **Environment**:
   - `API_ID`, `API_HASH`, `BOT_TOKEN`, `ADMINS`
6. Choose the **Free** instance type and deploy

> ✅ Free tier includes 1 web service. Works well for Telegram bots.

---

#### 2. Railway (Free Tier Available)

1. Go to [railway.app](https://railway.app) and sign in with GitHub
2. Click **New Project** → **Deploy from GitHub Repo**
3. Select your repository
4. Add variables under **Variables** tab:
   - `API_ID`, `API_HASH`, `BOT_TOKEN`, `ADMINS`
5. Railway auto-detects the `Procfile` and deploys automatically

> ✅ Free tier gives $5/month free credits. Suitable for small bots.

---

#### 3. Render (Free Tier Available)

1. Go to [render.com](https://render.com) and connect GitHub
2. Create a **New Web Service**
3. Set **Build Command**: `pip install -r requirements.txt`
4. Set **Start Command**: `python web.py`
5. Add environment variables in the dashboard
6. Deploy

> ⚠️ Free tier sleeps after 15 minutes of inactivity. Use an uptime monitor like UptimeRobot to ping the Flask `/` endpoint.

---

#### 4. Fly.io (Free Tier Available)

1. Install the Fly CLI: `curl -L https://fly.io/install.sh | sh`
2. Login: `fly auth login`
3. Launch: `fly launch` (auto-detects Dockerfile)
4. Set secrets:
   ```bash
   fly secrets set API_ID=... API_HASH=... BOT_TOKEN=... ADMINS=...
   ```
5. Deploy: `fly deploy`

> ✅ Free tier includes 3 shared VMs. Good Docker support.

---

### 💳 Paid Platforms

| Platform | Pricing | Notes |
|---|---|---|
| **Heroku** | From $5/month | Reliable, easy to use. Uses `Procfile` and `runtime.txt` — already configured in this repo. |
| **DigitalOcean App Platform** | From $5/month | Full Docker support, easy GitHub integration |
| **AWS EC2 / Lightsail** | From $3.5/month | Most control, requires server management knowledge |
| **Google Cloud Run** | Pay-per-use | Serverless Docker containers, free tier available |
| **VPS (Contabo, Hetzner, etc.)** | From $4–6/month | Best value for always-on bots; run with `nohup python web.py &` or `systemd` |

---

#### Heroku (Paid) – Quick Steps

```bash
# Install Heroku CLI, then:
heroku login
heroku create your-app-name
heroku config:set API_ID=... API_HASH=... BOT_TOKEN=... ADMINS=...
git push heroku main
```

---

## 🛠 Admin Commands

These commands are restricted to the user IDs listed in `ADMINS`.

| Command | Description |
|---|---|
| `/admin` | Show admin help panel |
| `/upload <category> <year> <branch> <sem> <subject>` | Start upload session, then send PDF |
| `/done` | End active upload session |
| `/delete <category> <year> <branch> <sem> <subject>` | Delete a stored resource |
| `/list` | List all uploaded resource keys |
| `/stats` | Show total uploaded resources |
| `/broadcast <message>` | Send a message to all bot users |

**Upload Example:**
```
/upload notes 2024 cse sem1 maths
```
Then send a PDF file. Repeat for multiple files. Use `/done` when finished.

---

## 🤖 Bot Usage Flow

```
/start
  └── 🎓 B.Tech
        └── Select Scheme (2019 / 2024)
              └── Select Semester (1–8)
                    └── Select Branch (CSE / ECE / EEE / ME / Civil / ICE)
                          └── Select Subject
                                └── Choose Resource (Notes / PYQ / Model / Video)
                                      └── 📄 File sent!
```

---

## 📦 Dependencies

```
pyrogram      # Telegram MTProto client
tgcrypto      # Faster encryption for Pyrogram
python-dotenv # Load .env variables
flask         # Lightweight web server (for health check on deployment platforms)
```

Install all with:
```bash
pip install -r requirements.txt
```

---

## 📝 Notes for Contributors

- Subject lists are in `data/<branch>.py` — add or edit subjects there.
- Resources are stored in `storage.json` using keys like `notes_2024_cse_sem1_maths`.
- Users are tracked in `users.json` for broadcast support.
- Both JSON files are auto-created; **do not commit them** (already in `.gitignore`).

---

## 📄 License

This project is licensed under the **MIT License**. See [LICENSE](LICENSE) for details.

---

## 🙌 Built With ❤️ for KTU Students

If this bot helped you, consider ⭐ starring the repo and sharing it with your classmates!
