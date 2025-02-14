// admin/src/router/index.js
import { createRouter, createWebHistory } from 'vue-router'
import Login from '../views/Login.vue'
import Dashboard from '../views/Dashboard.vue'
import HomeEditor from '../views/HomeEditor.vue'
import ServiceManager from '../views/ServiceManager.vue'
import ConsultantManager from '../views/ConsultantManager.vue'
import FeedbackManager from '../views/FeedbackManager.vue'

const routes = [
  {
    path: '/login',
    name: 'Login',
    component: Login
  },
  {
    path: '/dashboard',
    name: 'Dashboard',
    component: Dashboard,
    children: [
      {
        path: 'home-editor',
        name: 'HomeEditor',
        component: HomeEditor
      },
      {
        path: 'service-manager',
        name: 'ServiceManager',
        component: ServiceManager
      },
      {
        path: 'consultant-manager',
        name: 'ConsultantManager',
        component: ConsultantManager
      },
      {
        path: 'feedback-manager',
        name: 'FeedbackManager',
        component: FeedbackManager
      }
    ]
  },
  {
    path: '/',
    redirect: '/login'
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
