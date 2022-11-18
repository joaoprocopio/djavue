<template>
  <nav class="flex border-neutral-100 border-b-2 px-4 py-2 mx-auto">
    <div>
      <RouterLink :to="{ name: 'home' }">
        <img
          style="height: 48px"
          src="https://upload.wikimedia.org/wikipedia/commons/a/ab/Cat_black.svg" />
      </RouterLink>
    </div>
  </nav>
</template>
