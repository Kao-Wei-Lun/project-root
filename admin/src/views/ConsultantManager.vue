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
        <div class="card-header">
          <span class="serial">{{ index + 1 }}</span>
          <span class="order">順序：{{ consultant.order }}</span>
        </div>
        <div class="card-body">
          <label>姓名:
            <input v-model="consultant.name" placeholder="請輸入姓名" />
          </label>
          <label>描述:
            <input v-model="consultant.description" placeholder="請輸入描述" />
          </label>
          <label>詳細介紹:
            <textarea v-model="consultant.detailed_introduction" placeholder="請輸入詳細介紹"></textarea>
          </label>
          <!-- 修改服務項目，改成勾選方式 -->
          <div class="service-checkboxes">
            <p>服務項目:</p>
            <div v-for="option in serviceOptions" :key="option" class="checkbox-item">
              <label>
                <input
                  type="checkbox"
                  :value="option"
                  v-model="consultant.service_items_array"
                />
                {{ option }}
              </label>
            </div>
          </div>
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

// 預設服務選項
const serviceOptions = ['數字易經諮詢', '療癒與服務', '牌卡占卜', '商品販售']

const loading = ref(true)
const consultants = ref([])

// 取得諮詢師資料，並初始化 service_items_array
const fetchConsultants = async () => {
  try {
    const response = await axios.get(`${API}${endpoint}`)
    consultants.value = response.data.sort((a, b) => a.order - b.order)
    // 將每筆資料的 service_items（逗號分隔字串）轉換成陣列，存入 service_items_array
    consultants.value.forEach((consultant) => {
      consultant.service_items_array = consultant.service_items
        ? consultant.service_items.split(',').map(s => s.trim())
        : []
    })
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

const handleFileChange = (event, consultant) => {
  const file = event.target.files[0]
  if (file) {
    consultant.newImage = file
  }
}

const saveConsultant = async (consultant) => {
  try {
    // 將 service_items_array 轉換成逗號分隔字串，存入 service_items 欄位
    consultant.service_items = consultant.service_items_array.join(', ')
    
    if (consultant.newImage) {
      const formData = new FormData()
      formData.append('name', consultant.name)
      formData.append('description', consultant.description)
      formData.append('detailed_introduction', consultant.detailed_introduction)
      formData.append('service_items', consultant.service_items)
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

const deleteConsultant = async (consultant, index) => {
  if (!confirm('確定要刪除這筆資料嗎？')) return
  try {
    await axios.delete(`${API}${endpoint}${consultant.id}/`)
    consultants.value.splice(index, 1)
    await updateOrder()
    alert('刪除成功')
  } catch (error) {
    console.error('刪除失敗:', error)
    alert('刪除失敗，請重試')
  }
}

const recalcOrder = () => {
  consultants.value.forEach((consultant, idx) => {
    consultant.order = idx + 1
  })
}

const updateOrder = async () => {
  recalcOrder()
  try {
    const updatePromises = consultants.value.map((consultant) => {
      if (consultant.id) {
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

const moveUp = (index) => {
  if (index === 0) return
  const temp = consultants.value[index]
  consultants.value[index] = consultants.value[index - 1]
  consultants.value[index - 1] = temp
  updateOrder()
}

const moveDown = (index) => {
  if (index === consultants.value.length - 1) return
  const temp = consultants.value[index]
  consultants.value[index] = consultants.value[index + 1]
  consultants.value[index + 1] = temp
  updateOrder()
}

const addConsultant = () => {
  const newOrder = consultants.value.length ? consultants.value[consultants.value.length - 1].order + 1 : 1
  consultants.value.push({
    id: null,
    name: '',
    description: '',
    detailed_introduction: '',
    service_items: '',
    service_items_array: [], // 新增服務項目陣列
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

.card-body input[type="text"],
.card-body textarea {
  width: 100%;
  padding: 5px;
  box-sizing: border-box;
}

.card-body textarea {
  resize: vertical;
  min-height: 60px;
}

.service-checkboxes {
  margin-bottom: 8px;
}

.service-checkboxes p {
  margin-bottom: 4px;
  font-weight: bold;
}

.checkbox-item {
  display: inline-block;
  margin-right: 8px;
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
