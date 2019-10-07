import Vue from 'vue'
import Router from 'vue-router'
import Home from './views/Home.vue'

Vue.use(Router)

export default new Router({
  mode: 'history',
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      children: [
        {
          path: '/login',
          name: 'login',
          component: () => import(/* webpackChunkName: "login" */ './components/Login.vue')
        },
        {
          path: '/registration',
          name: 'registration',
          component: () => import(/* webpackChunkName: "registration" */ './components/Registration.vue')
        }
      ]
    }
  ]
})
