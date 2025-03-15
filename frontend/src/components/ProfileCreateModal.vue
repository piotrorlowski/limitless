<script setup lang="ts">
import { ref, computed } from 'vue'
import { useMutation } from '@tanstack/vue-query'
import { useProfileStore } from '@/stores/profile'
import type { Profile, ValidationErrors } from '@/interfaces/models'

const profiles = useProfileStore()
const dialogRef = ref<HTMLDialogElement | null>(null)
const errors = ref<Record<string, string[]>>({})

defineExpose({ dialog: dialogRef })

const mutation = useMutation<Profile, ValidationErrors, FormData>({
  mutationFn: (formData) => profiles.create(formData),
  onSuccess: () => {
    dialogRef.value?.close()
    errors.value = {}
  },
  onError: (error) => {
    if (error) {
      errors.value = error
    } else {
      console.error('Unexpected error:', error)
    }
  }
})

async function submit(event: Event) {
  event.preventDefault()
  errors.value = {}
  const formElement = event.target as HTMLFormElement
  const formData = new FormData(formElement)
  try {
    await mutation.mutateAsync(formData)
    formElement.reset()
  } catch (error) {
    console.error('Mutation failed:', error)
  }
}

const isPending = computed(() => mutation.isPending.value)
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
          <p v-if="errors.first_name" class="text-red-500 text-sm">
            {{ errors.first_name[0] }}
          </p>
          <input
            id="last_name"
            name="last_name"
            class="text-input"
            type="text"
            placeholder="Last Name"
          />
          <p v-if="errors.last_name" class="text-red-500 text-sm">
            {{ errors.last_name[0] }}
          </p>
          <input id="email" name="email" class="text-input" type="email" placeholder="Email" />
          <p v-if="errors.email" class="text-red-500 text-sm">
            {{ errors.email[0] }}
          </p>
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
          <p v-if="errors.avatar" class="text-red-500 text-sm">
            {{ errors.avatar[0] }}
          </p>
        </div>

        <div class="modal-action">
          <button type="button" class="btn" @click="dialogRef?.close()">Close</button>
          <button type="submit" class="btn btn-primary" :disabled="isPending">
            {{ isPending ? 'Creating...' : 'Create' }}
          </button>
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
