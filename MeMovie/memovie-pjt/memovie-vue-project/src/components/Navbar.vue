<template>
  <nav class="navbar">
    <!-- 버튼 -->
    <div class="menu-button-container">
      <button
        class="navbar-toggler"
        type="button"
        data-bs-toggle="offcanvas"
        data-bs-target="#offcanvasNavbar"
        aria-controls="offcanvasNavbar"
        aria-label="Toggle navigation"
      >
        <span class="navbar-toggler-icon"></span>
      </button>
    </div>

    <!-- 오프캔버스 -->
    <div
      class="offcanvas offcanvas-start custom-offcanvas"
      tabindex="-1"
      id="offcanvasNavbar"
      aria-labelledby="offcanvasNavbarLabel"
    >
      <div class="offcanvas-header">
        <h5 class="offcanvas-title" id="offcanvasNavbarLabel">Menu</h5>
        <button
          type="button"
          class="btn-close"
          data-bs-dismiss="offcanvas"
          aria-label="Close"
        ></button>
      </div>
      <div class="offcanvas-body">
        <!-- 검색 폼 추가 -->
        <div class="search-container">
          <input
            type="text"
            class="form-control search-input"
            placeholder="Search movie"
          />
          <button class="search-button">
            <i class="fa-solid fa-magnifying-glass"></i> <!-- 검색 아이콘 (Bootstrap Icons) -->
          </button>
        </div>

        <ul class="navbar-nav justify-content-end flex-grow-1 pe-3">
          <li class="nav-item">
            <RouterLink :to="{ name: 'MovieList' }" class="nav-link">Recommend</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'RecordList' }" class="nav-link">Monthly Movie</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'CommunityList' }" class="nav-link">Community</RouterLink>
          </li>
          <li class="nav-item">
            <RouterLink :to="{ name: 'LogInView' }" class="nav-link">Login</RouterLink>
          </li>
        </ul>
      </div>
    </div>

    <!-- 로고 -->
    <div class="logo-container">
      <RouterLink :to="{ name: 'Main' }">
        <img
          src="@/assets/MeMovie_nav_logo.png"
          alt="Memovie-logo"
          class="nav-logo"
        />
      </RouterLink>
    </div>

    <!-- 링크 -->
    <div class="links-container">
      <RouterLink :to="{ name: 'MovieList' }" class="nav-link">Recommend</RouterLink>
      <RouterLink :to="{ name: 'RecordList' }" class="nav-link">Monthly Movie</RouterLink>
      <RouterLink :to="{ name: 'CommunityList' }" class="nav-link">Community</RouterLink>
      <RouterLink :to="{ name: 'LogInView' }" class="nav-link">Login</RouterLink>
    </div>
  </nav>
</template>

<style>
/* 네비게이션 바 */
.navbar {
  position: absolute;
  width: 100%;
  height: 84px;
  display: flex;
  align-items: center;
  justify-content: center;
  background: rgba(252, 252, 252, 0.5);
  box-shadow: -4px -4px 4px rgba(0, 0, 0, 0.25),
    4px 4px 4px rgba(0, 0, 0, 0.25);
  backdrop-filter: blur(2px);
  border-radius: 60px;
  padding: 0 30px;
  box-sizing: border-box;
  z-index: 100;
}

/* 메뉴 버튼 스타일 */
.menu-button-container {
  position: absolute;
  left: 30px;
}

.menu-button-container .navbar-toggler {
  border: none; /* 테두리 제거 */
  box-shadow: none; /* 그림자 제거 */
  outline: none; /* 포커스 테두리 제거 */
  background: transparent; /* 배경 투명화 */
}

.menu-button-container .navbar-toggler:focus {
  outline: none; /* 포커스 시에도 테두리 제거 */
}

/* 로고 스타일 */
.logo-container {
  position: absolute;
  left: 50%;
  transform: translateX(-50%);
}

.nav-logo {
  height: 58px;
}

/* 링크 컨테이너 */
.links-container {
  display: flex;
  align-items: center;
  gap: 20px;
  position: absolute;
  right: 30px;
}

.nav-link {
  font-family: 'Inter', sans-serif;
  font-weight: 400;
  font-size: 15px;
  line-height: 15px;
  color: #28353d;
  text-decoration: none;
  transition: color 0.3s ease;
}

.nav-link:hover {
  font-weight: 600;
  color: #2AA971;
}

.router-link-active {
  font-weight: 600;
  color: #2AA971 !important;
}

/* 오프캔버스 커스터마이징 */
.custom-offcanvas {
  height: 100vh; /* 전체 화면 높이 */
  width: 300px; /* 폭을 적절히 설정 */
  background: #ffffff; /* 배경색 */
  box-shadow: 2px 0 10px rgba(0, 0, 0, 0.1); /* 오른쪽 그림자 */
  display: flex;
  flex-direction: column;
  position: fixed; /* 고정 위치 */
}

.custom-offcanvas .offcanvas-header {
  border-bottom: 1px solid #ddd;
  padding: 15px;
}

.custom-offcanvas .offcanvas-body {
  flex-grow: 1; /* 남은 공간을 차지하도록 설정 */
  overflow-y: auto; /* 스크롤 가능 */
  padding: 15px;
}

/* 검색 입력 스타일 */
.search-container {
  display: flex;
  align-items: center;
  margin-bottom: 15px;
}

.search-input {
  border-radius: 30px;
  padding: 10px 15px;
  width: 80%;
  font-size: 14px;
  border: 1px solid #ddd;
  background-color: #f8f9fa;
  box-shadow: none;
}

.search-input:focus {
  border-color: #2AA971;
  box-shadow: 0 0 5px rgba(42, 169, 113, 0.5);
}

.search-button {
  background-color: #2AA971;
  border: none;
  padding: 10px 15px;
  border-radius: 30px;
  color: white;
  font-size: 14px;
  margin-left: 10px;
  cursor: pointer;
  display: flex;
  align-items: center;
}

.search-button:hover {
  background-color: #218d58;
}

.search-button i {
  font-size: 16px; /* 아이콘 크기 */
}

</style>
