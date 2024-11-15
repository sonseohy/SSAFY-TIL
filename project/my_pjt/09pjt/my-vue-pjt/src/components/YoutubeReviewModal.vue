<template>
  <div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true" ref="modalRef">
  
    <div class="modal-dialog" >
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title">{{ store.videoTitle }}</h5>
          <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
        </div>
        <div class="modal-body">
          <!-- <p>Video ID: {{ store.videoId }}</p> -->
          <div v-if="isLoading">
            <p>로딩중</p>
          </div>
          <iframe v-else
            :src="videoData"
            width="100%"
            height="315"
            frameborder="0"            
          ></iframe>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, onBeforeUnmount } from 'vue'
import { useMovieStore } from '@/stores/movie'

const store = useMovieStore()
const isLoading = ref(false)
const modalRef = ref(null)
const videoData = ref(null)

const fetchReview = () => {
  isLoading.value = true;
  try {
    // 항상 YouTube 임베드 URL을 사용
    videoData.value = `https://www.youtube.com/embed/${store.videoId}?autoplay=1&mute=1`;
  } catch (error) {
    console.error("서버 에러:", error);
  }
  isLoading.value = false;
};


onMounted(() => {
  console.log(modalRef.value)
  if (modalRef.value) {
    modalRef.value.addEventListener("show.bs.modal", fetchReview);
  }
});

onBeforeUnmount(() => {
  if (modalRef.value) {
    modalRef.value.removeEventListener("show.bs.modal", fetchReview);
  }
});
</script>

<style scoped>

</style>