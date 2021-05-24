<template>
  <div class="createArticle container py-3" style="border-radius: 1em;background-color:#5f5446; border: 1px solid black;font-family: 'Gothic A1', sans-serif;">
    <label for="movie-select" class="me-2 mt-3">Choose a Movie:</label>
    <select v-model="movietitle" style="color:black; height:45px; width:70%">
      <option disabled value="" style="color:black">Please select one</option>
      <option v-for="(movie, idx) in movies"
      :key="idx"
      :value="[movie.id, movie.title]"
      style="color:black; width:70%;"
      >
      {{ movie.title }}
      </option>
    </select>
    <div class="mb-5">
      <span>제목: </span>
      <input class="mt-5" type="text" v-model.trim="title" style="width:70%;"> <br>
    </div>
    <div class="mb-5">
      <span>내용: </span>
      <input type="text" class="get_content" v-model.trim="content" style="width:70%; height:300px"> <br>
    </div>
    <div class="mb-5">
      <span>별점: </span>
      <input placeholder="5점 만점" type="number" min='0' max='5' v-model.trim="rating" @keyup.enter="createArticle" style="width:23%"> <br> 
    </div>
    <button @click="createArticle" class="btn btn-secondary mb-3" style="color:black; font-size:20px">작성하기</button> 
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
      movietitle: null,
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
        movietitle: this.movietitle[1],
        movieId: this.movietitle[0]
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
            this.$router.push({ name: 'ArticleList', params: { id: this.movietitle[0] }})

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
    },
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
  input {
    color:black;
  }
  .createArticle {
    font-size: 1.8rem;
  }
</style>