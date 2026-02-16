import re

# قائمة الكلمات الممنوعة - يمكنك التعديل عليها
BANNED_WORDS = {
    'سب', 'قذف', 'حرام', 'كفر', 'زنديق',
    'stupid', 'idiot', 'fuck', 'shit', 'damn',
    'احمق', 'غبي', 'كلب', 'حمار', 'تافه',
}

def contains_banned_words(text: str) -> bool:
    """التحقق من وجود كلمات ممنوعة"""
    if not text:
        return False
    
    text_lower = text.lower()
    
    # التحقق من الكلمات الممنوعة
    for word in BANNED_WORDS:
        pattern = r'\b' + re.escape(word.lower()) + r'\b'
        if re.search(pattern, text_lower):
            return True
    
    return False

def get_warning_message(user_name: str) -> str:
    """رسالة التحذير"""
    return f"""
⚠️ **تم حذف رسالة مخالفة**

عذراً {user_name}، 
تم حذف رسالتك لاحتوائها على محتوى مخالف.

📜 **يرجى الالتزام بقوانين المجموعة**
    """
    