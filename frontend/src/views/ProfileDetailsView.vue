<script setup lang="ts">
import { computed } from 'vue'
import { useRoute } from 'vue-router'

import { useProfileStore } from '@/stores/profile'

const route = useRoute()

const profiles = useProfileStore()

const profile = computed(() => {
  const profileId = parseInt(route.params.id as string)
  return profiles.byId(profileId)
})
</script>

<template>
  <div class="card shadow-lg bg-base-100">
    <div class="card-body">
      <div class="card-title">Profile #{{ profile?.id }}</div>
      <div class="card-actions mt-12">
        <router-link :to="{ name: 'profile-list' }" class="btn btn-primary">Back</router-link>
      </div>
    </div>
  </div>
</template>
