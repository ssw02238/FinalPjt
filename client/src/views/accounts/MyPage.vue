<template>
  <div>
    ad
  </div>
</template>

<script>
export default {
  name: 'MyPage',
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
    
  },
  // async mounted() {
  //   const { id } = this.$route.params
  //   this.id = id
  // },
  created: function () {
    if (localStorage.getItem('jwt')) {
      console.log()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>

<style>

</style>