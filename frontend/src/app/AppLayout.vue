<template>
  <VApp>
    <component :is="$route?.meta?.layout ?? DefaultLayoutName">
      <slot />
    </component>
  </VApp>
</template>

<script setup lang="ts">
  import { DefaultLayoutName } from "@/configs/constants"
</script>
