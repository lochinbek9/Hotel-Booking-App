import os

i18n_path = "/Users/user/Desktop/Hotel-Booking-App/src/i18n.js"

with open(i18n_path, "r", encoding="utf-8") as f:
    content = f.read()

# UZ updates
content = content.replace('"Hero Title": "Mukammal Sayohat Manzilingizni Kashf Eting"', '"Hero Title": "Andijon markazidagi shinam va zamonaviy hordiq"')
content = content.replace('"Dunyodagi eng eksklyuziv mehmonxona va kurortlarda mislsiz hashamat va qulaylik sizni kutmoqda. Sayohatni bugunoq boshlang."', '"Andijon shahridagi eng yaxshi mehmonxonada unutilmas va qulay dam oling. Xonangizni bugunoq band qiling."')
content = content.replace('"Best Seller": "Top sotuv"', '"Best Seller": "Eng ko\'p band qilingan"')

# RU updates
content = content.replace('"Hero Title": "Откройте Для Себя Идеальное Место Для Отдыха"', '"Hero Title": "Уютный и современный отдых в центре Андижана"')
content = content.replace('"Непревзойденная роскошь и комфорт ждут вас в самых эксклюзивных отелях и курортах мира. Начните свое путешествие сегодня."', '"Насладитесь незабываемым и комфортным отдыхом в лучшем отеле Андижана. Забронируйте номер уже сегодня."')
content = content.replace('"Best Seller": "Хит продаж"', '"Best Seller": "Самые бронируемые"')

# EN updates
content = content.replace('"Hero Title": "Discover Your Perfect Getaway Destination"', '"Hero Title": "Cozy and modern retreat in the heart of Andijan"')
content = content.replace('"Unparalleled luxury and comfort await at the world\'s most exclusive hotels and resorts. Start your journey today."', '"Enjoy an unforgettable and comfortable stay at the best hotel in Andijan. Book your room today."')
content = content.replace('"Best Seller": "Best Seller"', '"Best Seller": "Most Booked"')

with open(i18n_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated i18n.js with localized sales copy!")
