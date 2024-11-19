import { ref, computed } from 'vue'
import { defineStore } from 'pinia'
import axios from 'axios'

export const useAccountStore = defineStore('account', () => {
  const BASE_URL = 'http://127.0.0.1:8000'

  const token = ref(null)
  
  const isLogin = computed(() => {
    if (token.value === null) {
      return false
    } else {
      return true
    }
  })

  // 회원가입 요청 액션
  const signUp = function (payload) {
    const { username, password1, password2, email } = payload

    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/signup/`,
      data: {
        username, password1, password2, email
      }
    })
      .then((response) => {
        console.log(response)
        console.log('회원가입 성공')
      })
      .catch((error) => {
        console.error(error.response.data)
      })
  }

  // 로그인 요청 액션
  const logIn = function (payload) {
    const { username, password } = payload

    axios({
      method: 'post',
      url: `${BASE_URL}/accounts/login/`,
      data: {
        username, password
      }
    })
      .then((response) => {
        console.log(response.data)
        console.log('로그인 성공')
        token.value = response.data.key
      })
      .catch((error) => {
        console.log(error)
      })
  }
  
  return { BASE_URL, signUp, logIn, token, isLogin }
}, { persist: true })