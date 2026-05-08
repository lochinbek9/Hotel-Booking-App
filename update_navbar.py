import os

navbar_path = "/Users/user/Desktop/Hotel-Booking-App/src/components/Navbar.jsx"

with open(navbar_path, "r", encoding="utf-8") as f:
    content = f.read()

# 1. Update Desktop Language Switcher
old_lang_desktop = """                    {/* Language Switcher */}
                    <select 
                        value={i18n.language} 
                        onChange={(e) => i18n.changeLanguage(e.target.value)}
                        className={`bg-transparent outline-none cursor-pointer ${isScrolled ? 'text-gray-700' : 'text-white'}`}
                    >
                        <option value="uz" className="text-black">UZ</option>
                        <option value="ru" className="text-black">RU</option>
                        <option value="en" className="text-black">EN</option>
                    </select>"""
new_lang_desktop = """                    {/* Language Switcher */}
                    <div className="flex items-center gap-1">
                        <span className={`${isScrolled ? 'text-gray-700' : 'text-white'}`}>🌐</span>
                        <select 
                            value={i18n.language} 
                            onChange={(e) => i18n.changeLanguage(e.target.value)}
                            className={`bg-transparent outline-none cursor-pointer font-medium ${isScrolled ? 'text-gray-700' : 'text-white'}`}
                        >
                            <option value="uz" className="text-black">UZ</option>
                            <option value="ru" className="text-black">RU</option>
                            <option value="en" className="text-black">EN</option>
                        </select>
                    </div>"""
content = content.replace(old_lang_desktop, new_lang_desktop)

# 2. Update Mobile Language Switcher
old_lang_mobile = """                    <select 
                        value={i18n.language} 
                        onChange={(e) => i18n.changeLanguage(e.target.value)}
                        className="bg-transparent outline-none cursor-pointer"
                    >
                        <option value="uz" className="text-black">O'zbekcha (UZ)</option>
                        <option value="ru" className="text-black">Русский (RU)</option>
                        <option value="en" className="text-black">English (EN)</option>
                    </select>"""
new_lang_mobile = """                    <div className="flex items-center gap-2">
                        <span>🌐</span>
                        <select 
                            value={i18n.language} 
                            onChange={(e) => i18n.changeLanguage(e.target.value)}
                            className="bg-transparent outline-none cursor-pointer font-medium"
                        >
                            <option value="uz" className="text-black">O'zbekcha (UZ)</option>
                            <option value="ru" className="text-black">Русский (RU)</option>
                            <option value="en" className="text-black">English (EN)</option>
                        </select>
                    </div>"""
content = content.replace(old_lang_mobile, new_lang_mobile)

# 3. Hide Dashboard Button (Desktop)
old_dash_desktop = """                    <button className={`border px-4 py-1 text-sm font-light rounded-full cursor-pointer ${isScrolled ? 'text-black' : 'text-white'} transition-all`} onClick={() => navigate("/owner")}>
                        {t('Dashboard')}
                    </button>"""
new_dash_desktop = """                    {/* Admin Dashboard hidden for guests */}
                    {false && <button className={`border px-4 py-1 text-sm font-light rounded-full cursor-pointer ${isScrolled ? 'text-black' : 'text-white'} transition-all`} onClick={() => navigate("/owner")}>
                        {t('Dashboard')}
                    </button>}"""
content = content.replace(old_dash_desktop, new_dash_desktop)

# 4. Hide Dashboard Button (Mobile)
old_dash_mobile = """                   {user &&  <button className="border border-black px-4 py-1 text-sm font-light rounded-full cursor-pointer transition-all" onClick={() => navigate("/owner")}>
                       {t('Dashboard')}
                    </button>}"""
new_dash_mobile = """                   {/* Admin Dashboard hidden for guests */}
                   {false && user &&  <button className="border border-black px-4 py-1 text-sm font-light rounded-full cursor-pointer transition-all" onClick={() => navigate("/owner")}>
                       {t('Dashboard')}
                    </button>}"""
content = content.replace(old_dash_mobile, new_dash_mobile)

with open(navbar_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated Navbar.jsx successfully!")
