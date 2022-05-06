import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import React, { useEffect, useState } from 'react';
import axios from 'axios'


import 'bootstrap/dist/css/bootstrap.min.css';
import Editor from './pages/editor'
import Access from "./pages/access";
import Registration from "./pages/registration";
import Home from "./pages/home";
import Users from "./pages/users";
import Tournaments from "./pages/tournaments";


function App() {
  
    const [userState, setUserState] = useState();

    useEffect(() => {
        const apiUrl = 'http://127.0.0.1:8000/api/users/';
        axios.get(apiUrl).then((resp) => {
          const allUsers = resp.data;
          setUserState(allUsers);
        });
      }, []);


  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/tournaments' element={<Tournaments/>}>
            <Route path='editor' element={<Editor/>}></Route>
            <Route path='access' element={<Access/>}></Route>
            <Route path='registration' element={<Registration/>}></Route>
          </Route>
          <Route path='/users' element={<Users Users={userState}/>}></Route>
          <Route path='/' element={<Home/>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
