<template>
  <div class="feedback">
    <h1>回饋分享</h1>
    <div v-if="loading">資料載入中...</div>
    <div v-else>
      <ul class="feedback-list">
        <li v-for="item in feedbacks" :key="item.id" class="feedback-card">
          <p class="feedback-comment">"{{ item.comment }}"</p>
          <p class="feedback-user">- {{ item.user }}</p>
        </li>
      </ul>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

// API 基本設定與端點
const API = 'http://127.0.0.1:8000'
const endpoint = '/services/api/feedback/'

const feedbacks = ref([])
const loading = ref(true)

// 取得回饋資料的函式
const fetchFeedbacks = async () => {
  try {
    const response = await axios.get(`${API}${endpoint}`)
    console.log('回饋 API 回傳資料:', response.data)
    feedbacks.value = response.data
  } catch (error) {
    console.error('取得回饋資料失敗:', error)
  } finally {
    loading.value = false
  }
}

fetchFeedbacks()
</script>

<style scoped>
.feedback {
  padding: 20px;
}
.feedback-list {
  list-style: none;
  padding: 0;
}
.feedback-card {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 8px;
  margin-bottom: 15px;
  background-color: #f9f9f9;
}
.feedback-comment {
  font-style: italic;
  margin-bottom: 8px;
}
.feedback-user {
  text-align: right;
  font-weight: bold;
}
</style>
