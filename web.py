import os
import threading
from flask import Flask
from bot import app, main

flask_app = Flask(__name__)

@flask_app.route("/")
def home():
    return "Bot is Running"


def run_flask():
    port = int(os.environ.get("PORT", 8000))

    flask_app.run(
        host="0.0.0.0",
        port=port,
        use_reloader=False
    )


if __name__ == "__main__":

    flask_thread = threading.Thread(
        target=run_flask,
        daemon=True
    )

    flask_thread.start()

    print("Flask Started")

    app.run(main())
