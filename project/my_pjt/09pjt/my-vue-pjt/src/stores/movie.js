import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useMovieStore = defineStore('movie', () => {
  const reviews = ref(null)
  // 영화 공식 예고편 영상 아이디
  const trailerId = ref(null)

  // 리뷰 영상 아이디, 제목
  const videoId = ref(null)
  const videoTitle = ref(null)

  // 리뷰 영상 목록 조회
  const getReview = function (keyword) {
    axios({
      method: 'get',
      url: `https://www.googleapis.com/youtube/v3/search`,
      params: {
        key: 'AIzaSyCDbAwHimnglomV5qpsp2tBrPZcsq2Cpeg',
        q: keyword,
        part: "snippet",
        type: "video",
        fields: "items(id, snippet)",
      }
    })
      .then((response) => {
        console.log(response)
        reviews.value = response.data.items
      })
      .catch((error) => {
        console.log(error)
      })
  }


  return { reviews, getReview, trailerId, videoId, videoTitle }
})
