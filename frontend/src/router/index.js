import { createRouter, createWebHistory } from 'vue-router'
import Home from '../views/Home.vue'
import DigitalService from '../views/DigitalService.vue'
import HealingService from '../views/HealingService.vue'
import DivinationService from '../views/DivinationService.vue'
import ProductService from '../views/ProductService.vue'
import Consultant from '../views/Consultant.vue'
import Feedback from '../views/Feedback.vue'

const routes = [
  {
    path: '/',
    name: 'Home',
    component: Home
  },
  {
    path: '/service/digital',
    name: 'DigitalService',
    component: DigitalService
  },
  {
    path: '/service/healing',
    name: 'HealingService',
    component: HealingService
  },
  {
    path: '/service/divination',
    name: 'DivinationService',
    component: DivinationService
  },
  {
    path: '/service/product',
    name: 'ProductService',
    component: ProductService
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
  history: createWebHistory(),
  routes
})

export default router
