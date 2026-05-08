import { assets } from "../assets/assets"
import { useTranslation } from "react-i18next";

function Hero() {
    const { t } = useTranslation();
    return (
        <div className='flex flex-col items-start justify-center px-6 md:px-16 lg:px-24 xl:px-32 text-white bg-[url("/src/assets/heroImage.png")] bg-no-repeat bg-cover bg-center h-screen'>
            <p className="bg-[#49B9FF]/50 px-3.5 py-1 rounded-full mt-20">{t('The Ultimate Hotel Experience')}</p>
            <h1 className="font-playfair text-2xl md:text-5xl md:text-[56px] md:leading[56px] font-bold md:font-extrabold max-w-xl mt-4">
                {t('Hero Title')}
            </h1>
            <p className="max-w-130 mt-2 text-sm md:text-base mb-6 font-medium drop-shadow-md">
                {t('Hero Subtitle')}
            </p>
            <button className="bg-orange-500 hover:bg-orange-600 text-white px-8 py-3 rounded-full font-medium transition-all text-lg shadow-lg shadow-orange-500/30 cursor-pointer">
                {t('Book Now', 'Hoziroq band qilish')}
            </button>

            <form className='bg-white text-gray-500 rounded-lg px-6 py-4  flex flex-col md:flex-row max-md:items-start gap-4 max-md:mx-auto mt-8'>

                <div>
                    <div className='flex items-center gap-2'>
                        <img src={assets.homeIcon} alt="Room" className="h-4" />
                        <label htmlFor="roomTypeInput">{t('Room Type')}</label>
                    </div>
                    <select id="roomTypeInput" className="rounded border border-gray-200 px-3 py-1.5 mt-1.5 text-sm outline-none w-full bg-white text-gray-700 min-w-32 cursor-pointer">
                        <option value="All">{t('All Rooms')}</option>
                        <option value="Standard">{t('Standard Room')}</option>
                        <option value="Luxury">{t('Luxury Suite')}</option>
                        <option value="Family">{t('Family Suite')}</option>
                    </select>
                </div>

                <div>
                    <div className='flex items-center gap-2'>
                        <img src={assets.calenderIcon} alt="Calendar" className="h-4" />
                        <label htmlFor="checkIn">{t('Check in')}</label>
                    </div>
                    <input id="checkIn" type="date" className=" rounded border border-gray-200 px-3 py-1.5 mt-1.5 text-sm outline-none" />
                </div>

                <div>
                    <div className='flex items-center gap-2'>
                        <img src={assets.calenderIcon} alt="Calendar" className="h-4" />
                        <label htmlFor="checkOut">{t('Check out')}</label>
                    </div>
                    <input id="checkOut" type="date" className=" rounded border border-gray-200 px-3 py-1.5 mt-1.5 text-sm outline-none" />
                </div>

                <div className='flex md:flex-col max-md:gap-2 max-md:items-center'>
                    <label htmlFor="guests">{t('Guests')}</label>
                    <input min={1} max={4} id="guests" type="number" className=" rounded border border-gray-200 px-3 py-1.5 mt-1.5 text-sm outline-none  max-w-16" placeholder="0" />
                </div>

                <button className='flex items-center justify-center gap-1 rounded-md bg-black py-3 px-4 text-white my-auto cursor-pointer max-md:w-full max-md:py-1' >
                    <img src={assets.searchIcon} alt="Search Icon" className="h-7" />
                    <span>{t('Search')}</span>
                </button>
            </form>
        </div>
    )
}

export default Hero