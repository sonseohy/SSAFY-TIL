<template>
  <div class="container">
    <!-- <form @submit.prevent="searchReview" class="form-container">
      <input type="text" v-model="search">
      <input type="submit" value="검색"> 
    </form> -->
    <form @submit.prevent="searchReview" class="form-container">
        <input type="text" v-model="search" class="form-control" aria-describedby="emailHelp" placeholder="영화 제목을 검색해보세요">
        <input type="submit" class="btn btn-primary" value="검색"></input>
    </form>
    <div class="cards">
      <YoutubeCard
        v-for="review in store.reviews"
        :review="review"
      />
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useMovieStore } from '@/stores/movie'
import YoutubeCard from '@/components/YoutubeCard.vue'

const search = ref('')
const store = useMovieStore()

const searchReview = function () {
  const keyword = search.value
  store.getReview(keyword)
  search.value = ''
}
</script>

<style scoped>
form {
  padding: 20px;
}
.form-container {
  display: flex;
  justify-content: center; /* 입력 필드와 버튼 정렬 */
  gap: 10px; /* 입력 필드와 버튼 간격 */
}
</style>