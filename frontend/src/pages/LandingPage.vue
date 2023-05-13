<template>
  <VResponsive content-class="background">
    <VCard>
      <template #title>Djavue</template>
      <template #subtitle>Full-stack template project</template>
      <template #text>Built using Django, Vue and Postgres</template>
    </VCard>
  </VResponsive>
</template>

<style>
  .background {
    display: flex;
    align-items: center;
    justify-content: center;
    height: calc(100vh - 64px);
    background-image: url(https://images.unsplash.com/photo-1570458436416-b8fcccfe883f?ixlib=rb-4.0.3&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&q=80);
    background-size: cover;
    background-position: center;
  }
</style>
