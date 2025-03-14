import { createPinia } from 'pinia'
import { createApp } from 'vue'

import { router } from '@/router'
import App from '@/apps/LimitlessProfile.vue'

import 'vue-loading-overlay/dist/css/index.css'

const app = createApp(App)
app.use(router)
app.use(createPinia())
app.mount('#limitless-profile')
