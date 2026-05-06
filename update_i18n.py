import re
import os

i18n_path = "/Users/user/Desktop/Hotel-Booking-App/src/i18n.js"

with open(i18n_path, "r", encoding="utf-8") as f:
    content = f.read()

uz_entries = """
      "Dubai": "Dubay",
      "Singapore": "Singapur",
      "New York": "Nyu-York",
      "London": "London",
      "Summer Escape Package": "Yozgi ta'til paketi",
      "Enjoy a complimentary night and daily breakfast": "Bepul tun va kundalik nonushtadan bahramand bo'ling",
      "Romantic Getaway": "Romantik dam olish",
      "Special couples package including spa treatment": "Spa muolajasini o'z ichiga olgan maxsus juftliklar paketi",
      "Luxury Retreat": "Hashamatli dam olish",
      "Book 60 days in advance and save on your stay at any of our luxury properties worldwide.": "60 kun oldin band qiling va dunyo bo'ylab istalgan hashamatli ob'ektlarimizda tejang.",
      "I've used many booking platforms before, but none compare to the personalized experience and attention to detail that Mirzo hotel provides.": "Men oldin ko'plab band qilish platformalaridan foydalanganman, lekin hech biri Mirzo hotel taqdim etadigan shaxsiy tajriba va detallarga e'tibor bilan tenglasha olmaydi.",
      "Mirzo hotel exceeded my expectations. The booking process was seamless, and the hotels were absolutely top-notch. Highly recommended!": "Mirzo hotel kutganimdan a'lo darajada chiqdi. Band qilish jarayoni silliq o'tdi va mehmonxonalar mutlaqo yuqori darajada edi. Qat'iy tavsiya qilaman!",
      "Amazing service! I always find the best luxury accommodations through Mirzo hotel. Their recommendations never disappoint!": "Ajoyib xizmat! Men doimo Mirzo hotel orqali eng yaxshi hashamatli turar joylarni topaman. Ularning tavsiyalari hech qachon ko'ngilni qoldirmaydi!",
      "Barcelona, Spain": "Barselona, Ispaniya",
      "New York, USA": "Nyu-York, AQSh",
      "Seoul, South Korea": "Seul, Janubiy Koreya",
      "Free WiFi": "Bepul WiFi",
      "Free Breakfast": "Bepul Nonushta",
      "Room Service": "Xizmat ko'rsatish",
      "Mountain View": "Tog' manzarasi",
      "Pool Access": "Hovuz",
      "Single Bed": "1 kishilik karavot",
      "Double Bed": "2 kishilik karavot",
      "Single Bad": "1 kishilik karavot",
      "Double Bad": "2 kishilik karavot",
      "Luxury Bed": "Lyuks karavot",
      "Luxury Bad": "Lyuks karavot",
      "Family Bed": "Oila karavoti",
      "Family Bad": "Oila karavoti",
      "Family Suite": "Oilaviy xona",
      "Clean & Safe Stay": "Toza va Xavfsiz joy",
      "A well-maintained and hygienic space just for you.": "Siz uchun maxsus parvarishlangan va gigiyenik makon.",
      "Enhanced Cleaning": "Kuchaytirilgan Tozalash",
      "This host follows Staybnb's strict cleaning standards.": "Bu mezbon tozalik bo'yicha qat'iy standartlarga amal qiladi.",
      "Excellent Location": "Ajoyib Joylashuv",
      "90% of guests rated the location 5 stars.": "Mehmonlarning 90% joylashuvni 5 yulduz bilan baholadi.",
      "Smooth Check-In": "Muammosiz Joylashish",
      "100% of guests gave check-in a 5-star rating.": "Mehmonlarning 100% joylashishga 5 yulduzli baho berdi.",
      "Urbanza Suites": "Urbanza Suites",
      "Main Road  123 Street , 23 Colony": "Main yo'li 123-ko'cha, 23-daha"
"""

