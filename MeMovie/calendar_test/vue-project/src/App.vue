<template>
  <div>
    <div id="calendar"></div>
    
    <!-- 모달 -->
    <div v-if="showModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <!-- 닫기 버튼 -->
        <button class="close-button" @click="closeModal">×</button>
        
        <!-- 모달 내용 -->
        <h2>날짜 정보</h2>
        <p>선택한 날짜: {{ selectedDate }}</p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue';

// 모달 상태 관리
const showModal = ref(false);
const selectedDate = ref('');

// 모달 열기
const openModal = (date) => {
  selectedDate.value = date;
  showModal.value = true;
};

// 모달 닫기
const closeModal = () => {
  showModal.value = false;
};

// FullCalendar 설정
document.addEventListener('DOMContentLoaded', function () {
  var calendarEI = document.getElementById('calendar');
  var calendar = new FullCalendar.Calendar(calendarEI, {
    initialView: 'dayGridMonth',
    selectable: true,
    dateClick: function (info) {
      openModal(info.dateStr); // 날짜 클릭 시 모달 열기
    },
  });
  calendar.render();
});
</script>

<style scoped>
/* 모달 배경 */
.modal-overlay {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  background-color: rgba(0, 0, 0, 0.5);
  display: flex;
  align-items: center;
  justify-content: center;
  z-index: 1000;
}

/* 모달 창 */
.modal-content {
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  position: relative; /* 닫기 버튼 위치 조정을 위해 상대 위치 설정 */
  width: 90vw; /* 가로 크기: 화면 너비의 90% */
  height: 80vh; /* 세로 크기: 화면 높이의 80% */
  max-width: 800px; /* 최대 가로 크기 제한 */
  max-height: 600px; /* 최대 세로 크기 제한 */
  overflow: auto; /* 내용이 넘칠 경우 스크롤 활성화 */
}

/* 닫기 버튼 */
.close-button {
  position: absolute; /* 부모 요소 기준으로 위치 설정 */
  top: 10px; /* 위쪽에서 10px */
  right: 10px; /* 오른쪽에서 10px */
  background: none;
  border: none;
  font-size: 40px; /* 버튼 크기 */
  font-weight: bold;
  color: #333;
  cursor: pointer;
}

.close-button:hover {
  color: #2AA971; /* 마우스 오버 시 색 변경 */
}
</style>
