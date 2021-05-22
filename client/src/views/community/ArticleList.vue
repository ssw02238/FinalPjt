<template>
  <div>
    <router-link :to="{ name: 'CreateArticle' }"><button class="btn btn-success">새 글 작성하기</button></router-link> 
    <hr>
    <table class="table container">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">제목</th>
          <th scope="col">별점</th>
          <th scope="col">아이콘</th>
        </tr>
      </thead>
      <tbody v-for="(article, idx) in articles" :key="idx" @click="goDetail(article.id)">
        <tr>
          <th scope="row">{{ article.id }}</th>
          <th>{{ article.movietitle }}</th>
          <td>{{ article.title }}</td>
          <td>{{ article.rating }}</td>
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
      movieId: null,
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
      this.$router.push({ name: 'ArticleDetail',  params: {id: id }})
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

<style>

</style>