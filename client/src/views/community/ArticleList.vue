<template>
  <div class="container">
    <div>
      <div style="font-size:25px;font-family: 'Noto Sans KR', sans-serif;float:left">현재 상영작 리뷰 확인하기</div>
      <router-link :to="{ name: 'CreateArticle' }"><button class="btn btn-warning m-2" style="font-family:'Noto Sans KR', sans-serif;font-size:20px; display:inline-block;float:right">새 글 작성하기</button></router-link> 
    </div>
    <table class="table" style="font-size:18px; border-radius: 1em;background-color:#e0e8ed;">
      <thead>
        <tr>
          <th scope="col">Rank</th>
          <th scope="col">영화 제목</th>
          <th scope="col">한줄평</th>
          <th scope="col">☆</th>
        </tr>
      </thead>
      <tbody v-for="(article, idx) in paginatedArticles" :key="idx" @click="goDetail(article.movieId)" style="background-color:#9d9b9a;">
        <tr>
          <th>{{ 10*(page-1) + idx+1 }}</th>
          <th>{{ article.movietitle }}</th>
          <th>{{ article.content }}</th>
          <th v-if="article.rating === 5">★★★★★</th>
          <th v-else-if="4 <= article.rating">★★★★☆</th>
          <th v-else-if="3 <= article.rating">★★★☆☆</th>
          <th v-else-if="2 <= article.rating">★★☆☆☆</th>
          <th v-else-if="1 <= article.rating">★☆☆☆☆</th>
          <th v-else></th>
        </tr>
      </tbody>
    </table>
      <el-pagination
        class="text-center mb-4 d-flex align-items-center justify-content-center "
        background
        :page-size="10"
        layout="prev, pager, next"
        :total="totalPage"
        @current-change="movePage">
      </el-pagination>

  </div>
</template>

<script>
import axios from 'axios'


export default {
  name: 'ArticleList',
  data: function () {
    return {
      articles: [],
      // id: null,
      page: 1,
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
    getArticles: function () {
      axios({
        method: 'get',
        url: 'http://127.0.0.1:8000/movies/articles',
        headers: this.setToken()
      })
        .then((res) => {
          this.articles = res.data
        })
        .catch((err) => {
          console.log(err)
        })
    },
    
    goDetail(id) {
      this.$router.push({ name: 'MovieDetail',  params: {id: id }})
    },
    movePage: function (page) {
      this.page = page
    },
  },
  created: function () {
    if (localStorage.getItem('jwt')) {
      this.getArticles()

    } else {
      this.$router.push({name: 'Login'})
    }
  },
  computed: { 
    paginatedArticles: function () {
      const start = (this.page - 1) * 10, // 1페이지면 0~10
            end = start + 10;
      return this.articles.slice(start, end);
    },
    totalPage: function () {
      console.log(this.paginatedArticles)
      return this.articles.length
    }
  }
}
</script>

<style scoped>

@import url('https://fonts.googleapis.com/css2?family=Noto+Sans+KR:wght@300&display=swap');

td, th {
  color: black;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 20px;
}
th button {
  color: white;
  background: #5a6160;
}
td span {
  color: black;

}
</style>