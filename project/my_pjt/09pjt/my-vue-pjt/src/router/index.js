import { createRouter, createWebHistory } from 'vue-router'
import HomeView from '@/views/HomeView.vue'
import MovieListView from '@/views/MovieListView.vue'
import MovieDetailView from '@/views/MovieDetailView.vue'
import ReviewSearchView from '@/views/ReviewSearchView.vue'
import RecommendedView from '@/views/RecommendedView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'Home',
      component: HomeView,
    },
    {
      path: '/movies',
      name: 'MovieList',
      component: MovieListView,
    },
    {
      path: '/:movieId',
      name: 'MovieDetail',
      component: MovieDetailView,
    },
    {
      path: '/review-search',
      name: 'ReviewSearch',
      component: ReviewSearchView,
    },
    {
      path: '/recommended',
      name: 'Recommended',
      component: RecommendedView,
    },
  ],
})

export default router
