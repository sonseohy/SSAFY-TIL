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
          <label for="title">영화 제목</label><br />
          <div class="movie-input-container">
            <input
              type="text"
              id="title"
              v-model="title"
              placeholder="영화 제목을 검색하세요"
              @input="searchMovies"
            />
            <!-- 선택된 영화 포스터 -->
            <div class="selected-poster">
              <img
                v-if="selectedMoviePoster"
                :src="`https://image.tmdb.org/t/p/w200${selectedMoviePoster}`"
                alt="선택된 영화 포스터"
              />
            </div>
          </div>
          <!-- 검색 결과 -->
          <ul v-if="searchResults.length > 0" class="search-results">
            <li
              v-for="(movie, index) in searchResults"
              :key="index"
              @click="selectMovie(movie)"
              class="movie-item"
            >
              {{ movie.title }}
            </li>
          </ul>
        </div>

        <!-- 영화 내용 입력 폼 -->
        <div class="form-group">
          <label for="content">영화 내용</label><br>
          <textarea 
            id="content" 
            v-model="content" 
            placeholder="영화에 대한 내용을 작성하세요"
          ></textarea>
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
        <div v-for="(review, index) in selectedReviews" :key="index" class="review-item">
          <!-- 영화 포스터 -->
          <div class="poster-container">
            <img
              v-if="review.poster_path"
              :src="`https://image.tmdb.org/t/p/w200${review.poster_path}`"
              alt="영화 포스터"
              class="movie-poster"
            />
            <div v-else class="no-poster">포스터 없음</div>
          </div>

          <!-- 영화 정보 -->
          <div class="review-info">
            <p><strong>영화 제목:</strong> {{ review.title }}</p>
            <p><strong>영화 내용:</strong> {{ review.content }}</p>
            
            <!-- 별점 표시 -->
            <div class="star-rating">
              <span
                v-for="star in 5"
                :key="star"
                class="star"
                :class="{ active: review.rating >= star }"
              >
                ★
              </span>
            </div>
          </div>
          
          <!-- 구분선 -->
          <hr v-if="index < selectedReviews.length - 1" />
        </div>

        <!-- 추가 작성하기 버튼 -->
        <button @click="addNewReview" class="add-review-button">+</button>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue';
import axios from 'axios';  // axios 임포트

// 모달 상태 관리
const showModal = ref(false);
const showContentModal = ref(false);
const selectedDate = ref('');
const title = ref('');
const content = ref('');
const rating = ref(0);  // 별점 초기화 0으로 설정
const selectedReviews = ref([]); // 선택된 리뷰들 (배열로 저장)
const reviews = ref([]); // 저장된 리뷰들
const searchResults = ref([]); // 검색된 영화 목록

// TMDB API 키
const apiKey = '084c3c6e5b92e9efba1b413f8aa0a03f';  // 여기서 실제 API 키를 입력해야 합니다


// 모달 열기
const openModal = (date) => {
  selectedDate.value = date; // 선택된 날짜 설정
  title.value = ""; // 제목 초기화
  content.value = ""; // 내용 초기화
  rating.value = 0; // 별점 초기화
  selectedMoviePoster.value = ""; // 포스터 초기화
  searchResults.value = []; // 검색 결과 초기화
  showModal.value = true; // 모달 열기
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
      poster_path: selectedMoviePoster.value, // 포스터 경로 저장
    };
    reviews.value.push(review); // 영화 기록 저장

    // 영화 기록을 달력에 이벤트로 추가
    calendar.addEvent({
      title: review.title, // 영화 제목
      start: review.date,
      description: `내용: ${review.content}, 별점: ${review.rating} ★`, // 내용과 별점 포함
    });

    // 입력 필드 및 상태 초기화
    title.value = ""; // 제목 초기화
    content.value = ""; // 내용 초기화
    rating.value = 0; // 별점 초기화
    selectedMoviePoster.value = ""; // 포스터 초기화
    searchResults.value = []; // 검색 결과 초기화

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

// 상태 변수
const selectedMoviePoster = ref(""); // 선택된 영화의 포스터

