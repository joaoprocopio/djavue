<template>
  <div class="text-3xl font-bold mb-12">Page not found</div>
  <div class="mb-8">
    Sorry, the page
    <code class="px-2 py-1 bg-neutral-100 font-bold rounded">{{
      fullPath
    }}</code>
    could not be found.
  </div>
  <RouterLink
    class="underline text-blue-500"
    :to="{ name: 'home' }"
    >Go back to the home page</RouterLink
  >
</template>

<script setup>
  import { useRoute } from "vue-router"

  const fullPath = useRoute().fullPath
</script>
