import Vue from 'vue'
import VueRouter from 'vue-router'

import Home from '../views/Home.vue'
import Login from '../views/Login.vue'

Vue.use(VueRouter)  // middleware  등록 >> 우리같이 일해보자. 계약서 도장 찍음.


const router = new VueRouter({
  mode: 'history', // 원래의 브라우저 라우팅 방식. '#'이 없음
  routes : [
    {
      path: '/',
      name: 'home',
      component: Home
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    }
  ]
})

export default router
