<template>
  <div>
    <VResponsive
      class="mx-auto"
      :content-class="`pa-4 ${$props.contentClass}`"
      :max-width="thresholds.md">
      <slot />
    </VResponsive>
  </div>
</template>

<script lang="ts">
  interface Props {
    contentClass: string
  }
</script>

<script setup lang="ts">
  import { useDisplay } from "vuetify"

  const { thresholds } = useDisplay()
  const $props = withDefaults(defineProps<Props>(), {
    contentClass: "",
  })
</script>
