#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🤖 TESST Bot - Zombie Module
👨‍💻 المطور: رعد
📱 المعرف: JX_F9
🆔 الآيدي: 7788181885
📢 قناة السورس: RA3D_OFFICEL
👥 جروب السورس: KOJLM
🎨 التصميم: ᏚᎾᏌᎡᏟᎬ RA3D
"""

import asyncio
import json
import os
from pyrogram import Client, filters
from pyrogram.types import Message
from datetime import datetime

# تحميل إعدادات التكوين
with open('config.json', 'r', encoding='utf-8') as file:
    config = json.load(file)

class ZombieBot:
    """فئة البوت الرئيسية"""
    
    def __init__(self):
        self.version = "2.0"
        self.developer = "رعد"
        self.developer_id = 7788181885
        self.developer_username = "JX_F9"
        self.source_channel = "RA3D_OFFICEL"
        self.support_group = "KOJLM"
        self.bot_name = config.get('BOT_NAME', 'رعد بوت')
        
    def get_info(self):
        """إرجاع معلومات البوت"""
        return {
            "name": self.bot_name,
            "version": self.version,
            "developer": self.developer,
            "developer_id": self.developer_id,
            "developer_username": self.developer_username,
            "source_channel": self.source_channel,
            "support_group": self.support_group,
            "created_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    
    def is_developer(self, user_id: int) -> bool:
        """فحص إذا كان المستخدم مطور"""
        return user_id == self.developer_id
    
    def get_welcome_message(self, user_name: str) -> str:
        """رسالة الترحيب"""
        return f"""
🎉 أهلاً وسهلاً {user_name}!

🤖 مرحباً بك في {self.bot_name}
⚡ بوت متطور ومتعدد الاستخدامات

📢 قناة السورس: @{self.source_channel}
👥 جروب الدعم: @{self.support_group}
👨‍💻 المطور: {self.developer} (@{self.developer_username})

🔥 الإصدار: {self.version}
✨ تم التطوير بواسطة {config.get('Source_design', 'ᏚᎾᏌᎡᏟᎬ RA3D')}
"""

# إنشاء كائن البوت
zombie_bot = ZombieBot()

# تصدير المعلومات المهمة
__all__ = ['zombie_bot', 'ZombieBot']

if __name__ == "__main__":
    print("🤖 TESST Bot - Zombie Module")
    print(f"👨‍💻 المطور: {zombie_bot.developer}")
    print(f"📱 المعرف: @{zombie_bot.developer_username}")
    print(f"🆔 الآيدي: {zombie_bot.developer_id}")
    print(f"📢 قناة السورس: @{zombie_bot.source_channel}")
    print(f"👥 جروب السورس: @{zombie_bot.support_group}")
    print("✅ تم تحميل الوحدة بنجاح")
