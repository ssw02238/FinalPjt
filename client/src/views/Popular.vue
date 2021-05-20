<template>
  <div class="container">
    <div class="row">
    <MovieLists
    v-for="(pop_movie, idx) in popular" :key="idx"
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
      popular: {},
    }
  },
  async mounted() {
  try {
    const { data } = await movieApi.popular()
    console.log(data.results)
    this.popular = data.results
    } catch (error) {
      console.log(error)
    }
  }, 
}
</script>

<style>

</style>