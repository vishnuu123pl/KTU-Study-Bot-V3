from flask import Flask
import threading
import asyncio
from bot import main

app = Flask(__name__)


@app.route("/")
def home():
    return "Bot Running"


def run_flask():

    app.run(
        host="0.0.0.0",
        port=8000
    )


if __name__ == "__main__":

    flask_thread = threading.Thread(
        target=run_flask,
        daemon=True
    )

    flask_thread.start()

    print("Flask Started")

    asyncio.run(main())
