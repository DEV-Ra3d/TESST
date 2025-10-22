import os
import asyncio
from pyrogram import Client, filters
from pyrogram.types import Message
from dotenv import load_dotenv
import json

# تحميل المتغيرات البيئية
load_dotenv()

# قراءة الإعدادات
with open('config.json', 'r', encoding='utf-8') as f:
    config = json.load(f)

# معلومات البوت
API_ID = int(os.getenv("API_ID"))
API_HASH = os.getenv("API_HASH")
BOT_TOKEN = os.getenv("BOT_TOKEN")
DEVELOPER_ID = int(os.getenv("DEVELOPER_ID", config.get("sourse_dev", 9537788181885)))

# قائمة المطورين
DEVS = [DEVELOPER_ID]

# إنشاء عميل البوت
app = Client(
    "TelegramBot",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=BOT_TOKEN,
    plugins=dict(root="plugins")
)

async def start_zombiebot():
    """بدء تشغيل البوت"""
    try:
        await app.start()
        print("✅ تم تشغيل البوت بنجاح!")
        
        # إرسال رسالة للمطور عند بدء التشغيل
        try:
            await app.send_message(
                DEVELOPER_ID,
                "🤖 **تم تشغيل البوت بنجاح!**\n\n"
                f"🆔 **معرف المطور:** `{DEVELOPER_ID}`\n"
                f"🔗 **معرف البوت:** `@{(await app.get_me()).username}`"
            )
        except Exception as e:
            print(f"❌ خطأ في إرسال رسالة البدء: {e}")
            
        return app
    except Exception as e:
        print(f"❌ خطأ في تشغيل البوت: {e}")
        return None

# دالة للتحقق من المطور
def is_dev(user_id: int) -> bool:
    """التحقق من أن المستخدم مطور"""
    return user_id in DEVS

# فلتر المطورين
dev_filter = filters.user(DEVS)

if __name__ == "__main__":
    asyncio.run(start_zombiebot())
