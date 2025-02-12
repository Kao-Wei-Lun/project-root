<template>
  <div class="service-detail">
    <h1>{{ serviceData.name }}</h1>
    <!-- 將圖片 src 改為使用 computed 的 imageURL -->
    <img v-if="serviceData.image" :src="imageURL" :alt="serviceData.name" />
    <p>{{ serviceData.description }}</p>
    <p v-if="serviceData.price">價格：{{ serviceData.price }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import axios from 'axios'
import { useRoute } from 'vue-router'

// API 配置
const API = 'http://127.0.0.1:8000'
const getServiceURL = '/services/api/services/'

// 取得路由參數中的 serviceId
const route = useRoute()
const serviceId = route.params.id

// 定義響應式資料儲存 API 回傳的服務內容
const serviceData = ref({})

// 定義取得服務資料的函式
const fetchServiceDetail = async () => {
  try {
    const response = await axios.get(`${API}${getServiceURL}${serviceId}/`)
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

// 元件掛載時發送請求
onMounted(async () => {
  await fetchServiceDetail()
})

// 建立 computed 屬性 imageURL：如果 API 回傳的 image 為相對路徑則加上 API base URL
const imageURL = computed(() => {
  if (serviceData.value.image) {
    // 如果圖片路徑已包含 "http"，則直接回傳；否則拼接 API base URL 與圖片路徑
    return serviceData.value.image.startsWith('http')
      ? serviceData.value.image
      : `${API}${serviceData.value.image}`
  }
  return ''
})
</script>

<style scoped>
.service-detail {
  padding: 20px;
}
.service-detail img {
  max-width: 100%;
  height: auto;
  margin: 20px 0;
}
</style>
