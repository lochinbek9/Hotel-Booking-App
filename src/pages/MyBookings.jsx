import Title from "../components/Title"
import { assets, userBookingsDummyData } from "../assets/assets"
import { useState } from "react"
import { useTranslation } from "react-i18next";

const formatDate = (dateString) => {
    const d = new Date(dateString);
    const day = String(d.getDate()).padStart(2, '0');
    const month = String(d.getMonth() + 1).padStart(2, '0');
    const year = d.getFullYear();
    return `${day}.${month}.${year}`;
};

function MyBookings() {
    const { t } = useTranslation();
    const [bookings, setBookings] = useState(userBookingsDummyData)
    return (
        <div className="py-28 md:pb-35 md:pt-32 px-4 md:px-16 lg:px-24 xl:px-32">
            <Title title={t("My Bookings", "My Bookings")} subTitle={t('My Bookings Subtitle', 'Easily manage your past, current, and upcoming hotel reservations in one place. Plan your trips seamlessly with just a few clicks')} align="left" />

            <div className="max-w-6xl mt-8 w-full text-gray-800">
                <div className="hidden md:grid md:grid-cols-[3fr_2fr_1fr] w-full border-b border-gray-300 font-medium text-base py-3">
                    <div>{t('Hotels', 'Hotels')}</div>
                    <div>{t('Date & Timings', 'Date & Timings')}</div>
                    <div>{t('Payment', 'Payment')}</div>
                </div>
                {bookings.map((booking) => (
                    <div key={booking._id} className="grid grid-cols-1 md:grid-cols-[3fr_2fr_1fr] w-full border-b border-gray-300 py-6 first:border-t">
                        {/* Hotel Details */}
                        <div className="flex flex-col md:flex-row">
                            <img src={booking.room.images[0]} alt="hotel-img" className="md:w-44 rounded shadow object-cover" />
                            <div className="flex flex-col gap-1.5 md:ml-4 mt-3 md:mt-0">
                                <p className="font-playfair text-2xl">
                                    {t(booking.hotel.name)}
                                    <span className="font-inter text-sm"> ({t(booking.room.roomType)})</span>
                                </p>
                                <div className="flex items-center gap-1 text-sm text-gray-500">
                                    <img src={assets.locationIcon} alt="location-icon" />
                                    <span>{t(booking.hotel.address)}</span>
                                </div>
                                <div className="flex items-center gap-1 text-sm text-gray-500">
                                    <img src={assets.locationIcon} alt="guests-icon" />
                                    <span>{t('Guests', 'Guests')}: {booking.guests}</span>
                                </div>
                                <p className="text-base">{t('Total', 'Total')}: ${booking.totalPrice}</p>
                            </div>
                        </div>
                        {/* Date & Timings */}
                        <div className="flex flex-row md:items-center gap-6 md:gap-8 mt-3 md:mt-0">
                            <div>
                                <p>{t('Check-In', 'Check-In')}:</p>
                                <p className="text-gray-500 text-sm">
                                    {formatDate(booking.checkInDate)}
                                </p>
                            </div>
                            <div>
                                <p>{t('Check-Out', 'Check-Out')}:</p>
                                <p className="text-gray-500 text-sm">
                                    {formatDate(booking.checkOutDate)}
                                </p>
                            </div>
                        </div>
                        {/* Payment Status */}
                        <div className="flex flex-col items-start justify-center pt-3">
                            <div className="flex items-center gap-2">
                                <div className={`h-3 w-3 rounded-full ${booking.isPaid ? "bg-green-500" : "bg-red-500"}`}></div>
                                <p className={`text-sm ${booking.isPaid ? "text-green-500" : "text-red-500"}`}>
                                    {booking.isPaid ? t("Paid", "Paid") : t("Unpaid", "Unpaid")}
                                </p>
                            </div>
                            {!booking.isPaid && (
                                <button className="px-4 py-1.5 mt-4 text-xs border border-gray-400 rounded-full hover:bg-gray-50 tracking-all cursor-pointer">
                                    {t('Pay Now', 'Pay Now')}
                                </button>
                            )}
                        </div>
                    </div>
                ))}
            </div>
        </div>
    )
}

export default MyBookings