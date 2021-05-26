<template>
  <div class="container py-3 w-75">
    <h1 style="font-family: 'Noto Sans KR', sans-serif">Signup</h1>
    <p style="font-family: 'Noto Sans KR', sans-serif;font-size: 20px; color:red;">* 회원가입을 우선 진행해주세요 *</p>
    <div>
      <label for="username" class="my-3 me-2" style="font-size:27px">사용자 이름: </label>
      <input type="text" id="username" v-model="credentials.username"  style="color:black;width:150px; height:35px; font-size:25px;">
    </div>
    <div>
      <label for="password" class="my-3 me-2" style="font-size:27px">비밀번호: </label>
      <input type="password" id="password" v-model="credentials.password"  style="color:black;width:150px; height:35px;font-size:15px">
    </div>
    <div>
      <label for="passwordConfirmation" class="my-3 me-2" style="font-size:27px">비밀번호 확인: </label>
      <input type="password" id="passwordConfirmation" v-model="credentials.passwordConfirmation"  style="color:black;width:150px; height:35px;font-size:15px">
    </div>
    <button @click="signup(credentials)" class="mt-5 p-2" style="font-family: 'Noto Sans KR', sans-serif;font-size:20px; color:black; border-radius: 0.3em;">회원가입</button>
  </div>
</template>

<script>
import axios from 'axios'

// const SERVER_URL = process.env.VUE_APP_SERVER_URL

export default {
  name: 'Signup',
  data: function () {
    return {
      credentials: {
        username: null,
        password: null,
        passwordConfirmation: null,
      }
    }
  },
  methods: {
    signup: function () {
      axios({
        method: 'post',
        url: 'http://127.0.0.1:8000/accounts/signup/',
        data: this.credentials,
      })
        .then(res => {
          // 바로 로그인된 상태로 popular 페이지 나오게 
          console.log(res)
          // localStorage.setItem('jwt', res.data.token)
          // this.$emit('login')
          this.$router.push({ name: 'Login' })
        })
        .catch(err => {
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