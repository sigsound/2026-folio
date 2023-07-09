import React from 'react'
import { Link } from 'gatsby'
import icon from '../images/icon.svg'
import './header.css'

const Header = () => (
  <div className="Header">
    <div className="HeaderGroup">
      <Link className="Logo" to="/">
        <img src={icon} alt="An iconographic representation of Nick Woods" width="48" />
      </Link>
    </div>
  </div>
)

export default Header
