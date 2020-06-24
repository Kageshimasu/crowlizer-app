import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/form',
    name: 'Form',
    component: () => import('../components/pages/Form.vue'),
    children: [
      {
        path: 'date',
        component: () => import('../components/organisms/Date.vue')
      },
      {
        path: 'goal',
        component: () => import('../components/organisms/Goal.vue')
      },
      {
        path: 'methods',
        component: () => import('../components/organisms/Methods.vue')
      },
      {
        path: 'category',
        component: () => import('../components/organisms/Category.vue')
      },
      {
        path: 'description',
        component: () => import('../components/organisms/Description.vue')
      },
      {
        path: 'visualization',
        component: () => import('../components/organisms/Visualization.vue')
      },
      {
        path: 'sns',
        component: () => import('../components/organisms/Sns.vue')
      },
      {
        path: '*',
        component: () => import('../components/organisms/Date.vue')
      }
    ]
  },
  {
    path: '/about',
    name: 'About',
    component: () => import('../components/pages/About.vue')
  },
  {
    path: '/',
    name: 'Home',
    component: () => import('../components/pages/Home.vue')
  },
  {
    path: '/result',
    name: 'Result',
    component: () => import('../components/organisms/Result.vue')
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
