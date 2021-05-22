<template>
  
  <div class="createArticle container" style="border: 1px solid black;">
    <select v-model="selected">
      <option disabled value="">Please select one</option>
      <option v-for="(movie, idx) in movies"
      :key="idx"
      :value="movie.id"
      >
      {{ movie.title }}
      </option>
    </select>
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
    <button @click="createArticle" class="btn btn-danger mb-3" >작성하기</button> 
    <!-- Button trigger modal -->
<!-- <button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal">
  Launch demo modal
</button> -->

<!-- Modal -->
<!-- <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">Modal title</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        'asdasd'
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Save changes</button>
      </div>
    </div>
  </div>
</div> -->

    

    <!-- <div id="carouselExampleControls" class="carousel slide" data-bs-ride="carousel">
    <div class="carousel-inner">
      <div class="carousel-item active">
        <img src="https://image.tmdb.org/t/p/w500/cmzfmGxXxSF716SYBW6seMgxMWE.jpg" class="d-block w-100" alt="">
      </div>
      <div class="carousel-item">
        <img src="https://image.tmdb.org/t/p/w500/cmzfmGxXxSF716SYBW6seMgxMWE.jpg" class="d-block w-100" alt="">
      </div>
      <div class="carousel-item">
        <img src="https://image.tmdb.org/t/p/w500/cmzfmGxXxSF716SYBW6seMgxMWE.jpg" class="d-block w-100" alt="">
      </div>
    </div>
    <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="prev">
      <span class="carousel-control-prev-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Previous</span>
    </button>
    <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleControls" data-bs-slide="next">
      <span class="carousel-control-next-icon" aria-hidden="true"></span>
      <span class="visually-hidden">Next</span>
    </button> -->

</div>


</template>

<script>
import axios from'axios'
import { movieApi } from "@/utils/axios"

export default {
  name: 'CreateArticle',
  data: function () {
    return {
      title: null,
      content: null,
      rating: null,
      movies: [],
      selected: '',
      similars: [],
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

            console.log(this.selected)
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
    async getSimilar() {
      try{
        const {data} = await movieApi.movieSimilar(this.selected)
        this.similars = data.results
        console.log(this.similars)
      }
      catch (error) {
        console.log(error)
      }
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

  .example-slide {
  align-items: center;
  background-color: #666;
  color: #999;
  display: flex;
  font-size: 1.5rem;
  justify-content: center;
  min-height: 10rem;
 } 
</style>