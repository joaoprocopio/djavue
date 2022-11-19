<template>
  <footer class="bg-neutral-200 px-8">
    <div class="flex flex-col mx-auto max-w-screen-xl py-8 h-48">
      <RouterLink
        class="font-mono font-bold pb-2 underline"
        :to="{ name: 'home' }"
        >d-já vue!
      </RouterLink>
      <p>Maybe, you haven't seen nothing like this.</p>
    </div>
  </footer>
</template>
