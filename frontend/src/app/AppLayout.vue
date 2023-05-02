<template>
  <VApp :theme="$theme.current">
    <component :is="$route?.meta?.layout ?? DefaultLayoutName">
      <slot />
    </component>
  </VApp>
</template>

<script setup lang="ts">
  import { useThemeStore } from "~/stores"
  import { DefaultLayoutName } from "@/configs/constants"

  const $theme = useThemeStore()
</script>
