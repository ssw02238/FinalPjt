<template>
  <div class="createArticle container" style="border: 1px solid black;">
    <div class="mb-5">
      <span>내용: </span>
      <input type="text" v-model.trim="content" @keyup.enter="createComment"> <br>
    </div>
    <div class="mb-5">
      <span>별점: </span>
      <input placeholder="숫자를 입력하세요" type="text" v-model.trim="rating" @keyup.enter="createComment"> <br> 
    </div>
    <button @click="createComment" class="btn btn-danger mb-3">작성하기</button>

    <div v-for="(movieComment, idx) in movieComments" :key="idx">
      <span>{{ movieComment.content }}</span>
      <span>{{ movieComment.rating }}</span>
    </div>
  </div>
</template>

<script>
import axios from'axios'

export default {
  name: 'MovieComment',
  data: function () {
    return {
      content: null,
      rating: null,
      movieComments: [],
    }
  },
  methods: {
    setToken: function () {
      const token = localStorage.getItem('jwt')
      const config = {
          Authorization: `JWT ${token}`
      }
      return config
    },
    createComment: function () {
      const CommentItem = {
        content: this.content,
        rating: this.rating,
      }

      if (CommentItem.content) {
        axios({
          method: 'post',
          url: 'http://127.0.0.1:8000/movies/comments/',
          data: CommentItem,
          headers: this.setToken()
        })
          .then((res) => {
            // console.log(res)
            this.movieComments.push(res)
            // this.$router.push({ name: 'ArticleList' })
          })
          .catch((err) => {
            console.log(err)
          })
        }
    },
    getComments: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/comments',
        headers: this.setToken()
      })
      .then((res) => {
          console.log(res)
          this.movieComments = res.data
          // console.log(this.movieComments)
        })
        .catch((err) => {
          console.log(err)
        })
    }
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getComments()
    } else {
      this.$router.push({name: 'Login'})
    }
  }
}
</script>
<style scoped>

  .get_content {
    width: 40%;
    height: 80px;
  }
</style>