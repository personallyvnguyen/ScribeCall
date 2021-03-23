import Vue from 'vue'
import VueRouter, { RouteConfig } from 'vue-router'
import Ping from '../components/Ping.vue'
import Record from '../components/Record.vue'

Vue.use(VueRouter)

const routes: Array<RouteConfig> = [
  {
    path: '/',
    name: 'Record',
    component: Record,
  },
  {
    path: '/ping',
    name: 'Ping',
    component: Ping,
  },
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
