<template>
  <div>I am a Home Page</div>
</template>

<script setup>
  import { $axios } from "~/api"

  $axios.get("/tasks/")
</script>
