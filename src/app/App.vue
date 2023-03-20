<template>
  <VApp>
    <component :is="$route?.meta?.layout?.name ?? DefaultLayoutName">
      <RouterView />
    </component>
  </VApp>
</template>

<script setup>
  import { DefaultLayoutName } from "~/constants"
</script>
