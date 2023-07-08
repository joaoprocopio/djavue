<template>
  <VAppBar>
    <RouterLink :to="{ name: LandingPageName }">
      <VIcon icon="forum"></VIcon>
    </RouterLink>
  </VAppBar>
  <VMain>
    <RouterView />
  </VMain>
</template>

<script setup lang="ts">
  import { LandingPageName } from "@/lib/constants/pages"
</script>
