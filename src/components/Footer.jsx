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
                    
                    <div className="mt-6 flex flex-col gap-3">
                        <a href="tel:+998901234567" className="flex items-center gap-2 text-gray-800 hover:text-primary font-medium text-lg transition-all">
                            <span className="text-xl">📞</span> +998 90 123 45 67
                        </a>
                        <a href="https://maps.google.com" target="_blank" rel="noreferrer" className="flex items-center gap-2 text-primary hover:text-primary-dull transition-all text-sm font-medium">
                            <img src={assets.locationFilledIcon} alt="Location" className="w-5" />
                            {t('Open in Google Maps', 'Open in Google Maps')}
                        </a>
                    </div>
                    
                    <div className='flex items-center gap-3 mt-6'>
                        <a href="#" className="w-6 h-6 flex items-center justify-center rounded-full bg-[#0088cc] text-white hover:scale-110 transition-transform">
                           <svg viewBox="0 0 24 24" fill="currentColor" className="w-4 h-4"><path d="M11.944 0A12 12 0 0 0 0 12a12 12 0 0 0 12 12 12 12 0 0 0 12-12A12 12 0 0 0 12 0a12 12 0 0 0-.056 0zm4.962 7.224c.1-.002.321.023.465.14a.506.506 0 0 1 .171.325c.016.093.036.306.02.472-.18 1.898-.962 6.502-1.36 8.627-.168.9-.499 1.201-.82 1.23-.696.065-1.225-.46-1.9-.902-1.056-.693-1.653-1.124-2.678-1.8-1.185-.78-.417-1.21.258-1.91.177-.184 3.247-2.977 3.307-3.23.007-.032.014-.15-.056-.212s-.174-.041-.249-.024c-.106.024-1.793 1.14-5.061 3.345-.48.33-.913.49-1.302.48-.428-.008-1.252-.241-1.865-.44-.752-.245-1.349-.374-1.297-.789.027-.216.325-.437.888-.666 3.498-1.524 5.83-2.529 6.998-3.014 3.332-1.386 4.025-1.627 4.476-1.635z"/></svg>
                        </a>
                        <img src={assets.instagramIcon} alt="instagram icon" className="w-6 hover:scale-110 transition-transform cursor-pointer"/>
                        <img src={assets.facebookIcon} alt="Facebook icon" className="w-6 hover:scale-110 transition-transform cursor-pointer" />
                       <img src={assets.twitterIcon} alt="Twitter" className="w-6 hover:scale-110 transition-transform cursor-pointer" />
                        <img src={assets.linkendinIcon} alt="LinkedIn" className="w-6 hover:scale-110 transition-transform cursor-pointer" />
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