<template>
  <div class="createArticle container py-3 d-flex flex-column align-items-end" style="border-radius: 1em; border: 5px solid white;font-family: 'Gothic A1', sans-serif; min-width: 1250px;">
    <div class="my-3 w-100 d-flex justify-content-start align-items-center ">
      <label for="movie-select" class="mt-3 w-25">영화 제목</label>
      <select v-model="movietitle" style="color:black; height:45px; width:70%">
        <option disabled style="color:black">Please select one</option>
        <option v-for="(movie, idx) in movies"
        :key="idx"
        :value="[movie.id, movie.title]"
        style="color:black; width:70%;"
        >
        {{ movie.title }}
        </option>
      </select>
    </div>
    <div class="my-3 w-100 d-flex justify-content-start align-items-center ">
      <span class="w-25"> 오늘  </span>
      <!-- <input class="mt-5" type="text" v-model.trim="title" style="width:70%;"> <br> -->
      <select v-model="weather" style="color:black; height:45px; width:70%"><br>
        <option disabled>Open this select menu</option>
        <option value="맑음">맑음</option>
        <option value="흐림">흐림</option>
        <option value="천둥 번개">천둥 번개</option>
      </select>
    </div>
    <div class="my-3 w-100 d-flex justify-content-start align-items-center ">
      <span class="w-25">한줄평 </span>
      <input placeholder="100자 이내로 입력해주세요." type="text" class="get_content" v-model.trim="content" style="width:70%; height:100px"> <br>
    </div>
    <div class="my-3 w-100 d-flex justify-content-start align-items-center ">
      <span class="w-25">별점 </span>
      <input placeholder="5점 만점" type="number" min='0' max='5' v-model.trim="rating" @keyup.enter="createArticle" style="width:23%"> <br> 
    </div>
    <button @click="createArticle" class="btn btn-secondary mb-3" style="color:black; font-size:20px; margin-right: 10%;">작성하기</button> 
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'CreateArticle',
  data: function () {
    return {
      weather: null,
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
        weather: this.weather,
        content: this.content,
        rating: this.rating,
        movietitle: this.movietitle[1],
        movieId: this.movietitle[0]
      }
      if (ArticleItem.weather) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/movies/articles/',
          data: ArticleItem,
          headers: this.setToken()
        })
          .then((res) => {
            console.log(res)
            this.$router.push({ name: 'ArticleList'})

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
  option {
    color:black; 
    width:70%;
  }
</style>