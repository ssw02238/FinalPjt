<template>
<div class="col-lg-3 col-sm-6 mb-4">
  <div class="card">
    <div @click="goDetail(pop_movie.id)" v-if="pop_movie">
      <img v-bind:src="'https://image.tmdb.org/t/p/w500/'+pop_movie.poster_path" class="img-fluid" alt="movie_poster" style="height: 400px">
      <div class="card-body" style="height: 150px">
        <h5 class="card-title"><strong>{{ pop_movie.title }} </strong></h5>
        <h6>{{ pop_movie.release_date }}</h6>
        <!-- font awesome 사용
        <p><i class="fas fa-cloud-sun-rain"></i></p>--> 
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'MovieLists',
  props: {
    pop_movie: {
      type: Object
    }
  },
  methods: {
    goDetail(id) {
      this.$router.push(`moviedetail/${id}`)
    }
  }
}
</script>

<style>
</style>