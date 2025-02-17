<template>
  <div class="feedback-manager">
    <h1>回饋管理</h1>
    <div class="actions">
      <button @click="addFeedback">新增回饋</button>
      <button @click="updateOrder">更新順序</button>
    </div>
    <div v-if="loading" class="loading">資料載入中...</div>
    <div v-else class="card-container">
      <div
        class="feedback-card"
        v-for="(item, index) in feedbacks"
        :key="item.id ? item.id : 'new-' + index"
      >
        <!-- 顯示流水號與目前順序 -->
        <div class="card-header">
          <span class="serial">{{ index + 1 }}</span>
          <span class="order">順序：{{ item.order }}</span>
          <span class="created_at" v-if="item.created_at">建立時間：{{ item.created_at }}</span>
        </div>
        <!-- 編輯區：使用者與回饋內容 -->
        <div class="card-body">
          <label>
            使用者:
            <input v-model="item.user" placeholder="請輸入使用者名稱" />
          </label>
          <label>
            回饋:
            <textarea v-model="item.comment" placeholder="請輸入回饋內容"></textarea>
          </label>
        </div>
        <!-- 操作按鈕 -->
        <div class="card-actions">
          <button @click="moveUp(index)" :disabled="index === 0">上移</button>
          <button @click="moveDown(index)" :disabled="index === feedbacks.length - 1">下移</button>
          <button @click="saveFeedback(item)">儲存</button>
          <button @click="deleteFeedback(item, index)" v-if="item.id">刪除</button>
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
const endpoint = '/services/api/feedback/'

// 響應式變數
const loading = ref(true)
const feedbacks = ref([])

// 取得回饋資料
const fetchFeedbacks = async () => {
  try {
    const response = await axios.get(`${API}${endpoint}`)
    // 假設回傳資料包含 order 欄位，依 order 排序
    feedbacks.value = response.data.sort((a, b) => a.order - b.order)
  } catch (error) {
    console.error('取得回饋資料失敗:', error)
  } finally {
    loading.value = false
  }
}
fetchFeedbacks()

// 儲存單筆回饋資料：若 item.id 存在則更新，否則新增
const saveFeedback = async (item) => {
  try {
    if (item.id) {
      await axios.put(`${API}${endpoint}${item.id}/`, item)
      alert('更新成功')
    } else {
      const response = await axios.post(`${API}${endpoint}`, item)
      Object.assign(item, response.data)
      alert('新增成功')
    }
  } catch (error) {
    console.error('儲存回饋失敗:', error)
    alert('儲存回饋失敗，請重試')
  }
}

// 刪除回饋資料
const deleteFeedback = async (item, index) => {
  if (!confirm('確定要刪除這筆回饋嗎？')) return
  try {
    await axios.delete(`${API}${endpoint}${item.id}/`)
    feedbacks.value.splice(index, 1)
    // 刪除後更新順序
    await updateOrder()
    alert('刪除成功')
  } catch (error) {
    console.error('刪除回饋失敗:', error)
    alert('刪除回饋失敗，請重試')
  }
}

// 重新計算所有記錄的 order 值
const recalcOrder = () => {
  feedbacks.value.forEach((item, idx) => {
    item.order = idx + 1
  })
}

// 更新順序：使用 PATCH 方法僅更新 order 欄位
const updateOrder = async () => {
  recalcOrder()
  try {
    const updatePromises = feedbacks.value.map((item) => {
      if (item.id) {
        return axios.patch(`${API}${endpoint}${item.id}/`, { order: item.order })
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
  const temp = feedbacks.value[index]
  feedbacks.value[index] = feedbacks.value[index - 1]
  feedbacks.value[index - 1] = temp
  updateOrder()
}

// 順序調整：下移
const moveDown = (index) => {
  if (index === feedbacks.value.length - 1) return
  const temp = feedbacks.value[index]
  feedbacks.value[index] = feedbacks.value[index + 1]
  feedbacks.value[index + 1] = temp
  updateOrder()
}

// 新增回饋：新增一筆空白記錄，初始 order 為目前陣列長度 + 1
const addFeedback = () => {
  const newOrder = feedbacks.value.length ? feedbacks.value[feedbacks.value.length - 1].order + 1 : 1
  feedbacks.value.push({
    id: null,
    user: '',
    comment: '',
    order: newOrder,
    created_at: null
  })
}
</script>

<style scoped>
.feedback-manager {
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

.feedback-card {
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
  font-size: 0.9rem;
  color: #555;
  margin-bottom: 10px;
}

.card-body label {
  display: block;
  margin-bottom: 8px;
}

.card-body input,
.card-body textarea {
  width: 100%;
  padding: 5px;
  box-sizing: border-box;
}

.card-body textarea {
  resize: vertical;
  min-height: 60px;
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
