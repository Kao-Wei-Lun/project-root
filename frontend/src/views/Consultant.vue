<template>
  <div class="consultant">
    <h1>諮詢師介紹</h1>
    <!-- 篩選服務項目按鈕區 -->
    <div class="filter">
      <h3>篩選服務項目：</h3>
      <div class="filter-buttons">
        <button 
          v-for="option in filterOptions" 
          :key="option"
          :class="{ selected: isSelected(option) }"
          @click="toggleOption(option)"
        >
          {{ option }}
        </button>
      </div>
    </div>
    <div v-if="loading" class="loading">資料載入中...</div>
    <div v-else>
      <ul class="consultant-list">
        <li
          v-for="consultant in filteredConsultants"
          :key="consultant.id"
          class="consultant-card"
          @click="selectConsultant(consultant)"
        >
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

    <!-- 詳細介紹區 -->
    <div v-if="detailConsultant" class="detail">
      <h2>詳細介紹</h2>
      <img
        v-if="detailConsultant.image"
        :src="completeImageUrl(detailConsultant.image)"
        :alt="detailConsultant.name"
        width="150"
      />
      <h3>{{ detailConsultant.name }}</h3>
      <p><strong>服務項目：</strong> {{ detailConsultant.service_items }}</p>
      <p><strong>詳細介紹：</strong> {{ detailConsultant.detailed_introduction }}</p>
      <button @click="detailConsultant = null">關閉詳細介紹</button>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import axios from 'axios'

// API 基本設定與端點
const API = 'http://127.0.0.1:8000'
const endpoint = '/services/api/consultants/'

const loading = ref(true)
const consultants = ref([])
const detailConsultant = ref(null)

// 篩選條件
const filterOptions = ref(['ALL', '數字易經諮詢', '療癒與服務', '牌卡占卜', '商品販售'])
const selectedFilters = ref([])

// 取得諮詢師資料
const fetchConsultants = async () => {
  try {
    const response = await axios.get(`${API}${endpoint}`)
    consultants.value = response.data
  } catch (error) {
    console.error('取得資料失敗:', error)
  } finally {
    loading.value = false
  }
}
fetchConsultants()

// 輔助函式：組合完整圖片 URL
const completeImageUrl = (imgPath) => {
  if (!imgPath) return ''
  return imgPath.startsWith('http') ? imgPath : `${API}${imgPath}`
}

// 篩選功能
const toggleOption = (option) => {
  if (option === 'ALL') {
    if (selectedFilters.value.includes('ALL')) {
      selectedFilters.value = []
    } else {
      selectedFilters.value = ['ALL']
    }
  } else {
    if (selectedFilters.value.includes('ALL')) {
      selectedFilters.value = selectedFilters.value.filter(o => o !== 'ALL')
    }
    if (selectedFilters.value.includes(option)) {
      selectedFilters.value = selectedFilters.value.filter(o => o !== option)
    } else {
      selectedFilters.value.push(option)
    }
  }
}

const isSelected = (option) => selectedFilters.value.includes(option)

const filteredConsultants = computed(() => {
  if (selectedFilters.value.length === 0 || selectedFilters.value.includes('ALL')) {
    return consultants.value
  }
  return consultants.value.filter(consultant => {
    const items = consultant.service_items ? consultant.service_items.split(',').map(s => s.trim()) : []
    return selectedFilters.value.some(filter => items.includes(filter))
  })
})

// 點選卡片後顯示詳細介紹
const selectConsultant = (consultant) => {
  detailConsultant.value = consultant
}
</script>

<style scoped>
.consultant {
  padding: 20px;
}
.filter {
  margin-bottom: 20px;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 4px;
}
.filter-buttons {
  display: flex;
  flex-wrap: wrap;
  gap: 10px;
}
.filter-buttons button {
  padding: 10px 15px;
  border: 1px solid #ddd;
  background-color: #f5f5f5;
  border-radius: 10px; /* 圓角正方形 */
  cursor: pointer;
  font-size: 14px;
  transition: background-color 0.2s, border-color 0.2s, color 0.2s;
}
.filter-buttons button.selected {
  background-color: #007BFF;
  color: #fff;
  border-color: #007BFF;
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
  cursor: pointer;
  transition: transform 0.2s;
}
.consultant-card:hover {
  transform: scale(1.03);
}
.consultant-card img {
  width: 100%;
  height: auto;
  border-radius: 4px;
  margin-bottom: 10px;
}
.detail {
  margin-top: 30px;
  padding: 20px;
  border: 1px solid #aaa;
  border-radius: 8px;
  background: #f9f9f9;
}
.loading {
  text-align: center;
  font-size: 1.2rem;
}
</style>
