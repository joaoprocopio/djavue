<template>
  <section class="py-16">
    <h1 class="text-4xl font-bold mb-8">Page not found</h1>
    <p class="text-lg mb-6 break-all">
      Sorry, the page
      <span
        class="px-2 py-1 font-mono bg-neutral-100 font-bold rounded"
        v-text="path" />
      could not be found.
    </p>
    <RouterLink
      class="font underline text-blue-500"
      :to="{ name: 'home' }"
      >Go back to the home page</RouterLink
    >
  </section>
</template>

<script setup>
  import { useRoute } from "vue-router"

  const path = useRoute().fullPath
</script>
