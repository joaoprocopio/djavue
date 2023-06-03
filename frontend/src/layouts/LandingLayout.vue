<template>
  <VAppBar class="h-full">
    <template #prepend>
      <RouterLink
        class="text-h5 font-weight-bold text-primary text-decoration-none"
        :to="{ name: LandingPageName }">
        djavue
      </RouterLink>
    </template>
    <template #append>
      <VBtn append-icon="login" color="primary" class="mr-4">Login</VBtn>
    </template>
  </VAppBar>
  <VMain>
    <slot />
  </VMain>
</template>

<script setup lang="ts">
  import { LandingPageName } from "@/lib/constants/pages"
</script>
