<template>
<div class="col-lg-3 col-sm-6 mb-4" style="background-color:black;border-radius: 1em;">
  <div class="card my-2"  style="background-color:black;">
    <div class="card-imgTitle" @click="goDetail(pop_movie.id)" v-if="pop_movie" title="상세정보 확인!">
      <img v-bind:src="'https://image.tmdb.org/t/p/w500/'+pop_movie.poster_path" class="img-fluid" alt="movie_poster" style="height: 400px">
      <div class="card-body">
        <h5 class="card-title"><strong>☆ {{ pop_movie.vote_average }} </strong></h5>
        <h6 class="mt-4" style="font-size:20px">{{ pop_movie.title }}</h6>
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
@import url('https://fonts.googleapis.com/css2?family=Nanum+Gothic+Coding&display=swap');
.card {
  background-color: rgb(20, 20, 20);
  min-height: 40vh;
}
.card-body {
  min-height: 10vh;
  font-family: 'Nanum Gothic Coding', monospace;
}
.card-imgTitle:hover {
  opacity: 0.5;
  cursor: pointer;
}
</style>