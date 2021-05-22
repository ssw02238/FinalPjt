<template>
  <div>
    <p>{{ title }}</p>
    <p>{{ content }}</p>
    <p>{{ rating }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'ArticleDetail',
  data: function () {
    return {
      article: null,
      id: null,
      content: null,
      title: null,
      rating: null,
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
    getArticle: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/articles',
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.article = res.data[this.id-1]
          this.content = this.article.content
          this.title = this.article.title
          this.rating = this.article.rating
          console.log(this.article)
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  async mounted() {
    const { id } = this.$route.params
    this.id = id
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getArticle()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style>

</style>