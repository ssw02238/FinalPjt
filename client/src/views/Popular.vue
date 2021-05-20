<template>
  <div>
    <button @click="get_popular">get popular</button>

  </div>
</template>

<script>
import { movieApi } from "../utils/axios"

export default {
  name: 'popular',
  data: function () {
    return {
      popular: {},
    }
  },
  methods: {
    async get_popular() {
      try {
        const { data } = await movieApi.popular()
        console.log(data.results)
      } catch (error) {
        console.log(error)
      }
    }
  },
}
</script>

<style>

</style>