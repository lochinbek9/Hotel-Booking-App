
import { Outlet } from "react-router-dom"
import Navbar from "../pages/hotelOwner/Navbar"
import SideBar from "./hotelOwner/SideBar"

function Layout() {
  return (
    <div className="flex flex-col h-screen">
        <Navbar/>
        <div className="flex h-full">
          <SideBar />
          <div className="flex-1 p-4 pt-10 md:px-10 h-full">
            <Outlet/>
          </div>
        </div>
    </div>
  )
}

export default Layout