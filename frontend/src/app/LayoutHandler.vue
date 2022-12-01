<template>
  <v-app :theme="$globalTheme.theme">
    <component :is="layout">
      <slot />
    </component>
  </v-app>
</template>

<script setup>
  import { useGlobalTheme } from "~/stores"
  import { computed } from "vue"
  import { useRoute } from "vue-router"

  const $globalTheme = useGlobalTheme()

  const route = useRoute()
  const layout = computed(() => route?.meta?.layout?.name || "DefaultLayout")
</script>
