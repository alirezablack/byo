from telethon import TelegramClient, functions
import asyncio, datetime
from flask import Flask

# --------------------
api_id = 12128667          # اینو از my.telegram.org بگیر
api_hash = "ff5f1b17331d23aa0329ced7f255d408"  # اینو هم از my.telegram.org بگیر
# --------------------

client = TelegramClient("bio_updater", api_id, api_hash)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bio Updater Running ✅"

async def update_bio():
    while True:
        now = datetime.datetime.now().strftime("🕒 %H:%M")
        try:
            await client(functions.account.UpdateProfileRequest(about=now))
            print(f"بیو آپدیت شد به: {now}")
        except Exception as e:
            print("❌ خطا:", e)
        await asyncio.sleep(60)  # هر ۶۰ ثانیه

async def main():
    await client.start()
    await update_bio()

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.create_task(main())
    app.run(host="0.0.0.0", port=10000)

