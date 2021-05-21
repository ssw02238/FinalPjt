<template>
  <div class="createArticle container" style="border: 1px solid black;">
    <div class="mb-5">
      <span>제목: </span>
      <input class="mt-5" type="text" v-model.trim="title" @keyup.enter="createArticle"> <br>
    </div>
    <div class="mb-5">
      <span>내용: </span>
      <input class="get_content" type="text" v-model.trim="content" @keyup.enter="createArticle"> <br>
    </div>
    <div class="mb-5">
      <span>별점: </span>
      <input placeholder="숫자" type="number" min='0' max='5' v-model.trim="rating" @keyup.enter="createArticle"> <br> 
    </div>
    <button @click="createArticle" class="btn btn-danger mb-3">작성하기</button>
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
      movies: [],
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
    getMovies: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/movieList',
        headers: this.setToken()
      })
        .then((res) => {
          this.movies = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
    created: function () {
      if (localStorage.getItem('jwt')) {
        this.getMovies()
      } else {
        this.$router.push({name: 'Login'})
      }
  }
}
</script>
<style scoped>

  .get_content {
    width: 40%;
    height: 80px;
  }
</style>
