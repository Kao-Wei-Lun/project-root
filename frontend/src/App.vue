<!-- src/App.vue -->
<template>
  <div id="app">
    <Navbar />
    <!-- 之後可以加入 Footer -->
    <section class="hero">
      <h1>歡迎來到 XX 工作室</h1>
      <p>我們專注於數字易經、療癒占卜及神秘商品，幫助您找到心靈的平衡與生活的智慧。</p>
    </section>
    
    <router-view />

    <section class="done">
      <h2>聯絡資訊: line:@1234 email:1234@gmail.com</h2>
    </section>
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
  /* margin-bottom: 60px; */
}
/* 主視覺區 */
.hero {
  text-align: center;
  padding: 40px 20px;
  background: #f5f5f5;
  margin-bottom: 40px;
}

.done {
  /* position: fixed;   固定定位 */
  bottom: 0;         /* 與頁面底部對齊 */
  left: 0;
  right: 0;
  background: #fff;  /* 背景色，可根據需求調整 */
  text-align: center;
  padding: 1rem;     /* 內邊距 */
  border-top: 1px solid #ddd;  /* 上邊框 */
  z-index: 1000;     /* 確保顯示在其他內容上方 */
}

</style>
