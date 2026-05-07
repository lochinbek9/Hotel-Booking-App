import os

assets_path = "/Users/user/Desktop/Hotel-Booking-App/src/assets/assets.js"

with open(assets_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Address Update
content = content.replace('"address": "Main Road  123 Street , 23 Colony"', '"address": "Andijon sh., Milliy tiklanish ko\'chasi, 14-uy"')

# 2. Amenities Update ("Mountain View" -> "City View")
content = content.replace('"Mountain View": assets.mountainIcon', '"City View": assets.mountainIcon')
content = content.replace('"Mountain View"', '"City View"')

# 3. Room Pricing Update
content = content.replace('"pricePerNight": 399,', '"pricePerNight": 100,')
content = content.replace('"pricePerNight": 299,', '"pricePerNight": 60,')
content = content.replace('"pricePerNight": 249,', '"pricePerNight": 50,')
content = content.replace('"pricePerNight": 199,', '"pricePerNight": 40,')

# 4. User Bookings Pricing Update
content = content.replace('"totalPrice": 299,', '"totalPrice": 60,')
content = content.replace('"totalPrice": 399,', '"totalPrice": 100,')
content = content.replace('"totalPrice": 199,', '"totalPrice": 40,')
content = content.replace('"totalRevenue": 897,', '"totalRevenue": 200,')

# 5. Exclusive Offers Update
# Offer 1
content = content.replace(
    '"title": "Summer Escape Package", "description": "Enjoy a complimentary night and daily breakfast"',
    '"title": "Business Trip Package", "description": "Free transfer and dinner for stays over 3 days"'
)
# Offer 3
content = content.replace(
    '"title": "Luxury Retreat", "description": "Book 60 days in advance and save on your stay at any of our luxury properties worldwide."',
    '"title": "Early Bird Discount", "description": "Book 60 days in advance and get 30% off."'
)

with open(assets_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated assets.js with final pricing and offers!")
