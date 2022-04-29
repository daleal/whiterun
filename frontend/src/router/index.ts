import { createRouter, createWebHistory, RouteRecordRaw } from 'vue-router';
import AdminView from '@/views/AdminView.vue';
import PayView from '@/views/PayView.vue';

const routes: RouteRecordRaw[] = [
  { path: '/', redirect: '/pay' },
  { path: '/admin', component: AdminView },
  { path: '/pay', component: PayView },
  { path: '/pay/:amount', component: PayView },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
