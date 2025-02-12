<template>
    <div class="digital-service">
      <h1>{{ serviceData.name }}</h1>
      <img v-if="serviceData.image" :src="completeImageUrl" :alt="serviceData.name" />
      <p>{{ serviceData.description }}</p>
      <p v-if="serviceData.price">價格：{{ serviceData.price }}</p>
    </div>
  </template>
  
  <script setup>
  import { ref, onMounted, computed } from 'vue'
  import axios from 'axios'
  
  // API 基本設定
  const API = 'http://127.0.0.1:8000'
  const getServiceURL = '/services/api/services/'
  
  // 這裡指定數字易經諮詢的 slug 為 "digital"
  const serviceSlug = 'digital'
  
  // 用來儲存 API 回傳的服務資料
  const serviceData = ref({})
  
  // 定義取得服務資料的函式
  const fetchServiceDetail = async () => {
    try {
      const response = await axios.get(`${API}${getServiceURL}${serviceSlug}/`)
      console.log('API 回傳資料:', response.data)
      serviceData.value = response.data
    } catch (error) {
      console.error('API 取得資料失敗:', error)
      serviceData.value = {
        name: '找不到服務',
        description: '請檢查服務ID是否正確或稍後再試。',
        image: '',
        price: null,
      }
    }
  }
  
  // 當元件掛載時呼叫 API 取得資料
  onMounted(async () => {
    await fetchServiceDetail()
  })
  
  // computed 屬性：根據取得的圖片路徑組合完整 URL
  const completeImageUrl = computed(() => {
    if (!serviceData.value.image) return ''
    return serviceData.value.image.startsWith('http')
      ? serviceData.value.image
      : `${API}${serviceData.value.image}`
  })
  </script>
  
  <style scoped>
  .digital-service {
    padding: 20px;
  }
  .digital-service img {
    max-width: 100%;
    height: auto;
    margin: 20px 0;
  }
  </style>
  