<template>
  <div class="movie-detail p-3" style="margin-left:15%; margin-right:15%;">
    <div
      class="movie-detail-image"
      :style="{ backgroundImage: `url(${image(movieDetail.backdrop_path)})`}"
    ></div>
    <div class="movie-content d-flex flex-column">
      <div class="d-flex align-items-center justify-content-center">
      <!-- 영화 포스터입니다@@@ -->
        <img v-bind:src="'https://image.tmdb.org/t/p/w500/'+movieDetail.poster_path" class="m-2 me-5 rounded-3" alt="movie_poster" style="height:500px">
        <!-- 여기서 부터 유튭 비디오 입니다###### -->
        <div v-if="movieDetail.videos && movieDetail.videos.results">
          <div>
            <iframe
            v-if="movieDetail.videos.results[0]"
              :key="movieDetail.videos.results[0].key"
              width="650"
              height="400"
              :src="youtube(movieDetail.videos.results[0].key)"
              align="left"
              class="ms-5 rounded-3"
            >
            </iframe>
            <!-- <div v-else class="mt-5">
              <p style="margin-top:100px; font-size: 30px">예고편이 존재하지 않습니다.</p>
            </div> -->
          </div>
        </div>
      </div>
      <!-- 영화 내용입니다@@@@@@@ -->
      <div class="p-4">
        <div class="ml-5 ms-3">
          <div align="left">
            <span class="movie-title me-2" style="font-size:50px">{{ movieDetail.title }}</span>
            <span style="font-size:25px">({{ date }})</span>
          </div>   
          <div class="movie-information-wrapper mt-4 d-flex align-items-center">
            <div class="ml-2  d-flex">
              <div class="me-3"> 개요: </div>
              <div
                class="genres me-2"
                v-for="genre in movieDetail.genres"
                :key="genre.id"
              >
                {{ genre.name }}
              </div>
            </div>
          <span class="me-3">/</span>
          <div>러닝타임: {{ movieDetail.runtime }} 분 / </div>
          <div class="ms-2">
            <span style="color:yellow;">★</span> :{{movieDetail.vote_average}}
          </div>
          </div>
          <div v-if="movieDetail.overview" class="mt-3" align="left">
            <p>{{ movieDetail.overview }}</p>
          </div>
          <div v-else class="mt-5">
            <h5 style="margin-top:150px; font-size: 30px">줄거리가 등록되지 않았습니다!</h5>
          </div>
        </div>
        <!-- 댓글##################### -->
        <div class="comments m-5 px-5" style="width:640">
          <p class="p-2" style="font-size:36px; color:white;">{{choose}}</p>
          <div v-for="(article, idx) in paginatedArticles" :key="idx">
            <p v-if="article.movieId === id" style="color:white; font-size: 20px">
              {{ article.content }} / <span style="color:yellow;">★</span> {{ article.rating }}
            </p>
          </div>
          <el-pagination
            class="text-center mb-4"
            background
            :page-size="5"
            layout="prev, pager, next"
            :total="totalPage"
            @current-change="movePage">
          </el-pagination>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'
import { movieApi } from "../utils/axios";
export default {
  name: 'moviedetail',
  data() {
    return {
      movieDetail: {},
      comments: [],
      articles: null,
      id: '',
      date: null,
      weather: [0, 0, 0],
      choose: '',
      page: 1,
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getArticle()
    } else {
      this.$router.push({name: 'Login'})
    }
  },
  
  async mounted() {
    const { id } = this.$route.params
    this.id = id
    const { data } = await movieApi.movieDetail(id)
    this.movieDetail = data
    this.date = this.movieDetail.release_date.split('-')[0]
  },
  methods: {
    image(img) {
      return `https://image.tmdb.org/t/p/original/${img}`;
    },
    youtube(src) {
      return `https://www.youtube.com/embed/${src}`;
    },
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
          this.articles = res.data
          this.getWeather()
        })
        .catch((err) => {
          console.log(err)
        })
    },
    getWeather: function () {
      for (var cnt in this.articles) {
        if (this.articles[cnt].movieId == this.id) {
          if (this.articles[cnt].weather == '맑음') {
            this.weather[0] += 1
          } else if (this.articles[cnt].weather == '흐림') {
            this.weather[1] += 1
          } else {
            this.weather[2] += 1
          }
        }
      }
      // 최댓 등장 횟수
      this.choose = (Math.max.apply(null, this.weather))
      if (this.choose != 0) {
        if (this.weather.indexOf(this.choose) == '0') {
          // 문구
          this.choose = '화창한 날씨에 함께 할 영화'
        } else if (this.weather.indexOf(this.choose) == '1') {
          this.choose = '흐리고 울적한 날에 딱 맞는 영화'
        } else {
          this.choose = '천둥 번개처럼 긴장감있는 영화'
        }
      } else {
        this.choose = ''
      }
    },
    movePage: function (page) {
      this.page = page
    }
  },
  computed: { 
    paginatedArticles: function () {
      const start = (this.page - 1) * 5, // 1페이지면 0~5
            end = start + 5;
      const filteredArticles = this.articles.filter((article) => {
        return article.movieId === this.id
        })// articles에서 아이디 맞는거 걸러줌
      return filteredArticles.slice(start, end);
    },
    totalPage: function () {
      const filteredArticles = this.articles.filter((article) => {
        return article.movieId === this.id
      })
      return filteredArticles.length
    }
  }
}
</script>

<style >
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic+Coding&display=swap');

.movie-detail {
  position: relative;
  font-family: 'Noto Sans KR', sans-serif;
  min-width: 1250px;

}
.movie-detail-image {
  background-size: cover;
  height: 100vh;
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
}
.movie-detail-image::after {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  min-height: 100vh;
  background-color: rgb(34, 30, 30);
  opacity: 0.7;
  z-index: 1.5;
  content: "";
  margin-top: 0px;
}
.movie-content {
  position: relative;
}
.genres:not(:first-of-type)::before {
  margin-bottom: 4px;
  margin-left: 6px;
  margin-right: 1px;
}
</style>