from flask import Flask
import threading
import asyncio
import os
from bot import main

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot Running"

# NEW
def run_flask():
    import os
    port = int(os.environ.get("PORT", 8000))
    app.run(host="0.0.0.0", port=port, use_reloader=False)


if __name__ == "__main__":

    flask_thread = threading.Thread(
        target=run_flask,
        daemon=True
    )

    flask_thread.start()

    print("Flask Started")

    asyncio.run(main())
