import React from "react"
import Navbar from "./components/Navbar"
import Footer from "./components/Footer";
import { Route, Routes, useLocation } from "react-router-dom"

import Home from "./pages/Home";
import AllRooms from "./pages/AllRooms";
import RoomDetails from "./pages/RoomDetails";
import MyBookings from "./pages/MyBookings";
import HotelReg from "./components/HotelReg";
import Layout from "./pages/Layout";
import Dashboard from "./pages/Dashboard";
import AddRoom from "./pages/AddRoom";
import ListRoom from "./pages/ListRoom";

function App() {
  const isOwnerPath = useLocation().pathname.includes("owner");

  return (
    <div>
     {!isOwnerPath &&  <Navbar/>}
      {false &&  <HotelReg/>}
     <div className="min-h-[70vh]">
        <Routes>
          <Route path="/" element={<Home/>} /> 
          <Route path="/rooms" element={<AllRooms/>} />
          <Route path="/rooms/:id" element={<RoomDetails/>} />
          <Route path="/my-bookings" element={<MyBookings/>} />
          <Route path="/owner" element={<Layout/>}>
              <Route index element={<Dashboard/>} />
              <Route path="add-room" element={<AddRoom/>} />
              <Route path="list-room" element={<ListRoom/>} />
          </Route>
        </Routes>
     </div>
     <Footer/>

    </div>
  )
}

export default App
