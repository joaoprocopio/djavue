<template>
  <VResponsive class="mx-auto" :max-width="thresholds.sm">
    <VCard class="mt-8">
      <VCardTitle class="mb-2">
        <h1>Sorry</h1>
      </VCardTitle>
      <VCardSubtitle class="mb-4">
        <p class="text-h6">The page that you requested don't exist</p>
      </VCardSubtitle>
      <VCardText>
        <VBtn :to="{ name: LandingPageName }" color="primary" append-icon="arrow_right_alt">
          Go to the landing page
        </VBtn>
      </VCardText>
    </VCard>
  </VResponsive>
</template>

<script setup lang="ts">
  import { useDisplay } from "vuetify"
  import { LandingPageName } from "@/constants/pages"

  const { thresholds } = useDisplay()
</script>
