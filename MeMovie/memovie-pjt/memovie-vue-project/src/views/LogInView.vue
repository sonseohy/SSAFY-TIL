<template>
  <div class="login-container">
    <div class="login-box">
      <h1 class="welcome">Welcome!</h1>
      <h2 class="sign-in-title">Sign in to</h2>
      <p class="subtitle">Lorem Ipsum is simply dummy text of the printing.</p>
      
      <form @submit.prevent="logIn" class="login-form">
        <div class="form-group">
          <label for="username" class="label">User name</label>
          <input
            type="text"
            id="username"
            v-model.trim="username"
            placeholder="Enter your user name"
            class="input"
          />
        </div>

        <div class="form-group">
          <label for="password" class="label">Password</label>
          <input
            type="password"
            id="password"
            v-model.trim="password"
            placeholder="Enter your Password"
            class="input"
          />
        </div>

        <div class="form-options">
          <label class="remember-me">
            <input type="checkbox" />
            Remember me
          </label>
          <a href="#" class="forgot-password">Forgot Password?</a>
        </div>

        <button type="submit" class="login-button">Log In</button>
      </form>

      <p class="register-link">
        Don’t have an Account? <RouterLink :to="{ name: 'SignUpView' }">Register</RouterLink>
      </p>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { useAccountStore } from '@/stores/account'

const username = ref(null)
const password = ref(null)

const store = useAccountStore()

const logIn = function () {
  const payload = {
    username: username.value,
    password: password.value
  }
  store.logIn(payload)
}
</script>

<style>
/* 전체 컨테이너 */
.login-container {
  display: flex;
  justify-content: center;
  align-items: center;
  height: 100vh;
  background-color: #f8f8f8;
}

/* 로그인 박스 */
.login-box {
  position: relative;
  width: 505px;
  height: 701px;
  background: #ffffff;
  border: 0.5px solid #878787;
  box-shadow: 0px 4px 64px rgba(0, 0, 0, 0.05);
  border-radius: 10px;
  padding: 30px;
  box-sizing: border-box;
}

/* 제목 스타일 */
.welcome {
  font-family: 'Poppins', sans-serif;
  font-weight: 300;
  font-size: 25px;
  line-height: 38px;
  color: #000000;
  margin-bottom: 10px;
}

.sign-in-title {
  font-family: 'Poppins', sans-serif;
  font-weight: 500;
  font-size: 31px;
  line-height: 46px;
  color: #000000;
  margin-bottom: 10px;
}

.subtitle {
  font-family: 'Poppins', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  color: #000000;
  margin-bottom: 30px;
}

/* 폼 스타일 */
.login-form {
  display: flex;
  flex-direction: column;
}

.form-group {
  margin-bottom: 20px;
}

.label {
  display: block;
  font-family: 'Poppins', sans-serif;
  font-weight: 400;
  font-size: 16px;
  line-height: 24px;
  color: #000000;
  margin-bottom: 8px;
}

.input {
  width: 100%;
  height: 40px;
  border: 0.6px solid #282828;
  border-radius: 6px;
  padding: 10px;
  font-family: 'Poppins', sans-serif;
  font-size: 14px;
  color: #000000;
  box-sizing: border-box;
}

/* 옵션 스타일 */
.form-options {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 20px;
}

.remember-me {
  font-family: 'Poppins', sans-serif;
  font-size: 12px;
  color: #000000;
}

.forgot-password {
  font-family: 'Poppins', sans-serif;
  font-size: 12px;
  color: #4D4D4D;
  text-decoration: none;
}

/* 로그인 버튼 */
.login-button {
  width: 100%;
  height: 50px;
  background: #000000;
  color: #ffffff;
  font-family: 'Poppins', sans-serif;
  font-weight: 500;
  font-size: 16px;
  line-height: 24px;
  text-align: center;
  border: none;
  border-radius: 6px;
  cursor: pointer;
}

/* 하단 링크 */
.register-link {
  font-family: 'Poppins', sans-serif;
  font-size: 16px;
  font-weight: 300;
  text-align: center;
  margin-top: 20px;
  color: #7d7d7d;
}

.register-link a {
  color: #0000ff;
  text-decoration: none;
}
</style>
