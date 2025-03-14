import { fileURLToPath, URL } from 'node:url'
const { resolve } = require('path')
import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  root: resolve('./src'),
  base: '/static/frontend/',
  server: {
    host: true,
    port: 3000,
    open: false,
    watch: {
      usePolling: true,
      disableGlobbing: false
    }
  },
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  },
  build: {
    outDir: resolve('./dist/frontend/'),
    assetsDir: '',
    manifest: true,
    emptyOutDir: true,
    target: 'es2015',
    rollupOptions: {
      input: {
        // General assets & scripts
        main_css: resolve('./src/assets/main.css'),
        // Customer input scripts
        limitless_profile: resolve('./src/limitless_profile.ts')
      },
      output: {
        chunkFileNames: undefined
      }
    }
  }
})
