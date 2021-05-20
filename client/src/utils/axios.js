import axios from "axios"


const API_KEY = process.env.VUE_APP_TMDB_API_KEY
const request = axios.create({
  baseURL: "https://api.themoviedb.org/3/",
  params: {
    api_key: API_KEY,
    language: "ko-KR",
  },
})
// popular, nowplaying, Detail -> similar, random, search 
export const movieApi = {
  popular: () => request.get("movie/popular"),
  nowPlaying: (num) => request.get("movie/now_playing", {
    params: {
      page: num,
    }
  }),
  movieDetail: (id) =>
    request.get(`movie/${id}`, {
      params: { append_to_response: "videos" },
    }),
  search: (keyword) =>
    request.get("search/movie", {
      params: {
        query: keyword,
      },
    }),
}