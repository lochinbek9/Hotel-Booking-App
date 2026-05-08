import os
import re

i18n_path = "/Users/user/Desktop/Hotel-Booking-App/src/i18n.js"

with open(i18n_path, "r", encoding="utf-8") as f:
    content = f.read()

# Update "Hotels" translations
content = content.replace('"Hotels": "Mehmonxonalar"', '"Hotels": "Xonalarimiz"')
content = content.replace('"Hotels": "Mehmoxonalar"', '"Hotels": "Xonalarimiz"') # Just in case it was misspelled
content = content.replace('"Hotels": "Отели"', '"Hotels": "Наши номера"')
content = content.replace('"Hotels": "Hotels"', '"Hotels": "Our Rooms"')

uz_entries = """
      "Room Type": "Xona turi",
      "All Rooms": "Barcha xonalar",
      "Standard Room": "Standart xona",
      "Deluxe Room": "Deluks xona",
      "Luxury Suite": "Lyuks xona"
"""

ru_entries = """
      "Room Type": "Тип номера",
      "All Rooms": "Все номера",
      "Standard Room": "Стандартный номер",
      "Deluxe Room": "Номер Делюкс",
      "Luxury Suite": "Люкс номер"
"""

en_entries = """
      "Room Type": "Room Type",
      "All Rooms": "All Rooms",
      "Standard Room": "Standard Room",
      "Deluxe Room": "Deluxe Room",
      "Luxury Suite": "Luxury Suite"
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

print("Updated i18n.js with Room translations!")
