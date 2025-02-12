<!-- src/App.vue -->
<template>
  <div id="app">
    <Navbar />
    <router-view />
    <!-- 之後可以加入 Footer -->
  </div>
</template>

<script>
import Navbar from './components/Navbar.vue'
export default {
  name: 'App',
  components: {
    Navbar
  }
}
</script>

<style>
/* 全域樣式設定 */
.main-content {
  margin-top: 80px; /* 根據 nav 高度調整 */
}
</style>
