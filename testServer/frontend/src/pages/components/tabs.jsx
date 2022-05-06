import { NavLink } from 'react-router-dom';


function Tabs() {
    return (
      <div className="Tabs container-fluid">
        <ul className="nav nav-tabs">
            <li className="nav-item">
                <NavLink className={({ isActive }) => (isActive ? 'active nav-link' : 'inactive nav-link')}  to="/tournaments/editor">Редактор</NavLink>
            </li>
            <li className="nav-item">
                <NavLink className={({ isActive }) => (isActive ? 'active nav-link' : 'inactive nav-link')} to="/tournaments/access">Доступ</NavLink>
            </li>
            <li className="nav-item">
                <NavLink className={({ isActive }) => (isActive ? 'active nav-link' : 'inactive nav-link')} to="/tournaments/registration">Форма регистрации</NavLink>
            </li>
            <li className="nav-item">
                {/* <a className="nav-link disabled">Заявки</a> */}
            </li>
            <li className="nav-item">
                {/* <a className="nav-link disabled">Таблица</a> */}
            </li>
        </ul>
      </div>
    );
  }
  
  export default Tabs;