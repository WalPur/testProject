import { createStore, combineReducers, applyMiddleware } from "redux";
import { composeWithDevTools } from 'redux-devtools-extension';
import thunk from 'redux-thunk';


import { tournamentsReducer } from "./tournamentsReducer";
import { usersReducer } from "./usersReducer";


const rootReducer = combineReducers({
    tournaments: tournamentsReducer,
    users: usersReducer
})


export const store = createStore(rootReducer, composeWithDevTools(applyMiddleware(thunk)))