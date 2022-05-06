import { getUsersAction } from "../store/usersReducer"



export const fetchUsers = () => {
    return dispatch => {
        fetch('http://127.0.0.1:8000/api/users/')
            .then(response => response.json())
            .then(json => dispatch(getUsersAction(json)))
    }
}