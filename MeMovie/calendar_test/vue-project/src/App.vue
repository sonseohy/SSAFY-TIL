<template>
  <div>
    <!-- FullCalendar 사용 -->
    <div id="calendar"></div>

    <!-- 모달 (영화 기록 작성) -->
    <div v-if="showModal" class="modal-overlay" @click="closeModal">
      <div class="modal-content" @click.stop>
        <!-- 닫기 버튼 -->
        <button class="close-button" @click="closeModal">×</button>

        <!-- 모달 내용 -->
        <h2>영화 기록</h2>
        <p>선택한 날짜: {{ selectedDate }}</p>

        <!-- 영화 제목 입력 폼 -->
        <div class="form-group">
          <label for="title">영화 제목</label><br>
          <input type="text" id="title" v-model="title" placeholder="영화 제목을 입력하세요" />
        </div>

        <!-- 영화 내용 입력 폼 -->
        <div class="form-group">
          <label for="content">영화 내용</label><br>
          <textarea id="content" v-model="content" placeholder="영화에 대한 내용을 작성하세요"></textarea>
        </div>

        <!-- 별점 -->
        <div class="star-rating">
          <span 
            v-for="star in 5" 
            :key="star" 
            @click="setRating(star)" 
            class="star" 
            :class="{ active: rating >= star }">
            ★
          </span>
        </div>

        <!-- 작성 완료 버튼 -->
        <button @click="submitReview" class="submit-button">작성 완료</button>
      </div>
    </div>

    <!-- 영화 기록 내용 보기 모달 -->
    <div v-if="showContentModal" class="modal-overlay" @click="closeContentModal">
      <div class="modal-content" @click.stop>
        <!-- 닫기 버튼 -->
        <button class="close-button" @click="closeContentModal">×</button>

        <!-- 영화 기록 내용 -->
        <h2>영화 기록</h2>
        <!-- 여러 개의 영화 기록을 나열 -->
        <div v-for="(review, index) in selectedReviews" :key="index">
          <p><strong>영화 제목:</strong> {{ review.title }}</p>
          <p><strong>영화 내용:</strong> {{ review.content }}</p>
          
          <!-- 별점 표시 -->
          <div class="star-rating">
            <span 
              v-for="star in 5" 
              :key="star"
              class="star"
              :class="{ active: review.rating >= star }">
              ★
            </span>
          </div>
          
          <!-- 구분선 (hr 태그 추가) -->
          <hr v-if="index < selectedReviews.length - 1" />
        </div>

        <!-- 추가 작성하기 버튼 -->
        <button @click="addNewReview" class="add-review-button">추가 작성하기</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';

// 모달 상태 관리
const showModal = ref(false);
const showContentModal = ref(false);
const selectedDate = ref('');
const title = ref('');
const content = ref('');
const rating = ref(0);  // 별점 초기화 0으로 설정
const selectedReviews = ref([]); // 선택된 리뷰들 (배열로 저장)
const reviews = ref([]); // 저장된 리뷰들

// 모달 열기
const openModal = (date) => {
  selectedDate.value = date;
  title.value = '';    // 영화 제목 초기화
  content.value = '';  // 영화 내용 초기화
  rating.value = 0;    // 별점 초기화 (0점)
  showModal.value = true;
};

// 모달 닫기
const closeModal = () => {
  showModal.value = false;
};

// 영화 기록 내용 보기 모달 열기
const openContentModal = (date) => {
  // 해당 날짜에 작성된 영화 기록이 있으면 내용 모달 표시
  selectedReviews.value = reviews.value.filter(r => r.date === date);
  showContentModal.value = true;
};

// 영화 기록 내용 보기 모달 닫기
const closeContentModal = () => {
  showContentModal.value = false;
};

// 별점 설정 함수
const setRating = (star) => {
  rating.value = star;
};

