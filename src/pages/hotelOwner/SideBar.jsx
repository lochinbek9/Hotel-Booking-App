import { assets } from "../../assets/assets"

function SideBar() {
    const sidebarLinks = [
        {name: "Dashboard", path: "/owner", icon: assets.dashboardIcon},
        {name: "Add Room", path: "/owner", icon: assets.addIcon},
        {name: "List Room", path: "/list-room", icon: assets.listIcon},
    ]
  return (
    <div className="md:w-64 w-16 border-r h-full text-base border-gray-300 pt-4 flex flex-col transition-all duration-300">
        
    </div>
  )
}

export default SideBar