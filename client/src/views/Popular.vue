<template>
  <div>
    <button @click="movieList">get popular</button>

  </div>
</template>

<script>
import { movieApi } from "../utils/axios"
import request from "../utils/axios"

export default {
  name: 'popular',
  data: function () {
    return {
      popular: {},
      url: {},
    }
  },
  methods: {
    movieList: function () {
      this.popular = movieApi.popular
      this.url = request
      console.log(movieApi.popular)
      console.log(movieApi)

    }
  }
}
</script>

<style>

</style>