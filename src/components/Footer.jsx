import { Link } from "react-router-dom"
import { assets } from "../assets/assets"
import { useTranslation } from "react-i18next";

function Footer() {
    const { t } = useTranslation();
    return (
        <div className='bg-[#F6F9FC ] text-gray-500/80 pt-8 px-6 md:px-16 lg:px-24 xl:px-32'>
            <div className='flex flex-wrap justify-between gap-12 md:gap-6'>
                <div className='max-w-80'>
                    <Link to="/" className="inline-block mb-4">
                        <span className="font-playfair text-2xl font-bold text-gray-800">Mirzo hotel</span>
                    </Link>
                    <p className='text-sm'>
                        {t('Footer Description', "Discover the world's most extraordinary places to stay, from boutique hotels to luxury villas and private islands.")}
                    </p>
                    <div className='flex items-center gap-3 mt-4'>
                        {/* Instagram */}
                        <img src={assets.instagramIcon} alt="instagram icon" className="w-6"/>
                        {/* Facebook */}
                        <img src={assets.facebookIcon} alt="Facebook icon" />
                        {/* Twitter */}
                       <img src={assets.twitterIcon} alt="Twitter" />
                        {/* LinkedIn */}
                        <img src={assets.linkendinIcon} alt="Twitter" />
                    </div>
                </div>

                <div>
                    <p className='font-playfair  text-lg text-gray-800'>{t('COMPANY', 'COMPANY')}</p>
                    <ul className='mt-3 flex flex-col gap-2 text-sm'>
                        <li><a href="#">{t('About', 'About')}</a></li>
                        <li><a href="#">{t('Careers', 'Careers')}</a></li>
                        <li><a href="#">{t('Press', 'Press')}</a></li>
                        <li><a href="#">{t('Blog', 'Blog')}</a></li>
                        <li><a href="#">{t('Partners', 'Partners')}</a></li>
                    </ul>
                </div>

                <div>
                    <p className='font-playfair text-lg text-gray-800'>{t('SUPPORT', 'SUPPORT')}</p>
                    <ul className='mt-3 flex flex-col gap-2 text-sm'>
                        <li><a href="#">{t('Help Center', 'Help Center')}</a></li>
                        <li><a href="#">{t('Safety Information', 'Safety Information')}</a></li>
                        <li><a href="#">{t('Cancellation Options', 'Cancellation Options')}</a></li>
                        <li><a href="#">{t('Contact Us', 'Contact Us')}</a></li>
                        <li><a href="#">{t('Accessibility', 'Accessibility')}</a></li>
                    </ul>
                </div>

                <div className='max-w-80'>
                    <p className='font-playfair text-lg text-gray-800'>{t('STAY UPDATED', 'STAY UPDATED')}</p>
                    <p className='mt-3 text-sm'>
                        {t('Footer Subscribe', 'Subscribe to our newsletter for inspiration and special offers.')}
                    </p>
                    <div className='flex items-center mt-4'>
                        <input type="text" className='bg-white rounded-l border border-gray-300 h-9 px-3 outline-none' placeholder={t('Your email', 'Your email')} />
                        <button className='flex items-center justify-center bg-black h-9 w-9 aspect-square rounded-r'>
                            {/* Arrow icon */}
                           <img src={assets.arrowIcon} alt="Arrow Icon" className="w-3.5 invert" />
                        </button>
                    </div>
                </div>
            </div>
            <hr className='border-gray-300 mt-8' />
            <div className='flex flex-col md:flex-row gap-2 items-center justify-between py-5'>
                <p>© {new Date().getFullYear()} Mirzo hotel. {t('All rights reserved.', 'All rights reserved.')}</p>
                <ul className='flex items-center gap-4'>
                    <li><a href="#">{t('Privacy', 'Privacy')}</a></li>
                    <li><a href="#">{t('Terms', 'Terms')}</a></li>
                    <li><a href="#">{t('Sitemap', 'Sitemap')}</a></li>
                </ul>
            </div>
        </div>
    )
}

export default Footer