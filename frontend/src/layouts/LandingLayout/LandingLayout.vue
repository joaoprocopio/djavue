<script setup lang="ts">
  import { ChatBubbleLeftRightIcon } from "@heroicons/vue/24/solid"

  import { LandingPageName } from "@/lib/constants/pages"
  import { AppContainer } from "~/components"
</script>

<template>
  <AppContainer
    component="header"
    class="h-16"
    content-class="flex items-center">
    <RouterLink :to="{ name: LandingPageName }">
      <ChatBubbleLeftRightIcon class="h-8" />
    </RouterLink>
  </AppContainer>
  <main>
    <RouterView />
  </main>
</template>
