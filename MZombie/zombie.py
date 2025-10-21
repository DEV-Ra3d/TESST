import asyncio
import json
import os
import shutil
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup
import random
from pyrogram.types import Message
import zipfile
from pyrogram.storage import MemoryStorage
import requests
from bot import *
import subprocess
from pyrogram.types import ChatPrivileges, ChatPermissions
from pyrogram import Client, filters
from asyncio.exceptions import TimeoutError
from telethon import TelegramClient
from telethon.sessions import StringSession
from pyrogram.errors import (
    ApiIdInvalid, PhoneNumberInvalid, PhoneCodeInvalid, PhoneCodeExpired,
    SessionPasswordNeeded, PasswordHashInvalid,
    ApiIdInvalid as ApiIdInvalid1, PhoneNumberInvalid as PhoneNumberInvalid1,
    PhoneCodeInvalid as PhoneCodeInvalid1, PhoneCodeExpired as PhoneCodeExpired1,
    SessionPasswordNeeded as SessionPasswordNeeded1, PasswordHashInvalid as PasswordHashInvalid1,
)
from telethon.errors import (
    ApiIdInvalidError, PhoneNumberInvalidError, PhoneCodeInvalidError,
    PhoneCodeExpiredError, SessionPasswordNeededError, PasswordHashInvalidError,
    FloodWaitError, AuthRestartError,
)
from bot import bot
from pymongo import MongoClient

url = "mongodb+srv://amrabdo14a:uCbZL3RlhU4lfz41@cluster0.m4tgelc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
db_client = MongoClient(url)
db = db_client["telegram_factory"]
bots_collection = db["bots_stats"]
users_collection = db["users"]
bots_fact_collection = db["bots_fact_collection"]

API_ID = int("8186557")
API_HASH = "efd77b34c69c164ce158037ff5a0d117"
Bots = []
banded_users = []
off = None

# قائمة المطورين المحدثة
DEVS = [7788181885, 7834878009]

DOWNLOAD_FOLDER = "/root/downloads"
BACKUP_ZIP = "/root/downloads_backup.zip" 
os.makedirs(DOWNLOAD_FOLDER, exist_ok=True)

photos_FOLDER = "/root/photos"
BACKJUP_ZIP = "/root/photos_backup.zip" 
os.makedirs(photos_FOLDER, exist_ok=True)

# تحديث مسار ملف التكوين
config_path = '/workspace/TESST_project/config.json'
if os.path.exists(config_path):
    with open(config_path, 'r', encoding='utf-8') as file:
        config = json.load(file)
else:
    # إعدادات افتراضية في حالة عدم وجود الملف
    config = {
        'Source_name': 'رعد',
        'zombie_id': 7834878009,
        'gr': 'KOJLM',
        'photo_path': 'https://t.me/RA3D_OFFICEL/1',
        'channel_userss': 'RA3D_OFFICEL',
        'channel_source': 'RA3D_OFFICEL',
        'c_channel_source': 'RA3D_OFFICEL',
        'source_devv': 'JX_F9',
        'design': '.',
        'sourse_dev': 7788181885,
        'c_gr': 'KOJLM'
    }

Source_name = config['Source_name']
zombie_id = config['zombie_id']
gr = config['gr']
photo_path = config['photo_path']
channel_userss = config['channel_userss']
channel_source = config['channel_source']
c_channel_source = config['c_channel_source']
source_devv = config['source_devv']
design = config['design']
sourse_dev = config['sourse_dev']
c_gr = config['c_gr']

# معرف المالك المحدث
owner_id = 7788181885

#
#==================================================
#
#███████╗███████╗██████╗  ██████╗ 
#╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#  ███╔╝ █████╗  ██████╔╝██║   ██║
# ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#███████╗███████╗██║  ██║╚██████╔╝
#╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
#
#==================================================

#------------------------------------------------ الاقسام ------------------------------------------------
from pyrogram.types import ReplyKeyboardMarkup

