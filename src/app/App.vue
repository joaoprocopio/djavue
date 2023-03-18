<template>
  <component :is="$route?.meta?.layout?.name ?? DefaultLayoutName">
    <RouterView />
  </component>
</template>

<script setup>
  import { DefaultLayoutName } from "~/constants"
</script>
