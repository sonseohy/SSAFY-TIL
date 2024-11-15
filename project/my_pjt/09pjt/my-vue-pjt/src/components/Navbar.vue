<template>
  <nav class="navbar bg-body-tertiary">
    <div>
      <RouterLink to="/">
        <img src="@/assets/logo.png" alt="logo" width="80" height="80">
      </RouterLink>
    </div>
    <div>
      <RouterLink :to="{ name: 'MovieList' }">영화조회</RouterLink>
      <span>&nbsp</span>
      <RouterLink :to="{ name: 'ReviewSearch' }">리뷰검색</RouterLink>
      <span>&nbsp</span>
      <RouterLink :to="{ name: 'Recommended' }">영화추천</RouterLink>
    </div>
  </nav>
</template>

<script setup>
import { RouterLink } from 'vue-router'
</script>

<style scoped>
a {
  text-decoration: none;
  color: inherit;
}

.router-link-active {
  text-decoration: none;
  font-weight: bold;
  color: #007bff;
}
</style>