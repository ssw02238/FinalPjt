<template>
  <div class="container">
    <div>
      <span style="font-size:35px;font-family: 'Noto Sans KR', sans-serif;"> {{userName}}님의 My page </span>
      <hr>
        <table class="table" style="font-size:20px;border-radius: 1em;background-color:#e0e8ed;">
          <thead>
            <tr>
              <th scope="col">Rank</th>
              <th scope="col">영화 제목</th>
              <th scope="col">한줄평</th>
              <th scope="col">☆</th>
              <th scope="col"> 삭제</th>
            </tr>
          </thead>
          <tbody v-for="(review, idx) in reviews" :key="idx" @click="goDetail(review.movieId)" style="background-color:#9d9b9a;">
            <tr>

              <th>{{ idx+1 }}</th>
              <th>{{review.movietitle}}</th>
              <th>{{review.content}}</th>
              <th v-if="review.rating === 5">★★★★★</th>
              <th v-else-if="4 <= review.rating">★★★★☆</th>
              <th v-else-if="3 <= review.rating">★★★☆☆</th>
              <th v-else-if="2 <= review.rating">★★☆☆☆</th>
              <th v-else-if="1 <= review.rating">★☆☆☆☆</th>
              <th v-else></th>
              <th><button @click="deleteReview(review)">X</button></th>
            </tr>
          </tbody>
        </table>
      <hr>
      <button class="btn btn-warning my-3" style="font-size:25px;font-family: 'Noto Sans KR', sans-serif;" @click="getRecommend">추천 영화 확인!</button>
    </div>
      <!-- recommendation -->
      <div class="container">
        <div v-if="recommend_movie" class="row">
          <div v-for="(movie, idx) in recommend_movie" :key="idx" class="mx-2 col-sm">
            <img @click="goDetail(movie.id)" v-bind:src="'https://image.tmdb.org/t/p/w500/'+movie.poster_path" class="m-2" alt="movie_poster" style="height:500px;">
            <h3 style="font-size:20px;  font-family: 'Noto Sans KR', sans-serif;">{{ movie.title }} </h3>
          </div>
        </div>
      </div>
  </div>
</template>

<script>
import axios from 'axios'
import _ from 'lodash'
import { movieApi } from "../../utils/axios";

export default {
  name: 'MyPage',
  data: function () {
    return {
      userName: null,
      reviews: null,
      //평점 4점 이상인 영화 ID
      goodMovies: [],
      // 추천 영화 작 (각 goodMovies에서 추출)
      recommendation: [],
      // random으로 넣을 영화 
      recommend_movie: [],
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
    getReviews: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/profile/',
        headers: this.setToken()
      })
        .then(res => {
          localStorage.setItem('reviews', JSON.stringify(res.data.reviews))
          this.userName = localStorage.getItem('username')
          this.reviews = JSON.parse(localStorage.getItem('reviews'))
          // goodMovie ID 담기
          for (var cnt in this.reviews) {
              if (this.reviews[cnt].rating >= 4) {
                this.goodMovies.push(this.reviews[cnt].movieId)
              } else {
                continue
              }
            }
        })
    },
    deleteReview: function (review) {
      axios({
        method: 'delete',
        url: `http://127.0.0.1:8000/movies/${review.id}/`,
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.getReviews() // 삭제된거 실시간 렌더링 
          this.$router.push({ name: 'MyPage'})
        })
        .catch((err) => {
          console.log(err)
        })
    },
    goDetail(id) {
      this.$router.push({ name: 'MovieDetail',  params: {id: id }})
    },
    // goodMovie 안에 Id를 기준으로 영화 추천 리스트 받기 
    async getRecommend () {
        try{
          for (var Id in this.goodMovies) {
            const {data} = await movieApi.movieSimilar(this.goodMovies[Id])
            this.recommendation = this.recommendation.concat(data.results)
          }
          // 랜덤 추천 영화 넣어주기 
          this.recommend_movie = _.sampleSize(this.recommendation, 5)
        }
        catch (error) {
          console.log(error)
        }
    },
  },
  mounted: async function () {
    if (localStorage.getItem('jwt')) {
      this.getReviews()

    } else {
      this.$router.push({name: 'Login'})
    }
  },
}
</script>


<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap');
th, td {
  color: black;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px
}
th button {
  color: white;
  background: #5a6160;
}

</style>

