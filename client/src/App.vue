<template>
  <div id="app">

    <div id="nav" style="min-width:1250px">
      <span v-if="isLogin" class="p-3">
        <router-link to="/popular" class="mx-3">인기 상영작</router-link> 
        <router-link to="/nowplaying" class="mx-3">현재 상영작</router-link> 
        <router-link :to="{ name: 'ArticleList' }" class="mx-3">한줄평</router-link>
        <router-link :to="{ name: 'MyPage'}" class="mx-3">마이페이지</router-link> 
        <router-link @click.native="logout" to="#" class="mx-3">로그아웃</router-link>
      </span>
      <span v-else>
        <router-link to="/accounts/login" class="mx-3">로그인</router-link> 
        <router-link to="/accounts/signup" class="mx-3">회원가입</router-link> 
      </span>  
    </div>
    <router-view @login="isLogin=true"/>
  </div>
</template>

<script>
export default {
  name: 'App',
  data: function () {
    return {
      isLogin: false,
      userId: null,
    }
  },
  methods: {
    logout: function () {
      this.isLogin = false
      localStorage.removeItem('jwt')
      localStorage.removeItem('username')
      localStorage.removeItem('user_id')
      localStorage.removeItem('reviews')
      this.$router.push({ name: 'Login' })
    },
  },
  // try-catch로 바꾼 것 
  async mounted() {
    try {
      const token = localStorage.getItem('jwt')
      if (token) {
        this.isLogin = true
        // console.log(localStorage)
        this.userId = localStorage.getItem('user_id')
        // console.log(this.userId)
      }
    }
    catch (error) {
      console.log(error)
    }
  }
}
</script>

<style>
@import url('https://fonts.googleapis.com/css2?family=Yeon+Sung&display=swap');
#app {
  font-family: 'Yeon Sung', cursive;
  text-align: center;
  color: #4495e6;
}

#nav {
  padding: 50px;
  z-index: 999;
}

#nav a {
  /* font-weight: bold; */
  color: #ffffff;
  text-decoration: none;
  font-size: 2.3rem;
}

#nav a:hover{
  color: #967f7f;
}

#nav a.router-link-exact-active {
  color: #7c7c7c;
}

</style>