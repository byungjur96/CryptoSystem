import Vue from 'vue';
import Vuex from 'vuex';
import Constant from '../Constant';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        algorithm: "RSA",
        open_keygen_modal: false 
    },
    mutations: {
        change (state, alg) {
            state.algorithm = alg;
        },
        open_modal (state) {
            state.open_keygen_modal = !state.open_keygen_modal;
        },

    }
});

export default store;