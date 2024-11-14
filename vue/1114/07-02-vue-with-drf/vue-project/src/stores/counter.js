import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'
import { useRoute } from 'vue-router'

export const useCounterStore = defineStore('counter', () => {
  const articles = ref([])
  const API_URL = 'http://127.0.0.1:8000'

  const token = ref(null)
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // DRF로 전체 게시글 요청을 보내고 응답을 받아 articles에 저장하는 함수
  const getArticles = function () {
    axios({
      method: 'get',
      url: `${API_URL}/api/v1/articles/`,
      headers: {
        Authorization: `Token ${token.value}`
      }
    })
      .then((res) => {
        // console.log(res.data)
        articles.value = res.data
      })
      .catch((err) => {
        console.log(err)
      })
  }

  // 회원가입 요청 액션
  const signUp = function (payload) {
    // const username = payload.username
    // const password1 = payload.password1
    // const password2 = payload.password2
    const { username, password1, password2 } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/signup/`,
      data: {
        // username: username,
        // password1: password1,
        // password2: password2,
        username, password1, password2
      }
    })
      .then((response) => {
        console.log(response)
        console.log('회원가입 성공')
      })
      .catch((error) => {
        console.log(error)
      })
  }

  // 로그인 요청 액션
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${API_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        // console.log(response.data)
        // console.log('로그인 성공')
        token.value = response.data.key
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  return { articles, API_URL, getArticles, signUp, logIn, token, isLogin }
}, { persist: true })
