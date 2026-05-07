import { Link } from "react-router-dom"
import { assets, facilityIcons } from "../assets/assets"
import { useTranslation } from "react-i18next";

function HotelCard({room, index}) {
  const { t } = useTranslation();
  return (
    <Link to={"/rooms/" + room._id} onClick={()=>scrollTo(0,0)} key={room._id} className="relative max-w-70 w-full rounded-2xl overflow-hidden bg-white text-gray-500/90 shadow-[0px_4px_4px_rgba(0,0,0,0.05)]">
        <img src={room.images[0]} alt="Hotel" />

        {index % 2 === 0 &&  <p className="px-3 py-1 absolute top-3 left-3 text-xs bg-white text-gray-800 font-medium rounded-full">{t('Best Seller', 'Best Seller')}</p>}

        <div className="p-4 pt-5">
            <div className="flex items-center justify-between">
                <p className="font-playfair text-xl font-medium text-gray-800">{t(room.roomType)}</p>
                
                <div className="flex items-center gap-1">
                    <img src={assets.starIconFilled} alt="Star" /> 4.5
                </div>
               
            </div>
            <div className="flex items-center gap-1 text-sm mt-1 mb-1">
                 <img src={assets.locationIcon} alt="Location Icon" /> 
                 <span className="truncate">{t(room.hotel.address)}</span>
            </div>
            
            <div className="flex items-center gap-2 mt-3 flex-wrap">
                {room.amenities.slice(0,3).map((amenity, i) => (
                    <div key={i} className="flex items-center gap-1 text-xs text-gray-500 bg-gray-50 px-2 py-1 rounded">
                        <img src={facilityIcons[amenity]} alt={amenity} className="w-3.5 h-3.5 opacity-70" />
                        <span>{t(amenity)}</span>
                    </div>
                ))}
            </div>
            
            <div className="flex items-center justify-between mt-4">
                <p> <span className="text-xl text-gray-800"> ${room.pricePerNight} </span> {t('/night', '/night')}</p>
                <button className="px-4 py-2 text-sm font-medium border border-gray-300 rounded hover:bg-gray-50 transition-all cursor-pointer">{t('Book Now', 'Book Now')}</button>
            </div>
        </div>
    </Link>
  )
}

export default HotelCard