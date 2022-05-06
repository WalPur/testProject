import { getTournamentsAction } from '../store/tournamentsReducer';


export const fetchTournaments = () => {
    return dispatch => {
        fetch('http://127.0.0.1:8000/api/tournaments/')
            .then(response => response.json())
            .then(json => dispatch(getTournamentsAction(json)))
    }
}