import Vue from 'vue';
import Router from 'vue-router';
import Submit from '../components/contents/submit'
import History from '../components/contents/History'
import Analysis from '../components/contents/Analysis'

Vue.use(Router);

export default new Router({
    mode: "history",
    routes: [ {
        path: '/submit',
        component: Submit
    },
    {
        path: '/history',
        component: History
    },
    {
        path: '/analysis',
        component: Analysis
    } 
    ]
}

)