import Vue from 'vue'
import VueRouter from 'vue-router'
import NowPlaying from '../views/NowPlaying.vue'
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
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
