<template>
  <div class="content-container">
    <!-- 사용자 정보 -->
    <div class="user-info-card">
    </div>
    
    <Calendar
      class="user-info-card"
    />

  </div>
</template>

<script setup>
import Calendar from '@/components/Calendar.vue';


</script>

<style scoped>
/* 메인 콘텐츠 */
.content-container {
  display: flex;
  width: 100%;
  max-width: 1200px;
  margin: 20px auto; /* 중앙 정렬과 상하 여백 */
  gap: 20px;
  position: relative; /* 부모에 상대 위치 지정 */
}

/* 사용자 정보 카드 */
.user-info-card {
  width: 30%;
  background: white;
  border-radius: 10px;
  box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.1);
  padding: 20px;
  text-align: center;
}

.profile-image {
  width: 100px;
  height: 100px;
  border-radius: 50%;
  margin-bottom: 10px;
}

.username {
  font-size: 18px;
  font-weight: bold;
}

.user-description {
  font-size: 14px;
  color: gray;
}

.user-follow {
  font-size: 14px;
  margin-top: 10px;
}

.settings-button,
.logout-button {
  width: 100%;
  padding: 10px;
  margin-top: 10px;
  border: none;
  border-radius: 5px;
  cursor: pointer;
}

.settings-button {
  background-color: #e9ecef;
  color: #333;
}

.logout-button {
  background-color: #f03e3e;
  color: white;
}

.calendar {
  width: 70%;
}
</style>
