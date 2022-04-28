import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";


import 'bootstrap/dist/css/bootstrap.min.css';
import Editor from './pages/editor'
import Access from "./pages/access";
import Registration from "./pages/registration";
import Home from "./pages/home";
import Users from "./pages/users";


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Home/>}></Route>
          <Route path='/tournaments' element={<Editor/>}>
            <Route path='editor' element={<Editor/>}></Route>
            <Route path='access' element={<Access/>}></Route>
            <Route path='registration' element={<Registration/>}></Route>
          </Route>
          <Route path='/users' element={<Users/>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
