import {Routes, Route} from "react-router-dom"

import {Home} from "../Home/Home"
import { Menu } from "../Menu/Menu"
import { Logistica } from "../Logistica/Logistica"
export function Router(){

    return(

        <>

        <Menu></Menu>

        <Routes>
            <Route path="/" element={ <Home /> } />
            <Route path="/logistica" element={ <Logistica /> } />
        </Routes>

        </>
    )

}