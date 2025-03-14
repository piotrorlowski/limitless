import { createWebHistory, createRouter } from 'vue-router'

import NotFoundView from '@/views/NotFoundView.vue'
import ProfileListView from '@/views/ProfileListView.vue'
import ProfileDetailsView from '@/views/ProfileDetailsView.vue'

const routes = [
  { path: '/', component: ProfileListView, name: 'profile-list' },
  { path: '/profile/:id', component: ProfileDetailsView, name: 'profile-details' },
  { path: '/not-found/', component: NotFoundView, name: 'not-found' },
  { path: '/:pathMatch(.*)*', redirect: { name: 'not-found' } }
]

export const router = createRouter({
  history: createWebHistory(),
  routes
})
