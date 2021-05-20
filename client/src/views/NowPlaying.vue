<template>
  <div class="container">
    <div class="row">
      <NowMovieLists
      v-for="(now_movie, idx) in nowplaying"
      :key="idx"
      :now_movie="now_movie"
      />
    </div>
  </div>
</template>

<script>
import NowMovieLists from "@/components/NowMovieLists"
import { movieApi } from "../utils/axios"

export default {
  name: 'nowplaying',
  components: {
    NowMovieLists,
  },
  data: function () {
    return {
      nowplaying: {},
    }
  },

  async mounted() {
    try {
      const { data } = await movieApi.nowPlaying()
      this.nowplaying = data.results
    } catch (error) {
      console.log(error)
    }
  },
}
</script>

<style>

</style>