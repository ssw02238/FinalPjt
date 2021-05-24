<template>
<div class="col-lg-3 col-sm-6 mb-4" style="background-color:black;border-radius: 1em;">
  <div class="card my-2" style="background-color:black;">
    <div class="card-imgTitle" @click="goDetail(now_movie.id)" v-if="now_movie" title="상세정보 확인을 위해 클릭해보세요!">
      <img v-bind:src="'https://image.tmdb.org/t/p/w500/'+now_movie.poster_path" class="img-fluid" alt="movie_poster" style="height: 400px">
      <div class="card-body">
        <h5 class="card-title"><strong>☆ {{ now_movie.vote_average }}</strong></h5>
        <h6 class="mt-4" style="font-size:20px">{{ now_movie.title }}</h6>
      </div>
    </div>
  </div>
</div>
</template>

<script>
export default {
  name: 'NowMovieLists',
  props: {
    now_movie: {
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
.card {
  background-color: rgb(20, 20, 20);
  min-height: 40vh;
}
.card-body {
  min-height: 20vh;
  max-height: 20vh;
}
.card-imgTitle:hover {
  opacity: 0.5;
  cursor: pointer;
}

</style>