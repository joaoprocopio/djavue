<template>
  <VResponsive class="mx-auto px-4 py-2" :max-width="$props.maxWidth">
    <slot />
  </VResponsive>
</template>

<script setup>
  const $props = defineProps({
    maxWidth: {
      type: String,
      validator: (v) => ["800px", "1200px", "100%"].includes(v),
      default: "1200px",
    },
  })
</script>
