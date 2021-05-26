import Vue from 'vue'
import VueRouter from 'vue-router'
import NowPlaying from '../views/NowPlaying.vue'
import MovieDetail from '../views/MovieDetail.vue'
import Popular from '../views/Popular.vue'
import Signup from '@/views/accounts/Signup'
import Login from '@/views/accounts/Login'
import ArticleList from '@/views/community/ArticleList'
import CreateArticle from '@/views/community/CreateArticle'
import MyPage from '@/views/accounts/MyPage'


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
    path: '/accounts/signup',
    name: 'Signup',
    component: Signup,
  },
  {
    path: '/accounts/login',
    name: 'Login',
    component: Login,
  },
  {
    path: '/community/articlelist',
    name: 'ArticleList',
    component: ArticleList,
  },
  {
    path: '/community/createarticle',
    name: 'CreateArticle',
    component: CreateArticle,

  },
  {
    path: '/accounts/MyPage',
    name: 'MyPage',
    component: MyPage,

  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
