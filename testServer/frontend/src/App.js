import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";


import 'bootstrap/dist/css/bootstrap.min.css';
import Editor from './pages/editor'


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/' element={<Editor/>}></Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
