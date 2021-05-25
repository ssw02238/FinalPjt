<template>
  <div></div>
</template>

<script>
import axios from 'axios'

export default {
  name: MyPage,
  data: function () {
    return {
      person: null,
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
    getProfile: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/accounts/profile',
        headers: this.setToken()
      })
        .then((res) => {
          console.log(res)
          this.person = res
        })
        .catch((err) => {
          console.log(err)
        })
    },
  },
  // async mounted() {
  //   const { id } = this.$route.params
  //   this.id = id
  // },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getProfile()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style>

</style>