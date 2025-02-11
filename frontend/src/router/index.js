// src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import ServiceDetail from '../views/ServiceDetail.vue'
import Consultant from '../views/Consultant.vue'
import Feedback from '../views/Feedback.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/service/:id',
    name: 'ServiceDetail',
    component: ServiceDetail
  },
  {
    path: '/consultant',
    name: 'Consultant',
    component: Consultant
  },
  {
    path: '/feedback',
    name: 'Feedback',
    component: Feedback
  }
]

const router = createRouter({
  history: createWebHistory(), // 根據需求，可調整 BASE_URL 設定
  routes
})

export default router
