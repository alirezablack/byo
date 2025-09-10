from telethon import TelegramClient, functions
from telethon.sessions import StringSession
import asyncio, datetime
from flask import Flask
import threading

# --------------------
api_id = 28069133
api_hash = "5ca91588221d1dd9c46d0df1dd4768f0"
string = "1BJWap1sBu3S7VzzCfs5ehWqeK_V6m-6y6tXVMqJ-XGBnSIvNpCcLnfTp78NJuWpPsFA1rhgwMWq3JjWoceV0h7FGYwZkhFmwPj0ssvEjNMRBfs6UsCY_NGADx28bmCHtrunULcdwrmkvYEcJvuouZLJXF9sh0Xs2mbIjnoSTKXVaT8NfPOyp8-3la_l3uYfff1MfZ8muINNcHxkO1wAjfS9f77pDCbSUOItqTOaut9XdciD2p37h4UDyQ18Sgid2hlN1gLXLO51Vg8a0VSQLTuPl6v8IlA2SAs5g6FcMZR6O3r9KItHFmVoYiK7hsOXhBDcXeG0BeCLGG8pMjVl29aA07uuZiWw="
# --------------------

client = TelegramClient(StringSession(string), api_id, api_hash)
app = Flask(__name__)

@app.route("/")
def home():
    return "Bio Updater Running ✅"

# تابع برای تبدیل اعداد به بولد
def bold_numbers(time_str):
    bold_map = str.maketrans("0123456789", "𝟎𝟏𝟐𝟑𝟒𝟓𝟔𝟕𝟖𝟗")
    return time_str.translate(bold_map)

async def update_bio():
    while True:
        # زمان UTC و تبدیل به ایران
        utc_now = datetime.datetime.utcnow()
        iran_time = utc_now + datetime.timedelta(hours=3, minutes=30)
        time_str = iran_time.strftime("%H:%M")
        bold_time = bold_numbers(time_str)

        # بیو با ساعت بولد و شکلک 🕒
        bio_text = f"🕒 {bold_time} | Bio Updater"

        try:
            await client(functions.account.UpdateProfileRequest(about=bio_text))
            print(f"بیو آپدیت شد به: {bio_text}")
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

