import { createRouter, createWebHistory } from 'vue-router'
import MainView from '@/views/MainView.vue'
import MovieListView from '@/views/MovieListView.vue'
import RecordListView from '@/views/RecordListView.vue'
import CommunityListView from '@/views/CommunityListView.vue'
import LogInView from '@/views/LoginView.vue'
import SignUpView from '@/views/SignUpView.vue'

import { useAccountStore } from '@/stores/account'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Main',
      component: MainView
    },
    {
      path: '/movies',
      name: 'MovieList',
      component: MovieListView
    },
    {
      path: '/records',
      name: 'RecordList',
      component: RecordListView
    },
    {
      path: '/community',
      name: 'CommunityList',
      component: CommunityListView
    },
    {
      path: '/signup',
      name: 'SignUpView',
      component: SignUpView
    },
    {
      path: '/login',
      name: 'LogInView',
      component: LogInView
    }
  ],
})

router.beforeEach((to, from) => {
  const store = useAccountStore()

  // 만약 이동하는 목적지가 커뮤니티 페이지면서 현재 로그인 상태가 아니라면 로그인 페이지로 보냄
  if (to.name === 'CommunityList' && !store.isLogin) {
    window.alert('로그인이 필요합니다.')
    return { name: 'LogInView' }
  }

  // 만약 로그인 사용자가 회원가입 또는 로그인 페이지로 이동하려고 하면 메인 페이지로 보냄
  if ((to.name === 'SignUpView' || to.name === 'LogInView') && (store.isLogin)) {
    window.alert('이미 로그인 되어있습니다.')
    return { name: 'Main'}
  }
})

export default router
