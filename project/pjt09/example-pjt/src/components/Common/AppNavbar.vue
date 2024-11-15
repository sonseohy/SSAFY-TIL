<template>
  <nav>
    <RouterLink to="/">Home</RouterLink> |
    <RouterLink to="/cart">Cart</RouterLink>
  </nav>
</template>

<script setup>
// setup : Vue 라이프 사이클
// Setup :  최초 세팅
// Mount : DOM이 그려진 후
// Update : 화면 완성 후 데이터 변경 시
// UnMount : 다른 컴포넌트로 이동 시
import { RouterLink } from 'vue-router'
</script>
