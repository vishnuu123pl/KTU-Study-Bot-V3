from dotenv import load_dotenv
import os

load_dotenv()

API_ID = int(os.getenv("API_ID", "0"))
API_HASH = os.getenv("API_HASH", "")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")

# Validate on startup
if not API_ID or API_ID == 0:
    raise ValueError("❌ API_ID is missing or invalid in environment variables")
if not API_HASH:
    raise ValueError("❌ API_HASH is missing in environment variables")
if not BOT_TOKEN:
    raise ValueError("❌ BOT_TOKEN is missing in environment variables")
