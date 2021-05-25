<template>
  <div class="container">
    <div>
      <span style="font-size:60px"> "{{userName}}" </span> 
      <span style="font-size:45px"> 님의 My page </span>
      <div v-for="(review, idx) in reviews" :key="idx">
        {{review.movietitle}}
        {{review.title}}
        {{review.rating}}
      </div>
    </div>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'MyPage',
  data: function () {
    return {
      userName: null,
      reviews: null,
    }
  },
  methods: {
    setToken: function () {
      const jwtToken = localStorage.getItem('jwt')
      const config = {
        Authorization: `JWT ${jwtToken}`
      }
    
      return config 
    },
    getReviews: function () {
      axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/accounts/profile/',
            headers: this.setToken()
          })
            .then(res => {
              console.log(res.data.reviews)
              localStorage.setItem('reviews', JSON.stringify(res.data.reviews))
              console.log(localStorage)
            })
    }
  },
  mounted: function () {
    if (localStorage.getItem('jwt')) {
      this.getReviews()
      this.userName = localStorage.getItem('username')
      this.reviews = JSON.parse(localStorage.getItem('reviews'))
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style>
</style>