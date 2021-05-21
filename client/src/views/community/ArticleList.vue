<template>
  <div>
    <router-link :to="{ name: 'CreateArticle' }"><button class="btn btn-success">새 글 작성하기</button></router-link> 
    <hr>
    <table class="table container">
      <thead>
        <tr>
          <th scope="col">#</th>
          <th scope="col">제목</th>
          <th scope="col">내용</th>
          <th scope="col">별점</th>
        </tr>
      </thead>
      <tbody v-for="(article, idx) in articles" :key="idx">
        <tr>
          <th scope="row">{{ article.id }}</th>
          <td>{{ article.title }}</td>
          <td>{{ article.content }}</td>
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
          console.log(res)
          this.articles = res.data
        })
        .catch((err) => {
          console.log(err)
        })
        this.title = null
        this.content = null
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getArticles()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style>

</style>