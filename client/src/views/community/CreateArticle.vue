<template>
  <div>
    <input type="text" v-model.trim="title" @keyup.enter="createArticle">
    <input type="text" v-model.trim="content" @keyup.enter="createArticle">
    <input type="text" v-model.trim="rating" @keyup.enter="createArticle">
    <button @click="createArticle">+</button>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateArticle',
  data: function () {
    return {
      title: null,
      content: null,
      rating: null,
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${token}`
      }
      return config
    },
    createArticle: function () {
      const ArticleItem = {
        title: this.title,
        content: this.content,
        rating: this.rating,
      }

      if (ArticleItem.title) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/movies/articles/',
          data: ArticleItem,
          headers: this.setToken()
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'ArticleList' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
  }
}
</script>
