import ExlusiveOffers from "../components/ExlusiveOffers"
import FeaturedDesinition from "../components/FeaturedDesinition"
import Hero from "../components/Hero"
import NewsLetter from "../components/NewsLetter"
import Testimonial from "../components/Testimonial"

function Home() {
  return (
    <div>
        <Hero/>
        <FeaturedDesinition/>
        <ExlusiveOffers/>
        <Testimonial/>
        <NewsLetter/>
    </div>
  )
}

export default Home