#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
🤖 TESST Bot - ملف التشغيل الرئيسي لـ Replit
👨‍💻 المطور: رعد (@JX_F9)
🆔 الآيدي: 7788181885
📢 قناة السورس: @RA3D_OFFICEL
👥 جروب السورس: @KOJLM
"""

import os
import sys
import asyncio
from pathlib import Path

# إضافة المجلد الحالي لمسار Python
current_dir = Path(__file__).parent
sys.path.insert(0, str(current_dir))

def check_environment():
    """فحص المتغيرات البيئية المطلوبة"""
    required_vars = ['API_ID', 'API_HASH', 'BOT_TOKEN']
    missing_vars = []
    
    for var in required_vars:
        if not os.getenv(var):
            missing_vars.append(var)
    
    if missing_vars:
        print("❌ المتغيرات البيئية التالية مفقودة:")
        for var in missing_vars:
            print(f"   - {var}")
        print("\n💡 تأكد من إضافة هذه المتغيرات في ملف .env أو في إعدادات Replit")
        return False
    
    return True

def main():
    """الدالة الرئيسية"""
    print("🤖 TESST Bot - بدء التشغيل...")
    print("👨‍💻 المطور: رعد (@JX_F9)")
    print("📢 قناة السورس: @RA3D_OFFICEL")
    print("👥 جروب الدعم: @KOJLM")
    print("-" * 50)
    
    # فحص المتغيرات البيئية
    if not check_environment():
        sys.exit(1)
    
    # استيراد وتشغيل البوت
    try:
        from main import *
        print("✅ تم تشغيل البوت بنجاح!")
    except ImportError as e:
        print(f"❌ خطأ في استيراد الوحدات: {e}")
        sys.exit(1)
    except Exception as e:
        print(f"❌ خطأ في تشغيل البوت: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
