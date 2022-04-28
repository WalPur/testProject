
function Tabs() {
    return (
      <div className="Tabs container-fluid">
        <ul className="nav nav-tabs">
            <li className="nav-item">
                <a className="nav-link active" href="#">Редактор</a>
            </li>
            <li className="nav-item">
                <a className="nav-link" href="#">Доступ</a>
            </li>
            <li className="nav-item">
                <a className="nav-link" href="#">Форма регистрации</a>
            </li>
            <li className="nav-item">
                <a className="nav-link disabled">Заявки</a>
            </li>
            <li className="nav-item">
                <a className="nav-link disabled">Таблица</a>
            </li>
        </ul>
      </div>
    );
  }
  
  export default Tabs;
  