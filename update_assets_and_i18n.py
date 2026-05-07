import os
import re

assets_path = "/Users/user/Desktop/Hotel-Booking-App/src/assets/assets.js"
i18n_path = "/Users/user/Desktop/Hotel-Booking-App/src/i18n.js"

with open(assets_path, "r", encoding="utf-8") as f:
    content = f.read()

# Testimonial updates
content = content.replace('"Emma Rodriguez"', '"Malika Karimovna"')
content = content.replace('"Barcelona, Spain"', '"Toshkent, O\'zbekiston"')

content = content.replace('"Liam Johnson"', '"Dilshod To\'rayev"')
content = content.replace('"New York, USA"', '"Farg\'ona, O\'zbekiston"')

content = content.replace('"Sophia Lee"', '"Azizbek Rahimov"')
content = content.replace('"Seoul, South Korea"', '"Samarqand, O\'zbekiston"')

# Room Type updates
# First Double Bed
content = content.replace('"roomType": "Double Bed"', '"roomType": "Deluxe Room"', 1)
# Second Double Bed
content = content.replace('"roomType": "Double Bed"', '"roomType": "Luxury Suite"', 1)
# Third Double Bed
content = content.replace('"roomType": "Double Bed"', '"roomType": "Standard Room"', 1)

with open(assets_path, "w", encoding="utf-8") as f:
    f.write(content)

with open(i18n_path, "r", encoding="utf-8") as f:
    i18n_content = f.read()

uz_entries = """
      "Toshkent, O'zbekiston": "Toshkent, O'zbekiston",
      "Farg'ona, O'zbekiston": "Farg'ona, O'zbekiston",
      "Samarqand, O'zbekiston": "Samarqand, O'zbekiston",
      "Standard Room": "Standart xona",
      "Deluxe Room": "Deluks xona",
      "Luxury Suite": "Lyuks xona"
"""

ru_entries = """
      "Toshkent, O'zbekiston": "Ташкент, Узбекистан",
      "Farg'ona, O'zbekiston": "Фергана, Узбекистан",
      "Samarqand, O'zbekiston": "Самарканд, Узбекистан",
      "Standard Room": "Стандартный номер",
      "Deluxe Room": "Номер Делюкс",
      "Luxury Suite": "Люкс номер"
"""

en_entries = """
      "Toshkent, O'zbekiston": "Tashkent, Uzbekistan",
      "Farg'ona, O'zbekiston": "Fergana, Uzbekistan",
      "Samarqand, O'zbekiston": "Samarkand, Uzbekistan",
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

i18n_content = add_entries(i18n_content, "uz", uz_entries)
i18n_content = add_entries(i18n_content, "ru", ru_entries)
i18n_content = add_entries(i18n_content, "en", en_entries)

with open(i18n_path, "w", encoding="utf-8") as f:
    f.write(i18n_content)

print("Updated assets.js and i18n.js with localized dummy data!")
