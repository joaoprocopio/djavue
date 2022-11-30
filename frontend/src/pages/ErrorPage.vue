<template>
  <section>
    <h1>Page not found</h1>
    <p>
      Sorry, the page
      <span v-text="path" />
      could not be found.
    </p>
    <RouterLink :to="{ name: 'home' }">Go back to the home page</RouterLink>
  </section>
</template>

<script setup>
  import { useRoute } from "vue-router"

  const path = useRoute().fullPath
</script>
