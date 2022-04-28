import { NavLink } from 'react-router-dom';


function Header() {
  return (
    <div className="Header">
      <header>
          <nav className="navbar navbar-expand-lg navbar-light bg-light">
            <div className="container-fluid">
                <NavLink className={({ isActive }) => (isActive ? 'active nav-link' : 'inactive nav-link')} to="/">LOGO</NavLink>
                <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
                </button>
                <div className="collapse navbar-collapse" id="navbarNavDropdown">
                <ul className="navbar-nav">
                    <li className="nav-item">
                      <NavLink className={({ isActive }) => (isActive ? 'active nav-link' : 'inactive nav-link')} to="/users">Пользователи</NavLink>
                    </li>
                    <li className="nav-item">
                      <NavLink className={({ isActive }) => (isActive ? 'active nav-link' : 'inactive nav-link')} to="/tournaments">Турниры</NavLink>
                    </li>
                </ul>
                </div>
            </div>
          </nav>
      </header>
    </div>
  );
}

export default Header;
