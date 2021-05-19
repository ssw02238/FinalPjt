import axios from "axios"

const request = axios.create({
  baseURL: "https://api.themoviedb.org/3/",
  params: {
    api_key: "80ced8591ed61ab4a22df20840478047",
    language: "ko-KR",
  },
})
// popular, latest, Detail -> similar, random, search 
export const movieApi = {
  popular: () => request.get("movie/popular"),
  latest: () => request.get("movie/latest"),
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