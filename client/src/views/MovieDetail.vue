<template>
  <div class="movie-detail container p-3">
    <div
      class="movie-detail-image" style="margin-top:130px"
      :style="{ backgroundImage: `url(${image(movieDetail.backdrop_path)})`}"
    ></div>
    <div class="movie-content d-flex">
      <div style="">
        <router-link to="/nowplaying"><button class="btn btn-secondary mb-2"> 뒤로 가기 </button></router-link>
         <img v-bind:src="'https://image.tmdb.org/t/p/w500/'+movieDetail.poster_path" class="m-2" alt="movie_poster" style="height:500px;">
      </div>
      <div class="ml-5 w-75 ms-3">
        <span class="movie-title me-2" style="font-size:50px">{{ movieDetail.title }}</span>
        <span style="font-size:25px">({{ movieDetail.release_date.split("-")[0] }})</span>   
        <div class="movie-information-wrapper mt-4 d-flex align-items-center">
          <div class="ml-2 d-flex">
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
        <div class="ms-2">★: {{movieDetail.vote_average}}</div>
        </div>
        <div v-if="movieDetail.overview" class="mt-3" style="max-width:60rem;">
          <h5>{{ movieDetail.overview }}</h5>
          
        </div>
        <div v-else class="mt-3">
          <h5>줄거리가 등록되지 않았습니다!</h5>
        </div>
        <div v-if="movieDetail.videos && movieDetail.videos.results">
          <iframe
          v-if="movieDetail.videos.results[0]"
            class="mt-4"
            :key="movieDetail.videos.results[0].key"
            width="640"
            height="360"
            :src="youtube(movieDetail.videos.results[0].key)"
          >
          </iframe>
          <div v-else class="mt-4">
            <p>해당 영상이 존재하지 않습니다.</p>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import { movieApi } from "../utils/axios";
export default {
  name: 'moviedetail',
  data() {
    return {
      movieDetail: {},
    }
  },
  async mounted() {
    const { id } = this.$route.params
    const { data } = await movieApi.movieDetail(id)
    this.movieDetail = data
  },
  methods: {
    image(img) {
      console.log();
      return `https://image.tmdb.org/t/p/original/${img}`;
    },
    youtube(src) {
      return `https://www.youtube.com/embed/${src}`;
    },
  },
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic+Coding&display=swap');

.movie-detail {
  position: relative;
  font-family: 'Nanum Gothic Coding', monospace;
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
  content: "";
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