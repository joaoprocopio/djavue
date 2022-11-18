<template>
  <section>
    <h1 class="text-3xl font-bold mb-12">Page not found</h1>
    <p class="mb-8">
      Sorry, the page
      <code
        class="px-2 py-1 bg-neutral-100 font-bold rounded"
        v-text="path" />
      could not be found.
    </p>
    <RouterLink
      class="font underline text-blue-400"
      :to="{ name: 'home' }"
      >Go back to the home page</RouterLink
    >
  </section>
</template>

<script setup>
  import { useRoute } from "vue-router"

  const path = useRoute().fullPath
</script>
