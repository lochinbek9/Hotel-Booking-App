import React from "react"
import Navbar from "./components/Navbar"
import Footer from "./components/Footer";
import { Route, Routes, useLocation } from "react-router-dom"

import Home from "./pages/Home";
import AllRooms from "./pages/AllRooms";

function App() {
  const isOwnerPath = useLocation().pathname.includes("owner");

  return (
    <div>
     {!isOwnerPath &&  <Navbar/>}
     <div className="min-h-[70vh]">
        <Routes>
          <Route path="/" element={<Home/>} /> 
          <Route path="/rooms" element={<AllRooms/>} />
        </Routes>
     </div>
     <Footer/>

    </div>
  )
}

export default App
