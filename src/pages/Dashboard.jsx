
import { useState } from "react"
import { assets, dashboardDummyData } from "../assets/assets"
import Title from "../components/Title"

function Dashboard() {
  const [dashboardData, setDashboardData] = useState(dashboardDummyData)
  return (
    <div>

      <Title align='left' font='outfit' title='Dashboard' subTitle='Monitor your
room listings, track bookings and analyze revenue-all in one place. Stay
updated with real-time insights to ensure smooth operations.'/>

      <div className="flex gap-4 my-8">
        {/* Total Bookings */}
        <div className="bg-primary/3 border border-primary/10 rounded flex p-4 pr-8">
          <img src={assets.totalBookingIcon}
            className="max-sm:hidden h-10" alt="" />
          <div>
            <p>Total Bookings</p>
            <p>{dashboardData.totalBookings}</p>
          </div>
        </div>
        {/* Total Revenue */}
        <div className="bg-primary/3 border border-primary/10 rounded flex p-4 pr-8">
          <img src={assets.totalRevenueIcon} alt="" className="max-sm:hidden h-10" />

          <div className="flex flex-col sm:ml-4 font-medium">
            <p className="text-blue-500 text-lg">Total Revenue</p>
            <p className="text-neutral-400 text-base">
              $ {dashboardData.totalRevenue}
            </p>
          </div>
        </div>
      </div>

      {/* Recent Bookings */}

      <h2 className="text-xl text-blue-950/70 font-medium mb-5">
        Recent Bookings
      </h2>
      <div className="w-full max-w-3xl text-left border border-gray-300 rounded-lg max-h-80 overflow-y-scroll">
          
      </div>

    </div>
  )
}

export default Dashboard