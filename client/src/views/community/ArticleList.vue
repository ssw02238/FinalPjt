<template>
  <div>
    <ul>
    <li v-for="(article, idx) in articles" :key="idx">
      <span>{{ article.title }}</span>
      <span>{{ article.content }}</span>
    </li>
    </ul>
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