ru_entries = """
      "Dubai": "Дубай",
      "Singapore": "Сингапур",
      "New York": "Нью-Йорк",
      "London": "Лондон",
      "Summer Escape Package": "Летний пакет",
      "Enjoy a complimentary night and daily breakfast": "Наслаждайтесь бесплатной ночью и ежедневным завтраком",
      "Romantic Getaway": "Романтический отдых",
      "Special couples package including spa treatment": "Специальный пакет для пар, включая спа-процедуры",
      "Luxury Retreat": "Роскошный отдых",
      "Book 60 days in advance and save on your stay at any of our luxury properties worldwide.": "Бронируйте за 60 дней и экономьте на проживании в любом из наших роскошных отелей по всему миру.",
      "I've used many booking platforms before, but none compare to the personalized experience and attention to detail that Mirzo hotel provides.": "Я использовал много платформ для бронирования, но ни одна не сравнится с индивидуальным подходом и вниманием к деталям, которые предоставляет отель Mirzo.",
      "Mirzo hotel exceeded my expectations. The booking process was seamless, and the hotels were absolutely top-notch. Highly recommended!": "Отель Mirzo превзошел мои ожидания. Процесс бронирования прошел гладко, а отели были просто превосходны. Настоятельно рекомендую!",
      "Amazing service! I always find the best luxury accommodations through Mirzo hotel. Their recommendations never disappoint!": "Потрясающий сервис! Я всегда нахожу лучшие роскошные номера через отель Mirzo. Их рекомендации никогда не разочаровывают!",
      "Barcelona, Spain": "Барселона, Испания",
      "New York, USA": "Нью-Йорк, США",
      "Seoul, South Korea": "Сеул, Южная Корея",
      "Free WiFi": "Бесплатный WiFi",
      "Free Breakfast": "Бесплатный Завтрак",
      "Room Service": "Обслуживание номеров",
      "Mountain View": "Вид на горы",
      "Pool Access": "Бассейн",
      "Single Bed": "1-спальная кровать",
      "Double Bed": "2-спальная кровать",
      "Single Bad": "1-спальная кровать",
      "Double Bad": "2-спальная кровать",
      "Luxury Bed": "Роскошная кровать",
      "Luxury Bad": "Роскошная кровать",
      "Family Bed": "Семейная кровать",
      "Family Bad": "Семейная кровать",
      "Family Suite": "Семейный люкс",
      "Clean & Safe Stay": "Чистое и Безопасное Место",
      "A well-maintained and hygienic space just for you.": "Ухоженное и гигиеничное пространство только для вас.",
      "Enhanced Cleaning": "Усиленная Уборка",
      "This host follows Staybnb's strict cleaning standards.": "Этот хозяин следует строгим стандартам чистоты.",
      "Excellent Location": "Отличное Расположение",
      "90% of guests rated the location 5 stars.": "90% гостей оценили расположение на 5 звезд.",
      "Smooth Check-In": "Гладкий Заезд",
      "100% of guests gave check-in a 5-star rating.": "100% гостей оценили заезд на 5 звезд.",
      "Urbanza Suites": "Урбанза Сьютс",
      "Main Road  123 Street , 23 Colony": "Главная дорога, улица 123, 23 колония"
"""

en_entries = """
      "Dubai": "Dubai",
      "Singapore": "Singapore",
      "New York": "New York",
      "London": "London",
      "Summer Escape Package": "Summer Escape Package",
      "Enjoy a complimentary night and daily breakfast": "Enjoy a complimentary night and daily breakfast",
      "Romantic Getaway": "Romantic Getaway",
      "Special couples package including spa treatment": "Special couples package including spa treatment",
      "Luxury Retreat": "Luxury Retreat",
      "Book 60 days in advance and save on your stay at any of our luxury properties worldwide.": "Book 60 days in advance and save on your stay at any of our luxury properties worldwide.",
      "I've used many booking platforms before, but none compare to the personalized experience and attention to detail that Mirzo hotel provides.": "I've used many booking platforms before, but none compare to the personalized experience and attention to detail that Mirzo hotel provides.",
      "Mirzo hotel exceeded my expectations. The booking process was seamless, and the hotels were absolutely top-notch. Highly recommended!": "Mirzo hotel exceeded my expectations. The booking process was seamless, and the hotels were absolutely top-notch. Highly recommended!",
      "Amazing service! I always find the best luxury accommodations through Mirzo hotel. Their recommendations never disappoint!": "Amazing service! I always find the best luxury accommodations through Mirzo hotel. Their recommendations never disappoint!",
      "Barcelona, Spain": "Barcelona, Spain",
      "New York, USA": "New York, USA",
      "Seoul, South Korea": "Seoul, South Korea",
      "Free WiFi": "Free WiFi",
      "Free Breakfast": "Free Breakfast",
      "Room Service": "Room Service",
      "Mountain View": "Mountain View",
      "Pool Access": "Pool Access",
      "Single Bed": "Single Bed",
      "Double Bed": "Double Bed",
      "Single Bad": "Single Bed",
      "Double Bad": "Double Bed",
      "Luxury Bed": "Luxury Bed",
      "Luxury Bad": "Luxury Bed",
      "Family Bed": "Family Bed",
      "Family Bad": "Family Bed",
      "Family Suite": "Family Suite",
      "Clean & Safe Stay": "Clean & Safe Stay",
      "A well-maintained and hygienic space just for you.": "A well-maintained and hygienic space just for you.",
      "Enhanced Cleaning": "Enhanced Cleaning",
      "This host follows Staybnb's strict cleaning standards.": "This host follows Staybnb's strict cleaning standards.",
      "Excellent Location": "Excellent Location",
      "90% of guests rated the location 5 stars.": "90% of guests rated the location 5 stars.",
      "Smooth Check-In": "Smooth Check-In",
      "100% of guests gave check-in a 5-star rating.": "100% of guests gave check-in a 5-star rating.",
      "Urbanza Suites": "Urbanza Suites",
      "Main Road  123 Street , 23 Colony": "Main Road  123 Street , 23 Colony"
"""

def add_entries(text, lang_id, new_entries):
    # Find the end of the dictionary for lang_id
    pattern = rf"({lang_id}:\s*\{{\s*translation:\s*{{)([\s\S]*?)(\s*}}\s*}})"
    match = re.search(pattern, text)
    if match:
        existing = match.group(2)
        # Add comma if needed
        if not existing.strip().endswith(","):
            existing += ","
        # Insert new entries
        replacement = match.group(1) + existing + new_entries + match.group(3)
        return text[:match.start()] + replacement + text[match.end():]
    return text

content = add_entries(content, "uz", uz_entries)
content = add_entries(content, "ru", ru_entries)
content = add_entries(content, "en", en_entries)

with open(i18n_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated i18n.js with dynamic translations!")
