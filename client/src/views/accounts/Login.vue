<template>
  <div class="container py-3 w-75" style="border-radius: 1em;">
    <h1 style="font-family: 'Noto Sans KR', sans-serif;" >Login</h1>
    <div>
      <label for="username" class="my-3 me-2" style="font-size:27px">아이디: </label>
      <input type="text" id="username" v-model="credentials.username" style="font-size:25px;color:black;width:150px; height:35px">
    </div>
    <div>
      <label for="password"  class="my-3 me-2" style="font-size:27px">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password" style="font-size:15px;color:black;width:150px; height:35px">
    </div>
    <button @click="login" class="mt-3 p-2" style="font-family: 'Noto Sans KR', sans-serif;;font-size:20px; color:black;border-radius: 0.3em;">로그인</button>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
      },
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
    login: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        data: this.credentials,
      })
        .then(res => {
          console.log(res)
          localStorage.setItem('jwt', res.data.token)
          this.$emit('login')
          this.$router.push({ name: 'Popular' })
        })
        .then(res => {
          console.log(res)
          axios({
            method: 'get',
            url: 'http://127.0.0.1:8000/accounts/profile/',
            headers: this.setToken()
          })
            .then(res => {
              console.log(res.data)
              localStorage.setItem('username', res.data.username)
              localStorage.setItem('user_id', res.data.user_id)
              console.log(res.data.reviews)
              // localStorage.setItem('reviews',  JSON.stringify(res.data.reviews))
              
              console.log(localStorage)
            })
        })
        .catch(err => {
          this.$router.push({ name: 'Signup' })
          console.log(err)
        })
    }
  }
}
</script>
<style scoped>
@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap');


.container div {
    font-family: 'Noto Sans KR', sans-serif;
  }
</style>