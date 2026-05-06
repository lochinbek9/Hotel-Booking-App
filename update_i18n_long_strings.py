import re
import os

i18n_path = "/Users/user/Desktop/Hotel-Booking-App/src/i18n.js"

with open(i18n_path, "r", encoding="utf-8") as f:
    content = f.read()

uz_entries = """
      "Footer Description": "Boutique mehmonxonalaridan tortib, hashamatli villalar va xususiy orollargacha bo'lgan dunyoning eng g'aroyib turar joylarini kashf eting.",
      "Room Details Text": "Mehmonlar mavjudlikka qarab birinchi qavatga joylashtiriladi. Siz chinakam shahar shukuhiga ega bo'lgan shinam ikki xonali kvartiraga ega bo'lasiz. Ko'rsatilgan narx ikki kishi uchun, guruhlar uchun aniq narxni bilish uchun mehmonlar sonini belgilang.",
      "What Our Guests Say": "Mehmonlarimiz nima deydi",
      "Testimonials Subtitle": "Nima uchun talabchan sayohatchilar butun dunyo bo'ylab eksklyuziv va hashamatli turar joylari uchun doimiy ravishda Mirzo hotelni tanlashini bilib oling.",
      "My Bookings Subtitle": "O'tmishdagi, joriy va kelajakdagi mehmonxona bandlovlarini bir joyda osongina boshqaring. Sayohatlaringizni bir necha tugmani bosish orqali rejalashtiring."
"""

ru_entries = """
      "Footer Description": "Откройте для себя самые необычные места для проживания в мире: от бутик-отелей до роскошных вилл и частных островов.",
      "Room Details Text": "Гости будут размещены на первом этаже при наличии свободных мест. Вы получите комфортабельную квартиру с двумя спальнями и настоящей городской атмосферой. Указанная цена действительна для двух гостей, для групп, пожалуйста, укажите количество гостей, чтобы узнать точную цену.",
      "What Our Guests Say": "Что говорят наши гости",
      "Testimonials Subtitle": "Узнайте, почему взыскательные путешественники неизменно выбирают отель Mirzo для эксклюзивного и роскошного проживания по всему миру.",
      "My Bookings Subtitle": "Легко управляйте своими прошлыми, текущими и предстоящими бронированиями отелей в одном месте. Планируйте свои поездки без проблем всего в несколько кликов."
"""

en_entries = """
      "Footer Description": "Discover the world's most extraordinary places to stay, from boutique hotels to luxury villas and private islands.",
      "Room Details Text": "Guests will be allocated on the ground floor according to availability. You get a comfortable Two bedroom apartment has a true city feeling. The price quoted is for two guest, at the guest slot please mark the number of guests to get the exact price for groups. The Guests will be allocated ground floor according to availability. You get the comfortable two bedroom apartment that has a true city feeling.",
      "What Our Guests Say": "What Our Guests Say",
      "Testimonials Subtitle": "Discover why discerning travelers consistently choose Mirzo hotel for their exclusive and luxurious accommodations around the world.",
      "My Bookings Subtitle": "Easily manage your past, current, and upcoming hotel reservations in one place. Plan your trips seamlessly with just a few clicks"
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

print("Updated i18n.js with long strings and subtitles!")
