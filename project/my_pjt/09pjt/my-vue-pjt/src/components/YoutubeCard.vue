<template>
  <div class="card mb-3" style="max-width: 100%;" data-bs-toggle="modal" data-bs-target="#exampleModal" @click="setCurrentVideoId(review.id.videoId), setCurrentVideoTitle(review.snippet.title)">
    <div class="row g-0">
      <div class="col-md-4">
        <img :src="review.snippet.thumbnails.high.url" class="img-fluid rounded-start" alt="review.snippet.title">
      </div>
      <div class="col-md-8">
        <div class="card-body">
          <h5 class="card-title">{{ review.snippet.title }}</h5>
          <p class="card-text">{{ review.snippet.description }}</p>
        </div>
      </div>
    </div>
  </div>
  <div>
  <!-- <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true"> -->
    <YoutubeReviewModal />
  </div>
</template>

<script setup>
import { useMovieStore } from '@/stores/movie'
import YoutubeReviewModal from '@/components/YoutubeReviewModal.vue'

const store = useMovieStore()

const setCurrentVideoId = (videoId) => {
  console.log(videoId)
  store.videoId = videoId
}

const setCurrentVideoTitle = (videoTitle) => {
  store.videoTitle = videoTitle
}


defineProps({
  review: Object
})

</script>

<style scoped>
img {
  width: 100%;
}

</style>