// 영화 검색 함수 (TMDB API)
const searchMovies = async () => {
  if (title.value.trim().length > 1) {
    try {
      const response = await axios.get(`https://api.themoviedb.org/3/search/movie`, {
        params: {
          api_key: apiKey,
          query: title.value,
          language: "ko-KR",
        },
      });
      searchResults.value = response.data.results;
    } catch (error) {
      console.error("영화 검색에 실패했습니다:", error);
      searchResults.value = [];
    }
  } else {
    searchResults.value = [];
  }
};

// 영화 선택 시 제목 및 포스터 설정
const selectMovie = (movie) => {
  title.value = movie.title; // 제목 설정
  selectedMoviePoster.value = movie.poster_path || ""; // 포스터 설정
  searchResults.value = []; // 검색 결과 숨김
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

/* 검색 결과 */
.search-results {
  list-style: none;
  padding: 0;
  margin-top: 5px;
  border-top: 1px solid #E0E0E0;
  max-height: 200px;
  overflow-y: auto;
}

.search-results li {
  padding: 8px;
  cursor: pointer;
}

.search-results li:hover {
  background-color: #F0F0F0;
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

/* 영화 입력 컨테이너 */
.movie-input-container {
  display: flex;
  align-items: center;
  gap: 10px;
}

/* 선택된 영화 포스터 */
.selected-poster img {
  width: 120px;
  height: 180px;
  border-radius: 5px;
  object-fit: cover;
  box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
}

/* 영화 기록 내용 */
.review-item {
  display: flex;
  align-items: center; /* 수직 중앙 정렬 */
  margin-bottom: 20px; /* 간격 */
}

/* 영화 포스터 */
.poster-container {
  width: 100px; /* 포스터의 너비 */
  height: 150px; /* 포스터의 높이 */
  margin-right: 20px; /* 이미지와 텍스트 사이의 간격 */
}

/* 영화 포스터 이미지 */
.movie-poster {
  width: 100%;
  height: 100%;
  object-fit: cover; /* 비율 유지하며 꽉 채우기 */
  border-radius: 5px;
}

/* 포스터가 없을 때 */
.no-poster {
  width: 100%;
  height: 100%;
  background-color: #e0e0e0;
  display: flex;
  justify-content: center;
  align-items: center;
  color: #777;
  border-radius: 5px;
}

/* 영화 정보 (제목, 내용, 별점) */
.review-info {
  flex: 1; /* 나머지 공간을 차지 */
  text-align: left; /* 텍스트 왼쪽 정렬 */
}

.review-info p {
  margin: 5px 0;
}

.star-rating {
  display: flex;
  margin-top: 10px;
}

/* 모달 창 내에서 추가 작성하기 버튼을 오른쪽 아래에 고정 */
.modal-content {
  position: relative; /* 모달을 기준으로 위치 설정 */
  background: white;
  padding: 20px;
  border-radius: 8px;
  text-align: center;
  width: 90vw;
  height: 80vh;
  max-width: 800px;
  max-height: 600px;
  overflow: auto; /* 스크롤 가능하게 설정 */
}

/* 추가 작성하기 버튼 */
.add-review-button {
  position: absolute; /* 모달 창 내에서 고정 위치 설정 */
  bottom: 20px;         /* 모달 창 하단에서 20px */
  right: 20px;          /* 모달 창 오른쪽에서 20px */
  width: 50px;          /* 버튼 크기 */
  height: 50px;         /* 버튼 크기 */
  background-color: #2AA971; /* 버튼 색상 */
  color: white;         /* 글씨 색상 */
  border-radius: 50%;   /* 동그란 모양 */
  font-size: 30px;      /* + 기호 크기 */
  display: flex;        /* Flexbox로 중앙 정렬 */
  justify-content: center; /* 수평 중앙 정렬 */
  align-items: center;  /* 수직 중앙 정렬 */
  border: none;         /* 테두리 제거 */
  cursor: pointer;      /* 커서 포인터로 변경 */
  z-index: 2000;        /* 모달보다 위에 표시되도록 설정 */
}

.add-review-button:hover {
  background-color: #229A5F; /* 버튼 호버 시 색상 */
}

</style>
