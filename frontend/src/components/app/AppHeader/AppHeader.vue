<template>
  <nav class="border-neutral-200 border-b-2 px-8">
    <div class="flex mx-auto max-w-screen-xl py-2">
      <RouterLink :to="{ name: 'home' }">
        <img
          class="h-12"
          src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Cat_black.svg" />
      </RouterLink>
    </div>
  </nav>
</template>