// 작성 완료 함수
const submitReview = () => {
  if (title.value && content.value) {
    const review = {
      title: title.value,
      content: content.value,
      rating: rating.value,
      date: selectedDate.value,
    };
    reviews.value.push(review); // 영화 기록 저장

    // 영화 기록을 달력에 이벤트로 추가 (별점 포함)
    calendar.addEvent({
      title: review.title,   // 영화 제목
      start: review.date,
      description: `내용: ${review.content}, 별점: ${review.rating} ★`, // 내용과 별점도 포함
    });

    closeModal(); // 모달 닫기
  } else {
    alert("영화 제목과 내용을 입력해 주세요.");
  }
};

// FullCalendar 설정
let calendar = null;

onMounted(() => {
  var calendarEI = document.getElementById('calendar');
  calendar = new FullCalendar.Calendar(calendarEI, {
    initialView: 'dayGridMonth',
    selectable: true,
    events: reviews.value.map(review => ({
      title: review.title,   // 영화 제목 표시
      start: review.date,
      description: `내용: ${review.content}, 별점: ${review.rating} ★`, // 내용과 별점 포함
    })),
    dateClick: function (info) {
      // 해당 날짜에 작성된 영화 기록이 있으면 내용 모달 표시
      const review = reviews.value.filter(r => r.date === info.dateStr);
      if (review.length > 0) {
        openContentModal(info.dateStr); // 영화 기록 모달 열기
      } else {
        openModal(info.dateStr); // 날짜 클릭 시 영화 기록 모달 열기
      }
    },
  });
  calendar.render();
});

// 새로운 영화 기록 작성하기
const addNewReview = () => {
  closeContentModal();  // 기록 내용 모달 닫기
  openModal(selectedDate.value);  // 새로운 작성 모달 열기
};
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
  position: relative;
  width: 90vw;
  height: 80vh;
  max-width: 800px;
  max-height: 600px;
  overflow: auto;
}

/* 닫기 버튼 */
.close-button {
  position: absolute;
  top: 10px;
  right: 10px;
  background: none;
  border: none;
  font-size: 40px;
  font-weight: bold;
  color: #333;
  cursor: pointer;
}

.close-button:hover {
  color: #2AA971;
}

/* Form group */
.form-group {
  margin-bottom: 20px;
  width: 100%;
}

.form-group label {
  font-family: 'Inter', sans-serif;
  font-weight: 600;
  font-size: 16px;
  color: #000000;
}

/* 영화 제목(input) 폼 크기 수정 */
.form-group input {
  width: 100%;
  padding: 12px;
  margin-top: 8px;
  border: 1px solid #E0E0E0;
  border-radius: 8px;
  font-size: 14px;
  max-width: 100%; /* 100%로 너비 설정 */
  box-sizing: border-box;
}

/* 영화 내용(textarea) 폼 크기 수정 및 고정 */
.form-group textarea {
  width: 100%;
  padding: 12px;
  margin-top: 8px;
  border: 1px solid #E0E0E0;
  border-radius: 8px;
  font-size: 14px;
  max-width: 100%; /* 100%로 너비 설정 */
  height: 150px;    /* 높이 설정 */
  box-sizing: border-box;
  resize: none;     /* 사용자 크기 조정 비활성화 */
  overflow-y: auto; /* 내용이 길어지면 스크롤 */
}

/* Star rating */
.star-rating {
  display: flex;
  justify-content: center;
  margin: 20px 0;
}

.star {
  font-size: 30px;
  cursor: pointer;
  color: #D9D9D9;
}

.star.active {
  color: #2AA971;
}

/* Submit button */
.submit-button {
  width: 100%;
  padding: 12px;
  background: #2AA971;
  border-radius: 60px;
  font-family: 'Poppins', sans-serif;
  font-weight: 600;
  font-size: 16px;
  color: #FFFFFF;
  border: none;
  cursor: pointer;
}

.submit-button:hover {
  background-color: #229A5F;
}

/* 추가 작성하기 버튼 */
.add-review-button {
  position: absolute;
  bottom: 20px;
  left: 20px;
  padding: 10px 20px;
  background-color: #2AA971;
  color: white;
  border-radius: 30px;
  border: none;
  font-size: 16px;
  cursor: pointer;
}

.add-review-button:hover {
  background-color: #229A5F;
}
</style>
