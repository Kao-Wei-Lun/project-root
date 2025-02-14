<template>
    <div class="dashboard">
      <aside class="sidebar">
        <ul>
          <li><router-link to="/dashboard/home-editor">首頁編輯</router-link></li>
          <li><router-link to="/dashboard/service-manager">服務管理</router-link></li>
          <li><router-link to="/dashboard/consultant-manager">諮詢師管理</router-link></li>
          <li><router-link to="/dashboard/feedback-manager">回饋管理</router-link></li>
        </ul>
      </aside>
      <main class="content">
        <!-- 根據子路由顯示對應頁面 -->
        <router-view></router-view>
      </main>
    </div>
  </template>
  
  <script>
  export default {
    name: 'Dashboard'
  }
  </script>
  
  <style scoped>
  .dashboard {
    display: flex;
    min-height: 100vh;
  }
  .sidebar {
    width: 220px;
    background: #f5f5f5;
    padding: 1rem;
    border-right: 1px solid #ddd;
  }
  .sidebar ul {
    list-style: none;
    padding: 0;
  }
  .sidebar li {
    margin-bottom: 1rem;
  }
  .content {
    flex: 1;
    padding: 2rem;
  }
  </style>
  