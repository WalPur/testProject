const defaultState = {
    tournaments: []
}


const GET_TOURNAMENTS = "GET_TOURNAMENTS"


export const tournamentsReducer = (state = defaultState, action) => {
    console.log(action.payload)
    console.log(state)
    switch (action.type) {
      case GET_TOURNAMENTS:
        return {...state, tournaments: action.payload}
      default:
        return state;
    }
  }

export const getTournamentsAction = (payload) => ({type: GET_TOURNAMENTS, payload})