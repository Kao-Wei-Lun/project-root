<!-- src/components/Navbar.vue -->
<template>
  <nav>
    <ul>
      <li><router-link to="/">首頁</router-link></li>
      <li class="dropdown">
        <span class="dropdown-text">服務項目</span>
        <ul class="dropdown-menu">
          <li><router-link to="/service/digital">數字易經諮詢</router-link></li>
          <li><router-link to="/service/healing">療癒與服務</router-link></li>
          <li><router-link to="/service/divination">牌卡占卜</router-link></li>
          <li><router-link to="/service/product">商品販售</router-link></li>
        </ul>
      </li>
      <li><router-link to="/consultant">諮詢師介紹</router-link></li>
      <li><router-link to="/feedback">回饋分享</router-link></li>
    </ul>
  </nav>
</template>

<script>
export default {
  name: 'Navbar'
}
</script>

<style scoped>
/* 將 nav 固定在頁面最上方 */
nav {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  background-color: #fff; /* 背景色可依需求修改 */
  z-index: 1000;
  border-bottom: 1px solid #ddd;
}

/* 調整 nav 內部的 ul */
nav ul {
  list-style: none;
  display: flex;
  gap: 1rem;
  align-items: center;
  margin: 0;
  padding: 1rem;
}

/* 讓 router-link 與下拉文字共用樣式 */
nav ul li > .dropdown-text,
nav ul li > a {
  color: inherit;
  text-decoration: none;
  padding: 0.5rem;
}

/* 下拉選單容器 */
.dropdown {
  position: relative;
  cursor: pointer;
}

/* 下拉選單樣式 */
.dropdown-menu {
  position: absolute;
  top: 100%;
  left: 0;
  list-style: none;
  background: #fff;
  border: 1px solid #ddd;
  padding: 0.5rem 0;
  display: none;
  min-width: 180px;
  z-index: 100;
}

/* 下拉選單項目 */
.dropdown-menu li {
  padding: 0.5rem 1rem;
}

/* 當滑鼠懸停時顯示下拉選單 */
.dropdown:hover .dropdown-menu {
  display: block;
}

/* 下拉項目懸停效果 */
.dropdown-menu li:hover {
  background: #f5f5f5;
}
</style>
