import Vue from 'vue'
import VueRouter from 'vue-router'
import NowPlaying from '../views/NowPlaying.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Popular from '../views/Popular.vue'
import Random from '../views/Random.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'

Vue.use(VueRouter)

const routes = [
  {
    path: '/popular',
    name: 'Popular',
    component: Popular
  },
  {
    path: '/nowplaying',
    name: 'NowPlaying',
    component: NowPlaying
  },
  {
    path: '/moviedetail/:id',
    name: 'MovieDetail',
    component: MovieDetail
  },
  {
    path: '/random',
    name: 'Random',
    component: Random
  },
  {
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
