import os

hero_path = "/Users/user/Desktop/Hotel-Booking-App/src/components/Hero.jsx"

with open(hero_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Add CTA Button
old_subtitle = """            <p className="max-w-130 mt-2 text-sm md:text-base">
                {t('Hero Subtitle')}
            </p>"""
new_subtitle = """            <p className="max-w-130 mt-2 text-sm md:text-base mb-6 font-medium drop-shadow-md">
                {t('Hero Subtitle')}
            </p>
            <button className="bg-[#49B9FF] hover:bg-[#3ba0e5] text-white px-8 py-3 rounded-full font-medium transition-all text-lg shadow-lg shadow-[#49B9FF]/30 cursor-pointer">
                {t('View Rooms', 'View Rooms')}
            </button>"""
content = content.replace(old_subtitle, new_subtitle)

# 2. Replace Destination with Room Type dropdown
old_destination = """                <div>
                    <div className='flex items-center gap-2'>
                    <img src={assets.calenderIcon} alt="Calendar" className="h-4" />
                        <label htmlFor="destinationInput">{t('Destination')}</label>
                    </div>
                    <input list='destinations' id="destinationInput" type="text" className=" rounded border border-gray-200 px-3 py-1.5 mt-1.5 text-sm outline-none" placeholder={t('Type here')} required />

                    <datalist id="destinations">
                        {cities.map((city, index) =>{
                            <option value={city} key={index }/>
                        })}
                    </datalist>
                </div>"""
new_room_type = """                <div>
                    <div className='flex items-center gap-2'>
                        <img src={assets.homeIcon} alt="Room" className="h-4" />
                        <label htmlFor="roomTypeInput">{t('Room Type', 'Room Type')}</label>
                    </div>
                    <select id="roomTypeInput" className="rounded border border-gray-200 px-3 py-1.5 mt-1.5 text-sm outline-none bg-white min-w-[150px]">
                        <option value="all">{t('All Rooms', 'All Rooms')}</option>
                        <option value="standard">{t('Standard Room', 'Standard Room')}</option>
                        <option value="deluxe">{t('Deluxe Room', 'Deluxe Room')}</option>
                        <option value="luxury">{t('Luxury Suite', 'Luxury Suite')}</option>
                    </select>
                </div>"""

# Replace assets import to include homeIcon if not there
if "homeIcon" not in content and "cities" in content:
    content = content.replace("calenderIcon, cities", "calenderIcon, homeIcon")
    content = content.replace("cities", "homeIcon") # Just replace cities with homeIcon in import if it was { assets, cities } -> { assets, homeIcon }
    content = content.replace("import { assets, homeIcon }", "import { assets }") # Clean up if it was { assets }

# Safe replace for the import
content = content.replace('import { assets, cities } from "../assets/assets"', 'import { assets } from "../assets/assets"')

content = content.replace(old_destination, new_room_type)

with open(hero_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated Hero.jsx successfully!")
