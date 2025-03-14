<script setup lang="ts">
import { onMounted } from 'vue'

import { useProfileStore } from '@/stores/profile'

const profiles = useProfileStore()

onMounted(async () => {
  profiles.retrieveAll()
})
</script>

<template>
  <div class="flex flex-col items-center justify-center py-0 min-h-screen w-screen">
    <router-view />
  </div>
</template>
