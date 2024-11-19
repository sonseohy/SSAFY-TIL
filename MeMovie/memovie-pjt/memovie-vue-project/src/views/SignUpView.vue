<template>
  <div class="sign-up-container">
    <!-- 상단 제목 -->
    <div class="welcome-section">
      <h1 class="welcome-title">Welcome!</h1>
      <h2 class="sign-up-title">Sign up to</h2>
      <p class="description">Lorem Ipsum is simply dummy text of the printing industry.</p>
    </div>

    <!-- 회원가입 폼 -->
    <form @submit.prevent="signUp" class="sign-up-form">
      <!-- Username -->
      <div class="form-group">
        <label for="username" class="form-label">User name</label>
        <input type="text" id="username" v-model.trim="username" class="form-input" placeholder="Enter your user name">
      </div>

      <!-- Email -->
      <div class="form-group">
        <label for="email" class="form-label">Email</label>
        <input type="email" id="email" v-model.trim="email" class="form-input" placeholder="Enter your email">
      </div>

      <!-- Password -->
      <div class="form-group">
        <label for="password1" class="form-label">Password</label>
        <input type="password" id="password1" v-model.trim="password1" class="form-input" placeholder="Enter your password">
      </div>

      <!-- Confirm Password -->
      <div class="form-group">
        <label for="password2" class="form-label">Confirm Password</label>
        <input type="password" id="password2" v-model.trim="password2" class="form-input" placeholder="Confirm your password">
      </div>

      <!-- Submit 버튼 -->
      <div class="form-group">
        <button type="submit" class="submit-button">Register</button>
      </div>
    </form>

    <!-- 하단 링크 -->
    <p class="already-account">
      Already have an account? <RouterLink :to="{ name: 'LogInView' }" class="login-link">Login</RouterLink>
    </p>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'

const username = ref(null)
const password1 = ref(null)
const password2 = ref(null)
const email = ref(null)

const store = useAccountStore()

const signUp = function () {
  const payload = {
    username: username.value,
    password1: password1.value,
    password2: password2.value,
    email: email.value,
  }
  store.signUp(payload)
}

</script>

<style>
/* 전체 컨테이너 */
.sign-up-container {
  position: relative;
  width: 505px;
  margin: 0 auto;
  background: #FFFFFF;
  border: 0.5px solid #878787;
  box-shadow: 0px 4px 64px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  padding: 30px;
}

/* 상단 섹션 */
.welcome-section {
  text-align: left;
  margin-bottom: 20px;
}

.welcome-title {
  font-family: 'Poppins', sans-serif;
  font-size: 25px;
  font-weight: 300;
  color: #000000;
  margin: 0;
}

.sign-up-title {
  font-family: 'Poppins', sans-serif;
  font-size: 31px;
  font-weight: 500;
  color: #000000;
  margin: 10px 0;
}

.description {
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
}

/* 폼 섹션 */
.sign-up-form {
  display: flex;
  flex-direction: column;
  gap: 20px;
}

.form-group {
  display: flex;
  flex-direction: column;
}

.form-label {
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  font-weight: 400;
  color: #000000;
  margin-bottom: 5px;
}

.form-input {
  padding: 10px;
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  font-weight: 300;
  color: #282828;
  border: 0.6px solid #282828;
  border-radius: 6px;
  box-sizing: border-box;
}

.form-input::placeholder {
  color: #ABABAB;
}

/* 버튼 */
.submit-button {
  width: 100%;
  padding: 15px;
  background: #000000;
  color: #FFFFFF;
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  font-weight: 500;
  border: none;
  border-radius: 6px;
  cursor: pointer;
  transition: background 0.3s ease;
}

.submit-button:hover {
  background: #333333;
}

/* 하단 링크 */
.already-account {
  text-align: center;
  margin-top: 20px;
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  font-weight: 300;
  color: #7D7D7D;
}

.login-link {
  color: #000000;
  text-decoration: none;
  font-weight: 500;
}

.login-link:hover {
  text-decoration: underline;
}
</style>
