<template>
  <div>Page not found</div>
  <div>Sorry, the page {{ fullPath }} could not be found.</div>
  <RouterLink :to="{ name: 'home' }">Go back to the home page</RouterLink>
</template>

<script setup>
  import { useRoute } from "vue-router"

  const fullPath = useRoute().fullPath
</script>
