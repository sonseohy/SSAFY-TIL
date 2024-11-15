<template>
    <div class="modal-dialog">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">공식 예고편</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <iframe
            :src="`https://www.youtube.com/embed/${store.trailerId}`"
            width="100%"
            height="315"
            frameborder="0"            
          ></iframe>
        </div>
      </div>
    </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()

</script>

<style scoped>

</style>