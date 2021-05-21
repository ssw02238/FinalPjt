<template>
  <div class="movie-detail container my-4 py-3" style="background-color:#cbedf0;">
    <div class="movie-content d-flex">
      <img v-bind:src="'https://image.tmdb.org/t/p/w500/'+movieDetail.poster_path" class="m-2" alt="movie_poster" style="height:500px; width:55%">
      <div class="m-5" style="width:60%;">
        <h1>{{ movieDetail.title }} / {{ genre.name }}</h1> 
        <h3>평점: {{ movieDetail.vote_average }}</h3>
        <br>
        <div v-if="movieDetail.overview">
          <h5>{{ movieDetail.overview }}</h5>
        </div>
        <div v-else>
          <h5>줄거리가 등록되지 않았습니다!</h5>
        </div>
      </div>
    </div>
    <!-- movieDetail.videos에 영상이 있는 경우에만 데이터 받아오기-->
    <div v-if="movieDetail.videos && movieDetail.videos.results" class="text-align-center">
      <iframe
        v-if="movieDetail.videos.results[0]"
          :key="movieDetail.videos.results[0].key"
          class="mt-3"
          width="70%"
          height="400px"
          :src="youtube(movieDetail.videos.results[0].key)"
        >
        </iframe>
      <div v-else class="mt-4">
        <p>해당 영상이 존재하지 않습니다.</p>
      </div>
    </div>
  </div>
</template>

<script>
import { movieApi } from '../utils/axios'

export default {
  name: 'moviedetail',
  data() {
    return {
      movieDetail: {},
      genre: '',
    }
  },
  async mounted() {
    const { id } = this.$route.params
    const { data } = await movieApi.movieDetail(id)
    this.movieDetail = data
    this.genre = this.movieDetail.genres[0]
  },
  methods: {
    // detail에 youtube 정보가 있는게 있고 없는게 있음 
    youtube(src) {
      return `https://www.youtube.com/embed/${src}`
    }
  }
}

</script>

<style>
</style>