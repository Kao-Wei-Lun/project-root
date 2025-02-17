<template>
  <div class="consultant-manager">
    <h1>諮詢師管理</h1>
    <div class="actions">
      <button @click="addConsultant">新增人員</button>
      <button @click="updateOrder">更新順序</button>
    </div>
    <div v-if="loading" class="loading">資料載入中...</div>
    <div v-else class="card-container">
      <div
        class="consultant-card"
        v-for="(consultant, index) in consultants"
        :key="consultant.id ? consultant.id : 'new-' + index"
      >
        <!-- 顯示流水號與目前順序 -->
        <div class="card-header">
          <span class="serial">{{ index + 1 }}</span>
          <span class="order">順序：{{ consultant.order }}</span>
        </div>
        <!-- 編輯區 -->
        <div class="card-body">
          <label>姓名:
            <input v-model="consultant.name" placeholder="請輸入姓名" />
          </label>
          <label>描述:
            <input v-model="consultant.description" placeholder="請輸入描述" />
          </label>
          <div class="image-section">
            <img
              v-if="consultant.image"
              :src="completeImageUrl(consultant.image)"
              :alt="consultant.name"
              width="100"
            />
            <input type="file" @change="handleFileChange($event, consultant)" />
          </div>
        </div>
        <!-- 操作按鈕 -->
        <div class="card-actions">
          <button @click="moveUp(index)" :disabled="index === 0">上移</button>
          <button @click="moveDown(index)" :disabled="index === consultants.length - 1">下移</button>
          <button @click="saveConsultant(consultant)">儲存</button>
          <button @click="deleteConsultant(consultant, index)" v-if="consultant.id">刪除</button>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import axios from 'axios'

// API 基本設定與端點
const API = 'http://127.0.0.1:8000'
const endpoint = '/services/api/consultants/'

// 響應式變數
const loading = ref(true)
const consultants = ref([])

// 取得諮詢師資料並依 order 排序
const fetchConsultants = async () => {
  try {
    const response = await axios.get(`${API}${endpoint}`)
    consultants.value = response.data.sort((a, b) => a.order - b.order)
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

// 當使用者選擇新圖片時，將檔案存入 consultant.newImage
const handleFileChange = (event, consultant) => {
  const file = event.target.files[0]
  if (file) {
    consultant.newImage = file
  }
}

// 儲存單筆資料：若 consultant.id 存在則更新，否則新增
const saveConsultant = async (consultant) => {
  try {
    if (consultant.newImage) {
      const formData = new FormData()
      formData.append('name', consultant.name)
      formData.append('description', consultant.description)
      formData.append('order', consultant.order)
      formData.append('image', consultant.newImage)
      
      if (consultant.id) {
        await axios.put(`${API}${endpoint}${consultant.id}/`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
        alert('更新成功')
      } else {
        const response = await axios.post(`${API}${endpoint}`, formData, {
          headers: { 'Content-Type': 'multipart/form-data' }
        })
        Object.assign(consultant, response.data)
        alert('新增成功')
      }
      consultant.newImage = null
    } else {
      if (consultant.id) {
        await axios.put(`${API}${endpoint}${consultant.id}/`, consultant)
        alert('更新成功')
      } else {
        const response = await axios.post(`${API}${endpoint}`, consultant)
        Object.assign(consultant, response.data)
        alert('新增成功')
      }
    }
  } catch (error) {
    console.error('儲存失敗:', error)
    alert('儲存失敗，請重試')
  }
}

// 刪除人員資料
const deleteConsultant = async (consultant, index) => {
  if (!confirm('確定要刪除這筆資料嗎？')) return
  try {
    await axios.delete(`${API}${endpoint}${consultant.id}/`)
    consultants.value.splice(index, 1)
    // 刪除後重新更新順序
    await updateOrder()
    alert('刪除成功')
  } catch (error) {
    console.error('刪除失敗:', error)
    alert('刪除失敗，請重試')
  }
}

// 重新計算所有記錄的 order 值
const recalcOrder = () => {
  consultants.value.forEach((consultant, idx) => {
    consultant.order = idx + 1
  })
}

// 更新順序：改用 PATCH 方法批次更新僅 order 欄位
const updateOrder = async () => {
  recalcOrder()
  try {
    const updatePromises = consultants.value.map((consultant) => {
      if (consultant.id) {
        // 只更新 order 欄位，使用 PATCH 方法進行部分更新
        return axios.patch(`${API}${endpoint}${consultant.id}/`, { order: consultant.order })
      } else {
        return Promise.resolve()
      }
    })
    await Promise.all(updatePromises)
    alert('順序更新成功')
  } catch (error) {
    console.error('更新順序失敗:', error)
    alert('更新順序失敗，請重試')
  }
}

// 順序調整：上移
const moveUp = (index) => {
  if (index === 0) return
  const temp = consultants.value[index]
  consultants.value[index] = consultants.value[index - 1]
  consultants.value[index - 1] = temp
  updateOrder()
}

// 順序調整：下移
const moveDown = (index) => {
  if (index === consultants.value.length - 1) return
  const temp = consultants.value[index]
  consultants.value[index] = consultants.value[index + 1]
  consultants.value[index + 1] = temp
  updateOrder()
}

// 新增人員：新增一筆空白記錄，初始 order 為目前陣列長度 + 1
const addConsultant = () => {
  const newOrder = consultants.value.length ? consultants.value[consultants.value.length - 1].order + 1 : 1
  consultants.value.push({
    id: null,
    name: '',
    description: '',
    image: '',
    order: newOrder,
    newImage: null
  })
}
</script>

<style scoped>
.consultant-manager {
  padding: 20px;
}

.actions {
  margin-bottom: 20px;
}

.actions button {
  margin-right: 10px;
  padding: 5px 10px;
}

.card-container {
  display: flex;
  flex-wrap: wrap;
  gap: 20px;
}

.consultant-card {
  border: 1px solid #ddd;
  border-radius: 8px;
  width: 250px;
  padding: 15px;
  display: flex;
  flex-direction: column;
  justify-content: space-between;
}

.card-header {
  display: flex;
  justify-content: space-between;
  margin-bottom: 10px;
  font-size: 0.9rem;
  color: #555;
}

.card-body label {
  display: block;
  margin-bottom: 8px;
}

.card-body input[type="text"] {
  width: 100%;
  padding: 5px;
  box-sizing: border-box;
}

.image-section {
  margin-top: 10px;
}

.image-section img {
  margin-bottom: 5px;
}

.card-actions {
  margin-top: 10px;
  text-align: center;
}

.card-actions button {
  margin: 2px;
  padding: 5px 8px;
  font-size: 0.85rem;
}
</style>
