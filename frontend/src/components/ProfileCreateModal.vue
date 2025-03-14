<script setup lang="ts">
import { ref } from 'vue'

import { useProfileStore } from '@/stores/profile'

const profiles = useProfileStore()

const dialogRef = ref()

defineExpose({ dialog: dialogRef })

function submit(event: Event) {
  const formData = new FormData(event.target as HTMLFormElement)
  profiles.create(formData)
}
</script>

<template>
  <dialog id="create-profile-dialog" ref="dialogRef" class="modal">
    <div class="modal-box">
      <h3 class="font-bold text-lg">Create Profile</h3>
      <form method="dialog" @submit="submit">
        <div class="flex flex-col gap-5 my-5 p-5">
          <input
            id="first_name"
            name="first_name"
            class="text-input"
            type="text"
            placeholder="First Name"
          />
          <input
            id="last_name"
            name="last_name"
            class="text-input"
            type="text"
            placeholder="Last Name"
          />
          <input id="email" name="email" class="text-input" type="email" placeholder="Email" />
          <textarea
            id="bio"
            name="bio"
            class="textarea textarea-bordered"
            placeholder="Biography"
          />
          <input
            id="avatar"
            name="avatar"
            type="file"
            class="file-input file-input-bordered w-full max-w-xs"
          />
        </div>

        <div class="modal-action">
          <button type="button" class="btn" @click="dialogRef.close()">Close</button>
          <button type="submit" class="btn btn-primary">Create</button>
        </div>
      </form>
    </div>
  </dialog>
</template>

<style scoped>
.text-input {
  @apply input;
  @apply input-bordered;
  @apply w-full;
}
</style>
