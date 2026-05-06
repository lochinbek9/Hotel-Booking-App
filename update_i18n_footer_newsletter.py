import re
import os

i18n_path = "/Users/user/Desktop/Hotel-Booking-App/src/i18n.js"

with open(i18n_path, "r", encoding="utf-8") as f:
    content = f.read()

uz_entries = """
      "COMPANY": "KOMPANIYA",
      "Careers": "Karyera",
      "Press": "Matbuot",
      "Blog": "Blog",
      "Partners": "Hamkorlar",
      "SUPPORT": "QO'LLAB-QUVVATLASH",
      "Help Center": "Yordam Markazi",
      "Safety Information": "Xavfsizlik Ma'lumotlari",
      "Cancellation Options": "Bekor Qilish Variantlari",
      "Contact Us": "Biz Bilan Bog'lanish",
      "Accessibility": "Foydalanish Imkoniyati",
      "STAY UPDATED": "XABARDOR BO'LING",
      "Footer Subscribe": "Ilhom va maxsus takliflar uchun yangiliklarimizga obuna bo'ling.",
      "Your email": "Sizning elektron pochtangiz",
      "All rights reserved.": "Barcha huquqlar himoyalangan.",
      "Privacy": "Maxfiylik",
      "Terms": "Shartlar",
      "Sitemap": "Sayt xaritasi",
      "Stay Inspired": "Ilhomlanib qoling",
      "Stay Inspired Subtitle": "Bizning xabarnomamizga qo'shiling va birinchilardan bo'lib yangi manzillar, eksklyuziv takliflar va sayohat ilhomini kashf eting.",
      "Enter your email": "Elektron pochtangizni kiriting",
      "Privacy Consent": "Obuna bo'lish orqali siz bizning Maxfiylik Siyosatimizga rozilik bildirasiz va yangiliklarni qabul qilishga rozi bo'lasiz."
"""

ru_entries = """
      "COMPANY": "КОМПАНИЯ",
      "Careers": "Карьера",
      "Press": "Пресса",
      "Blog": "Блог",
      "Partners": "Партнеры",
      "SUPPORT": "ПОДДЕРЖКА",
      "Help Center": "Справочный Центр",
      "Safety Information": "Информация о Безопасности",
      "Cancellation Options": "Варианты Отмены",
      "Contact Us": "Связаться с Нами",
      "Accessibility": "Доступность",
      "STAY UPDATED": "БУДЬТЕ В КУРСЕ",
      "Footer Subscribe": "Подпишитесь на нашу рассылку для получения вдохновения и специальных предложений.",
      "Your email": "Ваш email",
      "All rights reserved.": "Все права защищены.",
      "Privacy": "Конфиденциальность",
      "Terms": "Условия",
      "Sitemap": "Карта сайта",
      "Stay Inspired": "Вдохновляйтесь",
      "Stay Inspired Subtitle": "Присоединяйтесь к нашей рассылке и первыми узнавайте о новых направлениях, эксклюзивных предложениях и вдохновении для путешествий.",
      "Enter your email": "Введите ваш email",
      "Privacy Consent": "Подписываясь, вы соглашаетесь с нашей Политикой конфиденциальности и даете согласие на получение обновлений."
"""

en_entries = """
      "COMPANY": "COMPANY",
      "Careers": "Careers",
      "Press": "Press",
      "Blog": "Blog",
      "Partners": "Partners",
      "SUPPORT": "SUPPORT",
      "Help Center": "Help Center",
      "Safety Information": "Safety Information",
      "Cancellation Options": "Cancellation Options",
      "Contact Us": "Contact Us",
      "Accessibility": "Accessibility",
      "STAY UPDATED": "STAY UPDATED",
      "Footer Subscribe": "Subscribe to our newsletter for inspiration and special offers.",
      "Your email": "Your email",
      "All rights reserved.": "All rights reserved.",
      "Privacy": "Privacy",
      "Terms": "Terms",
      "Sitemap": "Sitemap",
      "Stay Inspired": "Stay Inspired",
      "Stay Inspired Subtitle": "Join our newsletter and be the first to discover new destinations, exclusive offers, and travel inspiration.",
      "Enter your email": "Enter your email",
      "Privacy Consent": "By subscribing, you agree to our Privacy Policy and consent to receive updates."
"""

def add_entries(text, lang_id, new_entries):
    pattern = rf"({lang_id}:\s*\{{\s*translation:\s*{{)([\s\S]*?)(\s*}}\s*}})"
    match = re.search(pattern, text)
    if match:
        existing = match.group(2)
        if not existing.strip().endswith(","):
            existing += ","
        replacement = match.group(1) + existing + new_entries + match.group(3)
        return text[:match.start()] + replacement + text[match.end():]
    return text

content = add_entries(content, "uz", uz_entries)
content = add_entries(content, "ru", ru_entries)
content = add_entries(content, "en", en_entries)

with open(i18n_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated i18n.js with Footer and Newsletter strings!")
