<script setup>
  import { RouterLink, RouterView } from "vue-router"
  import HelloWorld from "./components/HelloWorld.vue"
</script>

<template>
  <header>
    <img alt="Vue logo" class="logo" width="125" height="125" />

    <div class="wrapper">
      <HelloWorld msg="You did it!" />

      <nav>
        <RouterLink to="/"> Home </RouterLink>
        <RouterLink to="/about"> About </RouterLink>
      </nav>
    </div>
  </header>

  <RouterView />
</template>
