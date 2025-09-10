from telethon import TelegramClient, functions
from telethon.sessions import StringSession
import asyncio, datetime
from flask import Flask
import threading

# --------------------
api_id = 12128667
api_hash = "ff5f1b17331d23aa0329ced7f255d408"
string = "1BJWap1sBu3vVPj6cwAjRVwxK-2Mbc9qw8VKzSyUk2QnWWHEuQHOYprYRX4z6GhHEph3mJ1hlzkCKNRYduZfeQM0n-JNIEx7qgWhoLRHcozuhLhDEOdKPdtxrcTiv0rm2Yz5KHYQAe6ZVdHpLbRC73QvQJsnVq-fiQDp5HH-wZpp19YOPpi9KAV6YTb5M1mJlnRdD8sA3dLnbzuALDSqgNkd_IbQY2Bv8Fe-SNSkLbyIfzKeY26ERLLbwAZnhXrmEk1OZTcpQfO6vna49RzD1qMMprJ0P4R2AS-4Akl-wwjCtBKXHdb-GFN594COSIblxmscnqJUcx0NhRgUr_M-8O_NtsMNlWmI="
# --------------------

client = TelegramClient(StringSession(string), api_id, api_hash)
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
        await asyncio.sleep(60)

async def runner():
    await client.start()
    await update_bio()

def start_loop():
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(runner())

if __name__ == "__main__":
    # اجرای حلقه تلگرام در یک ترد جدا
    t = threading.Thread(target=start_loop)
    t.start()

    # اجرای Flask برای Render
    app.run(host="0.0.0.0", port=10000)
