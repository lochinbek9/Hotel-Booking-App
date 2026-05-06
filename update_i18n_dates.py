import re
import os

i18n_path = "/Users/user/Desktop/Hotel-Booking-App/src/i18n.js"

with open(i18n_path, "r", encoding="utf-8") as f:
    content = f.read()

uz_entries = """
      "Aug 31": "31-avgust",
      "Sep 20": "20-sentyabr",
      "Sep 25": "25-sentyabr"
"""

ru_entries = """
      "Aug 31": "31 авг",
      "Sep 20": "20 сен",
      "Sep 25": "25 сен"
"""

en_entries = """
      "Aug 31": "Aug 31",
      "Sep 20": "Sep 20",
      "Sep 25": "Sep 25"
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

print("Updated i18n.js with dates!")
