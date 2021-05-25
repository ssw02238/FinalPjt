<template>
  <div class="container">
    <div>
      <span style="font-size:60px"> "{{userName}}" </span> 
      <span style="font-size:45px"> 님의 My page </span>
        <table class="table" style="font-size:20px; border-radius: 1em;background-color:#ddcfd5;">
          <thead>
            <tr>
              <th scope="col">Rank</th>
              <th scope="col">영화 제목</th>
              <th scope="col">글 제목</th>
              <th scope="col">☆☆☆☆☆</th>
            </tr>
          </thead>
          <tbody v-for="(review, idx) in reviews" :key="idx" @click="goDetail(review.movieId)">
            <tr>
              <th>{{ idx+1 }}</th>
              <th>{{review.movietitle}}</th>
              <th>{{review.title}}</th>
              <th>{{review.rating}}</th>
            </tr>
          </tbody>
        </table>
      <hr>
      <button class="btn btn-warning my-3" style="font-size:30px" @click="getRecommend">추천 영화 확인!</button>
      <!-- recommendation -->
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
          for (var cnt in this.reviews) {
            if (this.reviews[cnt].rating >= 3) {
              this.goodMovies.push(this.reviews[cnt].movieId)
          } else {
            continue
          }
        }
        })
        
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
          console.log(this.recommend_movie)
        }
        catch (error) {
          console.log(error)
        }
    },
    goDetail(id) {
      this.$router.push({ name: 'MovieDetail',  params: {id: id }})
    },
  },
  mounted: async function () {
    if (localStorage.getItem('jwt')) {
      this.getReviews()
      // goodMovie ID 담기

    } else {
      this.$router.push({name: 'Login'})
    }
  },
}
</script>

<style>
</style>

