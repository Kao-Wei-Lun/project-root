<template>
  <div class="consultant">
    <h1>諮詢師介紹</h1>
    <div v-if="loading">資料載入中...</div>
    <div v-else>
      <ul class="consultant-list">
        <li v-for="consultant in consultants" :key="consultant.id" class="consultant-card">
          <img
            v-if="consultant.image"
            :src="completeImageUrl(consultant.image)"
            :alt="consultant.name"
          />
          <h2>{{ consultant.name }}</h2>
          <p>{{ consultant.description }}</p>
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
const endpoint = '/services/api/consultants/'

const consultants = ref([])
const loading = ref(true)

// 取得諮詢師資料的函式
const fetchConsultants = async () => {
  try {
    const response = await axios.get(`${API}${endpoint}`)
    console.log('諮詢師 API 回傳資料:', response.data)
    consultants.value = response.data
  } catch (error) {
    console.error('取得資料失敗:', error)
  } finally {
    loading.value = false
  }
}

fetchConsultants()

// 輔助函式：根據圖片路徑組合完整 URL
const completeImageUrl = (imgPath) => {
  if (!imgPath) return ''
  return imgPath.startsWith('http') ? imgPath : `${API}${imgPath}`
}
</script>

<style scoped>
.consultant {
  padding: 20px;
}
.consultant-list {
  list-style: none;
  padding: 0;
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}
.consultant-card {
  border: 1px solid #ddd;
  padding: 15px;
  border-radius: 8px;
  width: 250px;
  text-align: center;
}
.consultant-card img {
  width: 100%;
  height: auto;
  border-radius: 4px;
  margin-bottom: 10px;
}
</style>
