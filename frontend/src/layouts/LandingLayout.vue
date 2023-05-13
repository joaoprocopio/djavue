<template>
  <VAppBar class="h-full">
    <template #prepend>
      <RouterLink class="text-h5 text-primary text-decoration-none font font-weight-bold" to="/">
        djavue
      </RouterLink>
    </template>
    <template #append>
      <VBtn append-icon="login" color="primary" class="mr-4">Entrar</VBtn>
    </template>
  </VAppBar>
  <VMain>
    <slot />
  </VMain>
</template>
