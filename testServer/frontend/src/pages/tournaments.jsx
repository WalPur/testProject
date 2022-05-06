import React, { useEffect } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { fetchTournaments } from "../asyncActions/tournaments";


import Header from './components/header';
import Tabs from './components/tabs';


function Tournaments() {


    const dispatch = useDispatch();
    const tournaments = useSelector(state => state.tournaments.tournaments);
    useEffect(() => {
        dispatch(fetchTournaments())
    }, []);

    return (
        <div className="Tournaments">
            <Header />
            <Tabs/>
            <div className='TournamentsTable container'>
                <table className='table'>
                    <thead>
                        <tr>
                            <th scope='col'>
                                #
                            </th>
                            <th scope='col'>
                                Название турнира
                            </th>
                            <th scope='col'>
                                Этап турнира
                            </th>
                            <th scope='col'>
                                Период проведения
                            </th>
                            <th scope='col'>
                                Описание
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        {tournaments.length > 0 ?
                            tournaments.map((Tournament) =>
                                <tr key={Tournament.id}>
                                    <td>{Tournament.id}</td>
                                    <td>{Tournament.name}</td>
                                    <td>{Tournament.status}</td>
                                    <td>{Tournament.start_date} - {Tournament.finish_date}</td>
                                    <td>{Tournament.description}</td>
                                </tr>
                            )
                            :
                            <tr>
                                <td>
                                    <h2>Нет турниров</h2>
                                </td>
                            </tr>
                        }
                    </tbody>
                </table>
            </div>
        </div>
    );
}
  
export default Tournaments;
  