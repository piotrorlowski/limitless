<script setup lang="ts">
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { PlusIcon } from '@heroicons/vue/24/outline'

import ProfileEntry from '@/components/ProfileEntry.vue'
import ProfileCreateModal from '@/components/ProfileCreateModal.vue'

import { useProfileStore } from '@/stores/profile'

const router = useRouter()
const profiles = useProfileStore()

const createModalRef = ref()

function openDetails(id: number) {
  router.push({ name: 'profile-details', params: { id } })
}

function openCreate() {
  createModalRef.value.dialog.showModal()
}
</script>

<template>
  <div class="card bg-base-300">
    <div class="card-body">
      <div class="flex flex-row justify-between">
        <div class="card-title">Profiles</div>
        <plus-icon class="w-8 h-8" @click="openCreate" />
      </div>

      <div class="mt-5 flex flex-col w-full gap-5">
        <profile-entry
          v-for="profile in profiles.all"
          :key="profile.id"
          :profile="profile"
          @click="openDetails(profile.id)"
        />
      </div>
    </div>
  </div>

  <profile-create-modal ref="createModalRef" />
</template>