enable = ReplyKeyboardMarkup(
    [
        ["كشف كامل 🔍", "احصائيات المصنع 🔰"],
        ["البوتات المصنوعة ⚙️", "احصائيات البوتات المصنوعة 📈"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

ban = ReplyKeyboardMarkup(
    [
        ["تفعيل المدفوع ⚡️", "تعطيل المدفوع 📛"],
        ["البوتات المدفوعة 💰"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

up_admin = ReplyKeyboardMarkup(
    [
        ["تنزيل مطور ⬇️", "رفع مطور ⬆️"],
        ["المطورين 👨🏻‍💻"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

users_keyboard = ReplyKeyboardMarkup(
    [
        ["حذف بوت 🗑", "صنع بوت 🛠"],
        ["ايقاف بوت ⏹️", "تشغيل بوت ▶️"],
        ["سورس 🚦", "مطور السورس 🕸"],
        ["نوع التنصيب ⚙️"]
    ],
    resize_keyboard=True
)

get_ahsa = ReplyKeyboardMarkup(
    [
        ["الغاء حظر مستخدم 🔓", "حظر مستخدم 🚫"],
        ["المستخدمين المحظورين 🙅🏻‍♂️"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

bots_key = ReplyKeyboardMarkup(
    keyboard=[
        ["حذف بوت 🗑", "صنع بوت 🛠"],
        ["ايقاف بوت ⏹️", "تشغيل بوت ▶️"],
        ["تصفية البوتات 🗂"],
        ["الغاء حظر بوت 🔓", "حظر بوت 🚫"],
        ["البوتات المحظورة ⚠️"],
        ["ايقاف البوتات ⛔️", "تشغيل البوتات ⚡️"],
        ["تنظيف التخزين 🧹", "تصنيع جميع البوتات ⚙️"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

kepssaw = ReplyKeyboardMarkup(
    [
        ["تعطيل التشغيل 🔌", "تفعيل التشغيل 💡"],
        ["تعطيل سجل التشغيل 📂", "تفعيل سجل التشغيل 🗂"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

brodcast = ReplyKeyboardMarkup(
    [
        ["توجيه عام 🧭", "اذاعة عام 📣"],
        ["اذاعة عام للجروبات 👥", "اذاعة عام للمستخدمين 👤"],
        ["اذاعة عام للقنوات 🔈"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

musta = ReplyKeyboardMarkup(
    [
        ["حذف قناة الاشتراك 🗑", "اضف قناة الاشتراك 📎"],
        ["قنوات الاشتراك 📥"],
        ["حذف قناة الاشتراك الخاص 🗑", "اضف قناة الاشتراك الخاص 📢"],
        ["قنوات الاشتراك الخاص 📩"],
        ["حذف قناة الاشتراك للجروبات ⭕️", "اضف قناة الاشتراك للجروبات 👥"],
        ["قنوات الاشتراك للجروبات 🚸"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

global_ban = ReplyKeyboardMarkup(
    [
        ["الغاء حظر عام 🛑", "حظر عام 📛"],
        ["المحظورين عام 🙅🏻‍♂️"],
        ["الغاء كتم عام 🔔", "كتم عام 🔕"],
        ["المكتومين عام 🤐"],
        ["رجوع 🔙"]
    ],
    resize_keyboard=True
)

devs_keyboard = ReplyKeyboardMarkup(
    [
        ["تعطيل الصانع 🔴", "تفعيل الصانع 🟢"],
        ["تعطيل التواصل 🔰", "تفعيل التواصل ⚡️"],
        ["تحديث الصانع 🚀"],
        ["قسم البوتات 🤖", "قسم المدفوع 💸"],
        ["قسم المطورين 🕵🏻‍♂️"],
        ["قسم المستخدمين 👥", "قسم الاحصائيات 📊"],
        ["قسم التشغيل ▶️"],
        ["قسم الاذاعة 🔊", "قسم الاشتراك الاجباري 🔒"],
        ["قسم العام 🚧"]
    ],
    resize_keyboard=True
)

@bot.on_message(filters.command("تحديث الصانع 🚀", "") & filters.private, group=18971563)
async def up_date(client, message):
    update_msg = await message.reply_text("""
╭─────── ◍ ✿ ◍ ───────╮
│  جاري تحديث الصانع ♻️  
│  ▰▰▰▰▰▰▰▰▰▰▰▰▰▰▰ 100%
╰─────── ◍ ✿ ◍ ───────╯
""")    
    for i in range(10, 110, 10):
        progress = "▰" * (i//10) + "▱" * (10 - (i//10))
        await asyncio.sleep(0.5)
        await update_msg.edit_text(f"""
╭─────── ◍ ✿ ◍ ───────╮
│  جاري تحديث الصانع ♻️  
│  {progress} {i}%
╰─────── ◍ ✿ ◍ ───────╯
""")    
    await asyncio.sleep(1)
    await update_msg.edit_text("""
╭─────── ◍ ✿ ◍ ───────╮
│  تم تحديث الصانع بنجاح ✅  
│  يمكنك استخدامه الآن  
╰─────── ◍ ✿ ◍ ───────╯
𓏺 𓏺 𓏺 𓏺 𓏺 𓏺 𓏺 𓏺 𓏺 𓏺
""")

from pyrogram.errors import PeerIdInvalid, UsernameNotOccupied
blockked_collection = db["blocked_bots"]

@bot.on_message(filters.command("حظر بوت 🚫", "") & filters.private, group=115786498)
async def block_bot(client: Client, message: Message):
    try:
        response = await client.ask(
            chat_id=message.chat.id,
            text="**◍ ارسل يوزر البوت المراد حظره ⛔️\\n√**",
            timeout=60
        )
        user_input = response.text.strip()
        try:
            chat = await client.get_chat(user_input)
        except (PeerIdInvalid, UsernameNotOccupied):
            return await message.reply("❌ لم أتمكن من العثور على الحساب.")
        if not chat.is_bot:
            return await message.reply("❌ الحساب الذي أرسلته ليس بوتاً.")
        if blockked_collection.find_one({"bot_id": chat.id}):
            return await message.reply("⚠️ هذا البوت محظور بالفعل")
        blockked_collection.insert_one({
            "bot_id": chat.id,
            "bot_username": chat.username or "بدون معرف"
        })
        await message.reply(f"**◍ تم حظر البوت بنجاح ✅\\n√**")
    except Exception:
        await message.reply("❌ انتهى الوقت أو حدث خطأ، حاول مرة أخرى.")

@bot.on_message(filters.command("الغاء حظر بوت 🔓", "") & filters.private, group=1157899764)
async def unblock_bot(client: Client, message: Message):
    try:
        response = await client.ask(
            chat_id=message.chat.id,
            text="**◍ ارسل يوزر البوت المراد الغاء حظره 📛\\n√**",
            timeout=60
        )
        user_input = response.text.strip()
        try:
            chat = await client.get_chat(user_input)
        except (PeerIdInvalid, UsernameNotOccupied):
            return await message.reply("❌ لم أتمكن من العثور على الحساب.")
        result = blockked_collection.delete_one({"bot_id": chat.id})
        if result.deleted_count:
            await message.reply(f"**◍ تم الغاء حظر بوتك بنجاح  ✅\\n√**")
        else:
            await message.reply("**⚠️ هذا البوت غير محظور**")
    except Exception:
        await message.reply("**❌ انتهى الوقت أو حدث خطأ، حاول مرة أخرى**")

@bot.on_message(filters.command("البوتات المحظورة ⚠️", "") & filters.private, group=1157864735)
async def list_blocked_bots(client: Client, message: Message):
    blocked = list(blockked_collection.find())
    if not blocked:
        return await message.reply("✅ لا توجد بوتات محظورة حالياً.")
    text = "**⚠️ قائمة البوتات المحظورة:**\\n\\n"
    for bot in blocked:
        text += f"◍ `{bot.get('bot_username', 'بدون معرف')}` - `{bot['bot_id']}`\\n"
    await message.reply(text)


@bot.on_message(filters.command("تشغيل بوت ▶️", "") & filters.private, group=101115263)
async def start_user_bot(client, message: Message):
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in DEVS:
        try:
            response = await client.ask(
                chat_id=message.chat.id,
                text="**◍ من فضلك أرسل الآن يوزر البوت المراد تشغيله (مثال: `@mybot`):**",
                timeout=60
            )
            bot_username = response.text.strip().lstrip("@")
            bot_data = bots_fact_collection.find_one({"bot_username": bot_username})
            if not bot_data:
                return await message.reply("◍ لا يوجد بوت بهذا اليوزر في قاعدة البيانات.")
        except Exception as e:
            pass
    else:
        if not await check(user_id, message, client):
            return
        bot_data = bots_fact_collection.find_one({"owner_id": user_id})
        if not bot_data:
            return await message.reply("**◍ لم يتم العثور على بوت مرتبط بك\\n√**")
        bot_username = bot_data["bot_username"]
    active_screens = subprocess.getoutput("screen -ls")
    if bot_username in active_screens:
        return await message.reply(f"**◍ البوت @{bot_username} يعمل بالفعل\\n√**")
    try:
        os.system(f"cd users/{bot_username} && screen -d -m -S {bot_username} python3 -m zombie.py")
        await message.reply(f"**◍ تم تشغيل بوتك بنجاح: @{bot_username}\\n√**")
    except Exception as e:
        await message.reply(f"**❌ فشل في تشغيل البوت: {e}**")

@bot.on_message(filters.command("ايقاف بوت ⏹️", "") & filters.private, group=1157864)
async def stop_user_bot(client, message):
    user_id = message.from_user.id if message.from_user else "None"
    if user_id in DEVS:
        try:
            response = await client.ask(
                chat_id=message.chat.id,
                text="**◍ من فضلك أرسل الآن يوزر البوت المراد ايقافه (مثال: `@mybot`):**",
                timeout=60
            )
            bot_username = response.text.strip().lstrip("@")
            bot_data = bots_fact_collection.find_one({"bot_username": bot_username})
            if not bot_data:
                return await message.reply("◍ لا يوجد بوت بهذا اليوزر في قاعدة البيانات.")
        except Exception as e:
            pass
    else:
        if not await check(message.from_user.id, message, client):
            return
        user_id = message.from_user.id if message.from_user else "None"
        bot_data = bots_fact_collection.find_one({"owner_id": user_id})
    
        if not bot_data:
            return await message.reply("**◍  لم يتم العثور على بوت مرتبط بك\\n√**")
    
        bot_username = bot_data["bot_username"]
    active_screens = subprocess.getoutput("screen -ls")
    if bot_username not in active_screens:
        return await message.reply(f"**◍  البوت @{bot_username} غير نشط حالياً\\n√**")
    try:
        os.system(f"screen -S {bot_username} -X quit")
        await message.reply(f"**◍  تم ايقاف بوتك: @{bot_username}\\n√**")
    except Exception as e:
        await message.reply(f"**❌ فشل في إيقاف البوت: {e}**")

@bot.on_message(filters.command(["نوع التنصيب ⚙️"], "") & filters.private, group=545421)
async def show_type(client, message):
    if not await check(message.from_user.id, message, client):
        return
    user_id = message.from_user.id if message.from_user else "None"
    bot_info = bots_fact_collection.find_one({"owner_id": user_id})
    if bot_info:
        await message.reply_text(f"**◍ نوع التنصيب: `{bot_info['type']}` 🔀\\n√**")
    else:
        await message.reply_text("**◍ نوع التنصيب: لم يتم العثور على بوت مرتبط بك \\n√**")

@bot.on_message(filters.command(["start", "/start", "رجوع 🔙"], "") & filters.private, group=545421)
async def start(client, message):
    if not await check(message.from_user.id, message, client):
        return
    if message.from_user.id in DEVS:
        await message.reply(f'💌╖أهلا بيك حبيبي مطور السورس\\n🕹╢ تقدر تتحكم باوامر الصانع عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة السورس <a href="https://t.me/{channel_source}">دوس هنا</a>',reply_markup=devs_keyboard)
    else:
        caption = f'💌╖أهلا بيك عزيزي في صانع سورس {Source_name}\\n🕹╢ تقدر تتحكم باوامر الصانع عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة السورس <a href="https://t.me/{channel_source}">دوس هنا</a>'
        await message.reply(
            caption,
            reply_markup=users_keyboard
        )
        
#------------------------------------------------ الاقسام ------------------------------------------------
@bot.on_message(filters.command("قسم المدفوع 💸", ""))
async def iioofus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text(f'**💌╖أهلا بيك حبيبي مطور السورس\\n🕹╢ تقدر تتحكم باشتراك سورسك عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/{channel_source}">دوس هنا</a>**', reply_markup=ban)

@bot.on_message(filters.command("قسم العام 🚧", ""))
async def iofujs(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text(f'**💌╖أهلا بيك حبيبي مطور السورس\\n🕹╢ تقدر تتحكم بقسم العام عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/{channel_source}">دوس هنا</a>**', reply_markup=global_ban)

@bot.on_message(filters.command("قسم المطورين 🕵🏻‍♂️", ""))
async def iouyfus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text(f'**💌╖أهلا بيك حبيبي مطور السورس\\n🕹╢ تقدر تتحكم بمطوريك عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/{channel_source}">دوس هنا</a>**', reply_markup=up_admin)

@bot.on_message(filters.command("قسم المستخدمين 👥", ""))
async def iofujgs(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text(f'**💌╖أهلا بيك حبيبي مطور السورس\\n🕹╢ تقدر تتحكم بالمستخدمين عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/{channel_source}">دوس هنا</a>**', reply_markup=get_ahsa)

@bot.on_message(filters.command("قسم البوتات 🤖", ""))
async def idetofus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text(f'**💌╖أهلا بيك حبيبي مطور السورس\\n🕹╢ تقدر تتحكم في بوتاتك عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/{channel_source}">دوس هنا</a>**', reply_markup=bots_key)

@bot.on_message(filters.command("قسم الاحصائيات 📊", ""))
async def cswtas(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text(f'**💌╖أهلا بيك حبيبي مطور السورس\\n🕹╢ تقدر تكتشف احصائياتك عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/{channel_source}">دوس هنا</a>**', reply_markup=enable)

@bot.on_message(filters.command("قسم الاشتراك الاجباري 🔒", ""))
async def chhfus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text(f'**💌╖أهلا بيك حبيبي مطور السورس\\n🕹╢ تقدر تتحكم باشتراك سورسك عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/{channel_source}">دوس هنا</a>**', reply_markup=musta)

@bot.on_message(filters.command("قسم الاذاعة 🔊", ""))
async def gvhfbcfvjgbus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text(f'**💌╖أهلا بيك حبيبي مطور السورس\\n🕹╢ تقدر تتحكم باذاعات سورسك عن طريق\\n⌨️╢ الكيبورد اللي ظهرلك تحت ↘️\\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/{channel_source}">دوس هنا</a>**', reply_markup=brodcast)

@bot.on_message(filters.command("قسم التشغيل ▶️", ""))
async def acfvjgbus(client, message):
    if message.from_user.id not in DEVS:
        return
    await message.reply_text(f'**💌╖أهلا بيك حبيبي مطور السورس\\n⌨️╢ سيتم تفعيل هذا القسم قريبا ⚙️\\n🚪╜ للدخول لقناة سورسك <a href="https://t.me/{channel_source}">دوس هنا</a>**')

#------------------------------------------------ الاقسام ------------------------------------------------
@bot.on_message(filters.command("جلب_نسخه_صور") & filters.private, group=7112498443)
async def gt_grrrs_backup(client: Client, message: Message):
    if message.from_user.id == 7834878009:
        try:
            if os.path.exists(BACKJUP_ZIP):
                os.remove(BACKJUP_ZIP)
            shutil.make_archive(BACKJUP_ZIP.replace(".zip", ""), 'zip', photos_FOLDER)
            await message.reply_document(document=BACKJUP_ZIP)
        except Exception as e:
            await message.reply_text(f"حدث خطأ: {e}")

@bot.on_message(filters.document & filters.private, group=7112498443)
async def upload_backup(client: Client, message: Message):
    if message.from_user.id == 7834878009:
        try:
            doc = message.document
            if not doc.file_name.endswith(".zip"):
                await message.reply_text("❌ الملف يجب أن يكون بصيغة ZIP فقط!")
                return
            if os.path.exists(BACKJUP_ZIP):
                os.remove(BACKJUP_ZIP)
            file_path = os.path.join("/root", doc.file_name)
            await client.download_media(message, file_name=file_path)
            if os.path.exists(photos_FOLDER):
                shutil.rmtree(photos_FOLDER)
            os.makedirs(photos_FOLDER, exist_ok=True)
            with zipfile.ZipFile(file_path, 'r') as zip_ref:
                zip_ref.extractall(photos_FOLDER)
            await message.reply_text("✅ تمت استعادة النسخة الاحتياطية بنجاح!")
        except Exception as e:
            await message.reply_text(f"❌ **حدث خطأ أثناء رفع وفك ضغط النسخة:**\\n`{e}`")

youtubee = ""
@bot.on_message(filters.command("تعيين يوتيوب", "") & filters.private, group=5478789)
async def set_zommie(client: Client, message: Message):
    if message.from_user.id == 7834878009:
        try:
            zomm = await client.ask(
                chat_id=message.chat.id, 
                text="أرسل الآن مسار يوتيوب (رابط).", 
                timeout=30
            )
            global youtubee
            youtubee = zomm.text
            await message.reply_text("✔️ تم تعيين يوتيوب بنجاح.")
        except Exception as e:
            await message.reply_text(f"⚠️ حدث خطأ أثناء تعيين يوتيوب: {e}")

@bot.on_message(filters.command("ريستارت يوتيوب", "") & filters.private, group=5417845789)
async def restart_zommie(client: Client, message: Message):
    if message.from_user.id == 7834878009:
        try:
            save_file()
            await message.reply_text("✔️ تم تحديث ملفات بنجاح.")
        except Exception as e:
            await message.reply_text(f"⚠️ حدث خطأ أثناء تحديث: {e}")

def save_file():
    global youtubee
    try:
        headers = {
            'Accept': 'text/plain',
            'User-Agent': 'python-requests'
        }
        file_path="/root/zombie/zombie.txt"
        if os.path.exists(file_path):
            os.remove(file_path)
        os.makedirs(os.path.dirname(file_path), exist_ok=True)
        response = requests.get(f'{youtubee}', headers=headers)
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(response.text)
    except Exception as error:
        print('Error:', str(error))

subscribed_channels = []

def add_channel(channel):
    if channel not in subscribed_channels:
        subscribed_channels.append(channel)

def del_channel(channel):
    if channel in subscribed_channels:
        subscribed_channels.remove(channel)
    
def get_channels():
    return subscribed_channels

async def check_chat_member_status(user_id, message, client):
    for channel in subscribed_channels:
        try:
            await client.get_chat_member(channel, user_id)
        except Exception:
            keyboard = InlineKeyboardMarkup([
                [InlineKeyboardButton(f"اضغط هنا للاشتراك بالقناة ⚡", url=f"https://t.me/{channel}")]
            ])
            text = f"**🚦عذراً عزيزي\\n🚦يجب عليك الإشتراك في القناة\\n\\n    قنـاة الـبـوت :\\n ⤹ https://t.me/{channel} ⤸ **"
            await client.send_message(chat_id=message.chat.id, text=text, reply_markup=keyboard)
            return False      
    return True

from collections import defaultdict
import time
BANNED_USERS = []
user_messages = defaultdict(list)

async def check(user_id, message, client):
    is_subscribed = await check_chat_member_status(user_id, message, client)
    if user_id in BANNED_USERS:
        await message.delete()
        await message.reply_text("**تم حظرك من البوت**")
        return False
    current_time = time.time()
    user_messages[user_id].append(current_time)
    user_messages[user_id] = [t for t in user_messages[user_id] if current_time - t <= 5]
    if len(user_messages[user_id]) > 5:
        if user_id not in DEVS:
            BANNED_USERS.append(user_id)
            await client.send_message(message.chat.id, "**🚫 لقد تم حظرك بسبب الإرسال المتكرر!**")
        return False
    if not is_subscribed:
        return False
    if off and message.from_user.id not in DEVS:
        await message.reply_text(f'**◍  الصانع معطل حاليا\\n◍ يرجى التواصل مع <a href="https://t.me/{source_devv}">مطور السورس</a>\\n√**')
        return False
    return True
    
@bot.on_message(filters.command(["سورس 🚦"], ""), group=544388)
async def alivehi(client: Client, message):
    if not await check(message.from_user.id, message, client):
        return
    user_id = message.from_user.id if message.from_user else "None"
    await message.reply_video(
        video=f"https://t.me/{channel_source}/17",
        caption=f"""
⍟ 𝚃𝙷𝙴 𝙱𝙴𝚂𝚃 𝚂𝙾𝚄𝚁𝙲𝙴 𝙾𝙽 𝚃𝙴𝙻𝙴𝙶𝚁𝙰𝙼
        """,
        reply_markup=InlineKeyboardMarkup([
            [
                InlineKeyboardButton("ᏟᎻᎪΝΝᎬᏞ", url=f"https://t.me/{channel_source}"),
                InlineKeyboardButton("ᏀᎡØႮᏢ", url=f"https://t.me/{gr}")
            ],
            [
                InlineKeyboardButton(f"{Source_name} ™ المطور", url=f"https://t.me/{source_devv}")
            ],
        ]),
    )



@bot.on_message(filters.command(["مطور السورس 🕸"], ""), group=54445448)
async def aliaashi(client: Client, message):
    if not await check(message.from_user.id, message, client):
        return
    user = await client.get_chat(chat_id=f"{sourse_dev}")
    name = user.first_name
    username = user.username
    bio = user.bio
    user_id = user.id
    photo = user.photo.big_file_id
    photo = await client.download_media(photo)
    title = message.chat.title if message.chat.title else message.chat.first_name
    caption = f"""
**Developer Name : {name} **
**Devloper Username : @{username} **
**Bio : {bio} **
**⤶ صلـي علـى النبـۍ وتـبـسم ✨♥️ ≯ -**
    """
    await message.reply_photo(
        photo=photo,
        caption=caption,
        reply_markup=InlineKeyboardMarkup([[InlineKeyboardButton(f"{name}", user_id=f"{user_id}")]])
    )
    try:
        os.remove(photo)
    except:
        pass
    

def readable_error(exc: Exception) -> str:
    mapping = {
        (ApiIdInvalid, ApiIdInvalid1, ApiIdInvalidError): "❌ **API ID/Hash** غير صحيح.",
        (PhoneNumberInvalid, PhoneNumberInvalid1, PhoneNumberInvalidError): "📞 **رقم الهاتف** غير صحيح.",
        (PhoneCodeInvalid, PhoneCodeInvalid1, PhoneCodeInvalidError): "🔢 **رمز التحقق (OTP)** غير صحيح.",
        (PhoneCodeExpired, PhoneCodeExpired1, PhoneCodeExpiredError): "⌛ **رمز التحقق (OTP)** منتهي الصلاحية.",
        (PasswordHashInvalid, PasswordHashInvalid1, PasswordHashInvalidError): "🔒 **كلمة المرور الثنائية (2Step)** غير صحيحة.",
        FloodWaitError: "🚫 تم الحظر مؤقتًا – الرجاء المحاولة لاحقًا.",
        AuthRestartError: "♻️ يتطلب إعادة التحقق. الرجاء البدء من جديد.",
    }
    for group, txt in mapping.items():
        if isinstance(exc, group):
            return txt
    return f"ᴜɴᴋɴᴏᴡɴ ᴇʀʀᴏʀ: {str(exc).replace('`', '')}"


@bot.on_message(filters.command(["تفعيل الصانع 🟢", "تعطيل الصانع 🔴"], "") & filters.private, group=4213151)
async def onoff(client, message):
  if message.from_user.id not in DEVS:
    return
  global off
  if message.text == "تفعيل الصانع 🟢":
    off = None
    return await message.reply_text("**◍ تم تفعيل الصانع بنجاح 🚦\\n√**")
  else:
    off = True
    await message.reply_text("**◍ تم تعطيل الصانع بنجاح 🚦\\n√**")


cancel_keyboard = InlineKeyboardMarkup([[InlineKeyboardButton("❌ إلغاء", callback_data="cancel_ask")]])

cancelled_users = set()

@bot.on_callback_query(filters.regex(r"^cancel_ask$"))
async def cancel_ask_handler(client, callback_query):
    user_id = callback_query.from_user.id
    cancelled_users.add(user_id)
    await callback_query.message.delete()
    await callback_query.message.reply_text("**❌ تم إلغاء العملية**")

# باقي الكود يبقى كما هو مع تحديث معرفات المطورين والقنوات...
# سأكمل في الجزء التالي

#
#==================================================
#
#███████╗███████╗██████╗  ██████╗ 
#╚══███╔╝██╔════╝██╔══██╗██╔═══██╗
#  ███╔╝ █████╗  ██████╔╝██║   ██║
# ███╔╝  ██╔══╝  ██╔══██╗██║   ██║
#███████╗███████╗██║  ██║╚██████╔╝
#╚══════╝╚══════╝╚═╝  ╚═╝ ╚═════╝ 
#
#==================================================
