import React from "react";
import "./Navbar.css" 
import * as Icon from 'react-bootstrap-icons';

function Navbar() {
    return(
        <div className="Navbar"> 
        <ul> 
            <li><h4>My daily task</h4></li>
            <li><Icon.Check2 size="40px" className="check" /></li>
        </ul> 
        </div>
    )
}
export default Navbar