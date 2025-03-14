import { defineStore } from 'pinia'
import { ref } from 'vue'

import { ProfileApi } from '@/api/profile'

import type { Profile } from '@/interfaces/models'

const api = new ProfileApi()

export const useProfileStore = defineStore('profile', () => {
  const all = ref<Profile[]>()

  function byId(id: number) {
    return all.value?.find((profile) => profile.id === id)
  }

  async function retrieveAll() {
    await api.retrieveProfileList().then((response) => {
      all.value = response
    })
  }

  async function create(profileData: FormData) {
    return api.create(profileData).then((response) => {
      all.value?.push(response)
    })
  }

  return { all, byId, create, retrieveAll }
})
