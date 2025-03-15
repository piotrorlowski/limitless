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

const profileName = computed(
  () => `${profile.value?.user.first_name} ${profile.value?.user.last_name}`
)
</script>

<template>
  <div class="min-h-screen flex items-center justify-center p-4 cursor-pointer">
    <div class="card max-w-sm w-full bg-white rounded-3xl overflow-hidden">
      <div class="relative">
        <div class="h-32 bg-[#7DD3D1]"></div>
        <div class="absolute left-1/2 transform -translate-x-1/2 -translate-y-1/2">
          <div class="avatar">
            <div
              class="relative w-24 h-24 rounded-full ring-white ring-4 overflow-hidden bg-gray-300 text-gray-800 text-3xl font-medium"
            >
              <img v-if="profile?.avatar" :src="profile?.avatar" alt="Profile" />
              <div v-else class="absolute inset-0 flex items-center justify-center select-none">
                {{ `${profile?.user.first_name[0]}${profile?.user.last_name[0]}` }}
              </div>
            </div>
          </div>
        </div>
      </div>
      <div class="card-body text-center pt-16">
        <h2 class="text-2xl font-semibold mb-6">
          {{ profileName }}
        </h2>
        <p class="text-gray-600 mb-4 max-w-sm mx-auto">
          {{
            profile?.bio ||
            'Lorem Ipsum Dolor Sit Amet, Consectetur Adipiscing Elit, Sed Do Eiusmod Tempor Incididunt Ut Labore Et Dolore Magna Aliqua.'
          }}
        </p>
        <p class="text-gray-600 mb-8">Volutpat Lacus Laoreet Non Curabitur Gravida.</p>
        <div class="card-actions justify-end">
          <router-link
            :to="{ name: 'profile-list' }"
            class="btn btn-md bg-[#7DD3D1] hover:bg-[#6BC3C1] border-none text-gray-800 font-normal uppercase px-8"
          >
            Back
          </router-link>
        </div>
      </div>
    </div>
  </div>
</template>
