<template>
  <div class="container p-4 w-60" style="font-size:30px; border:solid #6c6367 1px; background-color:#483946">
    <p style="font-family: 'Gothic A1', sans-serif;">글 제목: {{ title }} / 영화: {{ article.movietitle }} </p>
    <p style="font-family: 'Gothic A1', sans-serif;">내용: {{ content }}</p>
    <p style="font-family: 'Gothic A1', sans-serif;">별점: {{ rating }}</p>
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

<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Gothic+A1:wght@200&display=swap');

</style>