<template>
  <VApp :theme="$theme.theme">
    <component :is="$route?.meta?.layout?.name ?? AppLayoutName">
      <RouterView />
    </component>
  </VApp>
</template>

<script setup lang="ts">
  import { useThemeStore } from "~/stores"
  import { AppLayoutName } from "@/lib/constants/layouts"

  const $theme = useThemeStore()
</script>
