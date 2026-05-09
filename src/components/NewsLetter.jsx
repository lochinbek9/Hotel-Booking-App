import React from 'react'
import { assets } from '../assets/assets'
import Title from './Title'
import { useTranslation } from 'react-i18next';

function NewsLetter() {
  const { t } = useTranslation();
  return (
    <div className="flex justify-center items-center flex-col gap-6 px-6 md:px-16 lg:px-24 xl:px-32 py-20">
      <iframe src="https://yandex.uz/map-widget/v1/org/140753485947/?ll=72.332490%2C40.812586&z=16" width="860" height="400" frameBorder="1" allowFullScreen={true}></iframe>
    </div>
  )
}

export default NewsLetter