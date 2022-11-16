<template>
  <span
    :class="{ [$props.variant]: true }"
    v-text="$props.icon" />
</template>

<script setup>
  const $props = defineProps({
    icon: {
      type: String,
      required: true,
    },
    variant: {
      type: String,
      default: "material-icons",
    },
  })
</script>
