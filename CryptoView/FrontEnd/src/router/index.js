import Vue from 'vue';
import Router from 'vue-router';


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