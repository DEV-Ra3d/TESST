import asyncio
import json
import os
from pyrogram import Client
from pytgcalls import PyTgCalls
from dotenv import load_dotenv

# تحميل المتغيرات البيئية
load_dotenv()

# تحميل إعدادات التكوين
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

# معلومات API من المتغيرات البيئية (آمنة)
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")

# معرف المالك من التكوين
owner_id = config['sourse_dev']

# قائمة المطورين - المطور الجديد: رعد
DEVS = [7788181885]  # رعد فقط

# إنشاء عميل البوت
bot = Client(
    "zombie_bot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

# إنشاء عميل المكالمات الصوتية
call_py = PyTgCalls(bot)

async def start_zombiebot():
    """بدء تشغيل البوت"""
    try:
        await bot.start()
        await call_py.start()
        print("✅ تم تشغيل البوت بنجاح")
        print(f"🤖 اسم البوت: {(await bot.get_me()).first_name}")
        print(f"👤 معرف البوت: @{(await bot.get_me()).username}")
        print(f"👨‍💻 المطور: {config.get('dev_name', 'رعد')}")
        print(f"📢 قناة السورس: @{config.get('channel_source', 'RA3D_OFFICEL')}")
        await asyncio.Event().wait()
    except Exception as e:
        print(f"❌ خطأ في تشغيل البوت: {e}")

if __name__ == "__main__":
    asyncio.run(start_zombiebot())
