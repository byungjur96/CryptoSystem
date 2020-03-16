import Vue from 'vue';
import Vuex from 'vuex';
import Constant from '../Constant';

Vue.use(Vuex);

const store = new Vuex.Store({
    state: {
        algorithm: "RSA"
    },
    mutations: {

        }
    }
);

export default store;