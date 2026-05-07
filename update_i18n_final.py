import re
import os

i18n_path = "/Users/user/Desktop/Hotel-Booking-App/src/i18n.js"

with open(i18n_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Hero Subtitle Update (Replacing existing ones)
content = content.replace(
    '"Andijon shahridagi eng yaxshi mehmonxonada unutilmas va qulay dam oling. Xonangizni bugunoq band qiling."',
    '"Andijon markazida, Bobur maydonidan 5 daqiqalik yo\'lda joylashgan shinam mehmonxona. Biznes va oilaviy sayohatlar uchun ideal tanlov."'
)
content = content.replace(
    '"Насладитесь незабываемым и комфортным отдыхом в лучшем отеле Андижана. Забронируйте номер уже сегодня."',
    '"Уютный отель в центре Андижана, в 5 минутах от площади Бабура. Идеальный выбор для деловых и семейных поездок."'
)
content = content.replace(
    '"Enjoy an unforgettable and comfortable stay at the best hotel in Andijan. Book your room today."',
    '"A cozy hotel in the center of Andijan, a 5-minute walk from Babur Square. The perfect choice for business and family trips."'
)

# 2. Add New Translations for Address, Amenities, and Offers
uz_entries = """
      "Andijon sh., Milliy tiklanish ko'chasi, 14-uy": "Andijon sh., Milliy tiklanish ko'chasi, 14-uy",
      "Room Service": "24/7 xizmat",
      "City View": "Shahar manzarasi",
      "Business Trip Package": "Biznes sayohat paketi",
      "Free transfer and dinner for stays over 3 days": "3 kundan ko'p qolganlarga bepul transfer va kechki ovqat",
      "Early Bird Discount": "Erta band qilish chegirmasi",
      "Book 60 days in advance and get 30% off.": "60 kun oldin band qiling va 30% chegirmaga ega bo'ling.",
      "Open in Google Maps": "Google Maps'da ochish"
"""

ru_entries = """
      "Andijon sh., Milliy tiklanish ko'chasi, 14-uy": "г. Андижан, ул. Миллий тикланиш, дом 14",
      "Room Service": "Круглосуточное обслуживание 24/7",
      "City View": "Вид на город",
      "Business Trip Package": "Пакет для бизнес-поездок",
      "Free transfer and dinner for stays over 3 days": "Бесплатный трансфер и ужин при проживании более 3 дней",
      "Early Bird Discount": "Скидка за раннее бронирование",
      "Book 60 days in advance and get 30% off.": "Забронируйте за 60 дней и получите скидку 30%.",
      "Open in Google Maps": "Открыть в Google Maps"
"""

en_entries = """
      "Andijon sh., Milliy tiklanish ko'chasi, 14-uy": "14 Milliy Tiklanish Street, Andijan city",
      "Room Service": "24/7 Room Service",
      "City View": "City View",
      "Business Trip Package": "Business Trip Package",
      "Free transfer and dinner for stays over 3 days": "Free transfer and dinner for stays over 3 days",
      "Early Bird Discount": "Early Bird Discount",
      "Book 60 days in advance and get 30% off.": "Book 60 days in advance and get 30% off.",
      "Open in Google Maps": "Open in Google Maps"
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

print("Updated i18n.js with final copywriting!")
