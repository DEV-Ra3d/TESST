import asyncio
import json
import os
from pyrogram import Client
from pytgcalls import PyTgCalls

# تحميل إعدادات التكوين
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

# معلومات API
API_ID = int("8186557")
API_HASH = "efd77b34c69c164ce158037ff5a0d117"

# معلومات البوت من التكوين
BOT_TOKEN = "7417570990:AAHrUfsk5CKgVBWPrmY3nRVzRySUGn2lKAw"
owner_id = config['sourse_dev']

# قائمة المطورين
DEVS = [7788181885]

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
        await asyncio.Event().wait()
    except Exception as e:
        print(f"❌ خطأ في تشغيل البوت: {e}")

if __name__ == "__main__":
    asyncio.run(start_zombiebot())
