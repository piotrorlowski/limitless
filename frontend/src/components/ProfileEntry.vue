<script setup lang="ts">
import type { Profile } from '@/interfaces/models'

defineProps<{ profile: Profile }>()
</script>

<template>
  <div class="card card-compact shadow-lg bg-base-100 w-96">
    <div class="card-body">
      <div class="flex flex-row items-center justify-between">
        <span class="text-lg">{{ profile.user.first_name }} {{ profile.user.last_name }}</span>

        <div v-if="profile.avatar" class="avatar">
          <div class="w-12 rounded-full">
            <img :src="profile.avatar" />
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
