<template>
  <div>
    <button>moviedetail</button>
    <p>{{ movieDetail.title }}</p>
    <p>{{ genre.name }}</p>
    <p>{{ movieDetail.vote_average }}</p>
    <div v-if="movieDetail.overview">
      <p>{{ movieDetail.overview }}</p>
    </div>
    <div v-else>
      <p>'없어요'</p>
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
  }
}

</script>

<style>

</style>