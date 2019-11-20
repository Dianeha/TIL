// auth.js 인증관련 모든 state 를 작성.
// State 에 접근/변경하는 모든 로직은 여기로.
const state = {
    token: null,
};

// Vuex에서는 Arrow Function 
const getters = {
    isLoggedIN: state => !!state.token, // 특정 값을 t/f로 바꾸는 구문
    // isLoggedIN: state => {    
        // if (state.token) {
        //     return true
        // } else {
        //     return false;
        // }
        //} 의 최종 줄임 표현
};

const mutations = {
    setToken: (state, token) => state.token = token,
};

const actions = {
    // logout: (options) => {
    //     // mutations.setToken(state, null) === Very Bad 절대 이렇게 하지 말 것
    //     options.commit('setToken', null) // 넘어오는 객체 option
    //     options.a
    //     options.b
    //     // 공식문서에 'mutation은 commit으로 실행한다'고 되어있음
    // }
    logout: ({ commit, a, b }) => {
        commit('setToken', null)
        a
        b // 이케 바로 꺼내올 수 있도록 적은 새로운 문법....... 흠
    },

    login: ({ commit }, token) => {
        commit('setToken', token)
    },
};

export default {
    state, getters, mutations, actions
}