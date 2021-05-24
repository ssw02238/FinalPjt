<template>
  <div class="container">
    <div class="row">
      <NowMovieLists
      v-for="(now_movie, idx) in nowplaying"
      :key="idx"
      :now_movie="now_movie"/>
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
      data1: [],
      data2: [],
      nowplaying: [],
    }
  },

  async mounted() {
    try {
        const { data } = await movieApi.nowPlaying(3)
        this.data1 = data.results
      }
    catch (error) {
      console.log(error)
    }
    try {
        const { data } = await movieApi.nowPlaying(2)
        this.data2 = data.results
        this.data2 = this.data2.concat(this.data1)

      }
    catch (error) {
      console.log(error)
    }
    try {
        const { data } = await movieApi.nowPlaying(1)
        this.nowplaying = data.results
        this.nowplaying = this.nowplaying.concat(this.data2)
      }
    catch (error) {
      console.log(error)
    }
  },
}
</script>

<style>
@import url("https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@100;300;400&display=swap");
  * {
    color: #ffffff;
  }
  body {
    font-family: "Noto Sans KR", sans-serif;
  }
  #app {
  background-color: rgb(20, 20, 20);

  color: #ffffff;
  min-height: 100vh;
}
</style>