<script setup lang="ts"></script>

<template>
  <div class="card bg-base-100 shadow-lg w-96">
    <div class="card-body">
      <div class="card-title justify-center">Page Not Found</div>
      <div class="card-actions justify-center mt-12">
        <router-link :to="{ name: 'profile-list' }" class="btn btn-primary">Return</router-link>
      </div>
    </div>
  </div>
</template>
