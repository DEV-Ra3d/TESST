from pyrogram import Client, filters
from pyrogram.types import Message
import json

# تحميل إعدادات التكوين
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

@Client.on_message(filters.command("start") & filters.private)
async def start_command(client: Client, message: Message):
    """أمر البدء"""
    user_name = message.from_user.first_name
    bot_name = config.get('BOT_NAME', 'رعد بوت')
    source_channel = config.get('channel_source', 'RA3D_OFFICEL')
    
    welcome_text = f"""
🎉 أهلاً وسهلاً {user_name}!

🤖 مرحباً بك في {bot_name}
⚡ بوت متطور ومتعدد الاستخدامات

📢 قناة السورس: @{source_channel}
👨‍💻 المطور: {config.get('dev_name', 'رعد')}

🔥 استخدم الأوامر التالية:
/help - عرض المساعدة
/info - معلومات البوت
"""
    
    await message.reply_text(welcome_text)

@Client.on_message(filters.command("help") & filters.private)
async def help_command(client: Client, message: Message):
    """أمر المساعدة"""
    help_text = f"""
📋 **قائمة الأوامر المتاحة:**

🔹 /start - بدء البوت
🔹 /help - عرض هذه المساعدة
🔹 /info - معلومات البوت
🔹 /ping - فحص سرعة البوت

👨‍💻 **المطور:** {config.get('dev_name', 'رعد')}
📢 **قناة السورس:** @{config.get('channel_source', 'RA3D_OFFICEL')}
👥 **جروب الدعم:** @{config.get('gr', 'KOJLM')}
"""
    
    await message.reply_text(help_text)

@Client.on_message(filters.command("info") & filters.private)
async def info_command(client: Client, message: Message):
    """معلومات البوت"""
    info_text = f"""
ℹ️ **معلومات البوت:**

🤖 **الاسم:** {config.get('BOT_NAME', 'رعد بوت')}
🎨 **التصميم:** {config.get('Source_design', 'ᏚᎾᏌᎡᏟᎬ RA3D')}
👨‍💻 **المطور:** {config.get('dev_name', 'رعد')}
📱 **معرف المطور:** {config.get('source_devv', 'JX_F9')}

📢 **قناة السورس:** @{config.get('channel_source', 'RA3D_OFFICEL')}
👥 **جروب الدعم:** @{config.get('gr', 'KOJLM')}

⚡ **حالة البوت:** يعمل بكفاءة عالية
🔄 **الإصدار:** 2.0
"""
    
    await message.reply_text(info_text)

@Client.on_message(filters.command("ping"))
async def ping_command(client: Client, message: Message):
    """فحص سرعة البوت"""
    await message.reply_text("🏓 Pong! البوت يعمل بسرعة ممتازة ⚡")
