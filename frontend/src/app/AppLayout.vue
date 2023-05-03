<template>
  <VApp :theme="$theme.current">
    <component :is="$route?.meta?.layout ?? DefaultLayoutName">
      <slot />
    </component>
  </VApp>
</template>

<script setup lang="ts">
  import { useThemeStore } from "~/stores"
  import { DefaultLayoutName } from "@/config/constants/layouts"

  const $theme = useThemeStore()
</script>
