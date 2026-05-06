import re
import os

components = {
    "src/components/ExlusiveOffers.jsx": [
        (r"\{item\.title\}", "{t(item.title)}"),
        (r"\{item\.description\}", "{t(item.description)}")
    ],
    "src/components/Testimonial.jsx": [
        (r"\{testimonial\.address\}", "{t(testimonial.address)}"),
        (r"\"\{testimonial\.review\}\"", "\"{t(testimonial.review)}\"")
    ],
    "src/components/HotelCard.jsx": [
        (r"\{room\.hotel\.name\}", "{t(room.hotel.name)}"),
        (r"\{room\.hotel\.address\}", "{t(room.hotel.address)}")
    ],
    "src/pages/AllRooms.jsx": [
        (r"label=\{room\}", "label={t(room)}"),
        (r"label=\{option\}", "label={t(option)}"),
        (r"label=\{`\$\s*\{range\}`\}", "label={`$ ${t(range)}`}"),
        (r"\{room\.hotel\.city\}", "{t(room.hotel.city)}"),
        (r"\{room\.hotel\.name\}", "{t(room.hotel.name)}"),
        (r"\{room\.hotel\.address\}", "{t(room.hotel.address)}"),
        (r"<p className=\"text-xs\">\{item\}</p>", "<p className=\"text-xs\">{t(item)}</p>")
    ],
    "src/pages/RoomDetails.jsx": [
        (r"\{room\.hotel\.name\}", "{t(room.hotel.name)}"),
        (r"\{room\.roomType\}", "{t(room.roomType)}"),
        (r"\{room\.hotel\.address\}", "{t(room.hotel.address)}"),
        (r"<p className=\"text-xs\">\{item\}</p>", "<p className=\"text-xs\">{t(item)}</p>"),
        (r"\{spec\.title\}", "{t(spec.title)}"),
        (r"\{spec\.description\}", "{t(spec.description)}")
    ],
    "src/pages/Dashboard.jsx": [
        (r"\{item\.room\.roomType\}", "{t(item.room.roomType)}")
    ],
    "src/pages/MyBookings.jsx": [
        (r"\{booking\.hotel\.name\}", "{t(booking.hotel.name)}"),
        (r"\{booking\.room\.roomType\}", "{t(booking.room.roomType)}"),
        (r"\{booking\.hotel\.address\}", "{t(booking.hotel.address)}")
    ],
    "src/pages/ListRoom.jsx": [
        (r"\{item\.roomType\}", "{t(item.roomType)}"),
        (r"\{item\.amenities\.join\(\", \"\)\}", "{item.amenities.map(a => t(a)).join(\", \")}")
    ]
}

base_path = "/Users/user/Desktop/Hotel-Booking-App/"

for file_path, replacements in components.items():
    full_path = os.path.join(base_path, file_path)
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
        
    for old, new in replacements:
        content = re.sub(old, new, content)
        
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
        
print("Successfully applied t() to dynamic values!")
