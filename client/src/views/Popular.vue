<template>
  <div class="container">
    <div class="row">
    <MovieLists
    v-for="(pop_movie, idx) in popular" 
    :key="idx"
    :pop_movie="pop_movie"/>
  </div>
</div>
</template>

<script>
import MovieLists from "@/components/MovieLists"
import { movieApi } from "../utils/axios"

export default {
  name: 'Popular',
  components: {
    MovieLists
  },
  data: function () {
    return {
      pop1: [],
      pop2: [],
      popular: [],
    }
  },
  async mounted() {
    try {
          const { data } = await movieApi.popular(3)
          this.pop1 = data.results
        }
    catch (error) {
      console.log(error)
    }
    try {
        const { data } = await movieApi.popular(2)
        this.pop2 = data.results
        this.pop2 = this.pop2.concat(this.pop1)

      }
    catch (error) {
      console.log(error)
    }
    try {
        const { data } = await movieApi.popular(1)
        this.popular = data.results
        this.popular = this.popular.concat(this.pop2)
      }
    catch (error) {
      console.log(error)
    }
  },
}
</script>

<style>

  * {
    color: #ffffff;
  }
  #app {
  background-color: rgb(20, 20, 20);

  color: #ffffff;
  min-height: 100vh;
}
</style>