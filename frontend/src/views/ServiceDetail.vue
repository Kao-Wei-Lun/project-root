<template>
  <div class="service-detail">
    <h1>{{ serviceData.name }}</h1>
    <img v-if="serviceData.image" :src="serviceData.image" :alt="serviceData.name" />
    <p>{{ serviceData.description }}</p>
    <p v-if="serviceData.price">價格：{{ serviceData.price }}</p>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
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
