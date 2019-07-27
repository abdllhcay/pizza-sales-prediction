import Vue from 'vue'
import Router from 'vue-router'
import store from './store.js'
import Home from './views/Home.vue'
import NewTask from './views/NewTask.vue'
import Result from './views/Result.vue'
import Login from './views/Login.vue'
import Register from './views/Register.vue'

Vue.use(Router)

let router = new Router({
  mode: 'history',
  base: process.env.BASE_URL,
  routes: [
    {
      path: '/',
      name: 'home',
      component: Home,
      meta: { 
        requiresAuth: true
      }
    },
    {
      path: '/create',
      name: 'create-task',
      component: NewTask,
      meta: { 
        requiresAuth: true
      }
    },
    {
      path: '/result/:id',
      name: 'result',
      component: Result,
      meta: { 
        requiresAuth: true
      }
    },
    {
      path: '/login',
      name: 'login',
      component: Login
    },
    {
      path: '/register',
      name: 'register',
      component: Register
    }
  ]
})


router.beforeEach((to, from, next) => {
  if(to.matched.some(record => record.meta.requiresAuth)) {
    if (store.getters.isLoggedIn) {
      next()
      return
    }
    next('/login') 
  } else {
    next() 
  }
})

export default router
