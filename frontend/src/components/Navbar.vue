<!-- src/components/Navbar.vue -->
<template>
    <nav>
      <ul>
        <li><router-link to="/">首頁</router-link></li>
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
  /* 加入基本樣式 */
  nav ul {
    list-style: none;
    display: flex;
    gap: 1rem;
  }
  </style>
  