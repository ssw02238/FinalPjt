<template>
  <div class="container">
    <div>
      <span class="me-5" style="font-size:23px;font-family: 'Nanum Gothic Coding', monospace;">현재 상영작 리뷰 확인하기</span>
      <router-link :to="{ name: 'CreateArticle' }"><button class="btn btn-success ms-5" style="font-family: 'Nanum Gothic Coding', monospace;font-size:1rem">새 글 작성하기</button></router-link> 
      
    </div>
    <hr>
    <table class="table" style="font-size:20px; border-radius: 1em;background-color:#ddcfd5;">
      <thead>
        <tr>
          <th scope="col">Rank</th>
          <th scope="col">영화 제목</th>
          <th scope="col">글 제목</th>
          <th scope="col">☆☆☆☆☆</th>
        </tr>
      </thead>
      <tbody v-for="(article, idx) in articles" :key="idx" @click="goDetail(article.movieId)">
        <tr>
          <th>{{ idx+1 }}</th>
          <th>{{ article.movietitle }}</th>
          <th>{{ article.title }}</th>
          <th>{{ article.rating }}</th>
        </tr>
      </tbody>
    </table>
  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'ArticleList',
  data: function () {
    return {
      articles: [],
      // id: null,

    }
  },
  methods: {
    setToken: function () {
      const jwtToken = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${jwtToken}`
      }
      return config 
    },
    getArticles: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/articles',
        headers: this.setToken()
      })
        .then((res) => {
          this.articles = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    
    goDetail(id) {
      this.$router.push({ name: 'MovieDetail',  params: {id: id }})
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getArticles()

    } else {
      this.$router.push({name: 'Login'})
    }
  },
}
</script>

<style scoped>
th {
  color: black;
  font-family: 'Nanum Gothic Coding', monospace;
}
th button {
  color: white;
  background: #5a6160;
}
</style>