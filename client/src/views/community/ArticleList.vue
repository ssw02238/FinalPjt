<template>
  <div class="container">
    <div>
      <span class="me-3" style="font-size:25px;font-family: 'Noto Sans KR', sans-serif;">현재 상영작 리뷰 확인하기</span>
      <router-link :to="{ name: 'CreateArticle' }"><button class="btn btn-warning ms-5" style="font-family:'Noto Sans KR', sans-serif;font-size:25px">새 글 작성하기</button></router-link> 
      
    </div>
    <hr>
    <table class="table" style="font-size:20px; border-radius: 1em;background-color:#e0e8ed;">
      <thead>
        <tr>
          <th scope="col">Rank</th>
          <th scope="col">영화 제목</th>
          <th scope="col">한줄평</th>
          <th scope="col">☆☆☆☆☆</th>
        </tr>
      </thead>
      <tbody v-for="(article, idx) in articles" :key="idx" @click="goDetail(article.movieId)" style="background-color:#9d9b9a;">
        <tr>

          <th>{{ idx+1 }}</th>
          <th>{{ article.movietitle }}</th>
          <th>{{ article.content }}</th>
          <th v-if="article.rating === 5">★★★★★</th>
          <th v-else-if="4 <= article.rating">☆★★★★</th>
          <th v-else-if="3 <= article.rating">☆☆★★★</th>
          <th v-else-if="2 <= article.rating">☆☆☆★★</th>
          <th v-else-if="1 <= article.rating">☆☆☆☆★</th>
          <th v-else></th>

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
          console.log(this.articles[0])
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

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap');

td, th {
  color: black;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 25px;
}
th button {
  color: white;
  background: #5a6160;
}
td span {
  color: black;

}
</style>