<template>
  <div class="login-container">
    <h1>後台管理登入</h1>
    <form @submit.prevent="handleLogin">
      <div>
        <label for="username">帳號:</label>
        <input id="username" v-model="username" type="text" required />
      </div>
      <div>
        <label for="password">密碼:</label>
        <input id="password" v-model="password" type="password" required />
      </div>
      <button type="submit" :disabled="loading">登入</button>
    </form>
    <p v-if="error" class="error">{{ error }}</p>
  </div>
</template>

<script>
import axios from 'axios'

export default {
  name: 'Login',
  data() {
    return {
      username: '',
      password: '',
      loading: false,
      error: ''
    }
  },
  methods: {
    async handleLogin() {
      this.loading = true
      this.error = ''
      try {
        // 使用 Axios 呼叫登入 API（僅接受 POST 請求）
        const response = await axios.post('http://127.0.0.1:8000/api/admin/login/', {
          username: this.username,
          password: this.password
        })
        console.log('登入成功：', response.data)
        // 儲存 token 並導向 Dashboard（根據需求調整）
        localStorage.setItem('adminToken', response.data.access)
        this.$router.push('/dashboard')
      } catch (err) {
        this.error = '登入失敗，請檢查帳號密碼'
        console.error(err)
      } finally {
        this.loading = false
      }
    }
  }
}
</script>

<style scoped>
.login-container {
  max-width: 400px;
  margin: 100px auto;
  padding: 1rem;
  border: 1px solid #ddd;
  border-radius: 8px;
  text-align: center;
}
label {
  display: block;
  margin-bottom: 0.5rem;
}
input {
  width: 100%;
  padding: 0.5rem;
  margin-bottom: 1rem;
}
.error {
  color: red;
  margin-top: 1rem;
}
</style>
