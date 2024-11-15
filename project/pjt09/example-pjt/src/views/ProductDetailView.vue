<template>
  <h1>상세 페이지</h1>
  <div v-if="product">
    <img :src="product.image" alt="" width="200px">
    <h3>가격 : {{ product.title }}</h3>
    <p>카테고리 : {{  product.category  }}</p>
  </div>
  <div v-else>
    <p>Loading...</p>
  </div>
</template>

<script setup>
import { useRoute } from 'vue-router'
import { useCartStore } from '@/stores/cart'

const store = useCartStore()
const route = useRoute()
const productId = route.params.product_id

const product = store.getProductById(productId)
console.log('product in component = ', product)
</script>

<style scoped>

</style>