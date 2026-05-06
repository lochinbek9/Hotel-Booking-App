import re
import os

i18n_path = "/Users/user/Desktop/Hotel-Booking-App/src/i18n.js"

with open(i18n_path, "r", encoding="utf-8") as f:
    content = f.read()

uz_entries = """
      "View All Offers": "Barcha takliflarni ko'rish",
      "OFF": "chegirma",
      "Expires": "Amal qilish muddati:",
      "View Offers": "Takliflarni ko'rish",
      "Best Seller": "Top sotuv",
      "/night": "/kecha",
      "View All Destinations": "Barcha manzillarni ko'rish",
      "FILTERS": "FILTRLAR",
      "HIDE": "YASHIRISH",
      "SHOW": "KO'RSATISH",
      "CLEAR": "TOZALASH",
      "Sort By": "Saralash:",
      "reviews": "sharhlar",
      "Experience Luxury Like Never Before": "Mislsiz hashamatni his eting",
      "Check Availability": "Mavjudligini tekshirish",
      "Contact Now": "Hozir bog'lanish",
      "User Name": "Foydalanuvchi ismi",
      "Room Name": "Xona nomi",
      "Total Price": "Umumiy narx",
      "Payment Status": "To'lov holati",
      "Completed": "Tugallangan",
      "Pending": "Kutilmoqda",
      "Name": "Nomi",
      "Facility": "Qulayliklar",
      "Price / Night": "Narx / Kecha",
      "Actions": "Amallar",
      "Date & Timings": "Sana va vaqt",
      "Payment": "To'lov"
"""

ru_entries = """
      "View All Offers": "Посмотреть все предложения",
      "OFF": "скидка",
      "Expires": "Истекает:",
      "View Offers": "Посмотреть предложения",
      "Best Seller": "Хит продаж",
      "/night": "/ночь",
      "View All Destinations": "Посмотреть все направления",
      "FILTERS": "ФИЛЬТРЫ",
      "HIDE": "СКРЫТЬ",
      "SHOW": "ПОКАЗАТЬ",
      "CLEAR": "ОЧИСТИТЬ",
      "Sort By": "Сортировать по:",
      "reviews": "отзывы",
      "Experience Luxury Like Never Before": "Ощутите роскошь как никогда раньше",
      "Check Availability": "Проверить наличие",
      "Contact Now": "Связаться сейчас",
      "User Name": "Имя пользователя",
      "Room Name": "Название номера",
      "Total Price": "Общая цена",
      "Payment Status": "Статус оплаты",
      "Completed": "Завершено",
      "Pending": "В ожидании",
      "Name": "Название",
      "Facility": "Удобства",
      "Price / Night": "Цена / Ночь",
      "Actions": "Действия",
      "Date & Timings": "Дата и время",
      "Payment": "Оплата"
"""

en_entries = """
      "View All Offers": "View All Offers",
      "OFF": "OFF",
      "Expires": "Expires",
      "View Offers": "View Offers",
      "Best Seller": "Best Seller",
      "/night": "/night",
      "View All Destinations": "View All Destinations",
      "FILTERS": "FILTERS",
      "HIDE": "HIDE",
      "SHOW": "SHOW",
      "CLEAR": "CLEAR",
      "Sort By": "Sort By",
      "reviews": "reviews",
      "Experience Luxury Like Never Before": "Experience Luxury Like Never Before",
      "Check Availability": "Check Availability",
      "Contact Now": "Contact Now",
      "User Name": "User Name",
      "Room Name": "Room Name",
      "Total Price": "Total Price",
      "Payment Status": "Payment Status",
      "Completed": "Completed",
      "Pending": "Pending",
      "Name": "Name",
      "Facility": "Facility",
      "Price / Night": "Price / Night",
      "Actions": "Actions",
      "Date & Timings": "Date & Timings",
      "Payment": "Payment"
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

print("Updated i18n.js with missing UI strings!")
