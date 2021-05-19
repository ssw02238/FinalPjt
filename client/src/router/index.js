import Vue from 'vue'
import VueRouter from 'vue-router'
import Latest from '../views/Latest.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Popular from '../views/Popular.vue'
import Random from '../views/Random.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/popular',
    name: 'Popular',
    component: Popular
  },
  {
    path: '/latest',
    name: 'Latest',
    component: Latest
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
