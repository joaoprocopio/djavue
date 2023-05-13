<template>
  <VAppBar> </VAppBar>
  <VMain>
    <slot />
  </VMain>
  <VBottomNavigation v-if="$display.mobile"></VBottomNavigation>
</template>

<script setup lang="ts">
  import { useDisplay } from "vuetify"

  const $display = useDisplay()
</script>
