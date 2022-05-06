import React, { useEffect } from 'react';
import { fetchUsers } from '../asyncActions/users';
import { useDispatch, useSelector } from 'react-redux';


import Header from './components/header'


function Users() {


  const dispatch = useDispatch();
  const users = useSelector(state => state.users.users);
  useEffect(() => {
      dispatch(fetchUsers())
  }, []);


  return (
    <div className="Users">
      <Header />
      <div className='TournamentsTable container'>
        <table className='table'>
          <thead>
            <tr>
              <th scope='col'>
                Имя пользователя
              </th>
              <th scope='col'>
                Права доступа
              </th>
            </tr>
          </thead>
          <tbody>
            {
            users.map((User) =>
            <tr key={User.id}>
              <td>{User.username}</td>
              <td>{User.is_mod ? "да" : "нет"}</td>
            </tr>
            )
            }
          </tbody>
        </table>
      </div>
    </div>
  );
}

export default Users;