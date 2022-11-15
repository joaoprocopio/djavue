<template>
  <component
    :is="$props.tag"
    :disabled="$props.disabled || $props.loading"
    :class="classes"
    v-bind="$attrs">
    <slot />
  </component>
</template>

<script setup>
  import { computed } from "vue"

  const $props = defineProps({
    tag: {
      type: String,
      default: "button",
      validator: (value) =>
        ["button", "a", "label", "RouterLink"].includes(value),
    },
    block: {
      type: Boolean,
      default: false,
    },
    // disabled: boolean
    // loading: boolean
  })

  const classes = computed(() => ({
    "d-button": true,
    "d-button--block": $props.block,
  }))
</script>

<style lang="scss">
  .d-button {
    @apply bg-neutral-300 border-neutral-400;
    @apply font-bold;
    @apply border-2 rounded-lg;
    @apply px-4 py-2;

    &--block {
      @apply w-full;
    }

    &:hover {
      @apply bg-neutral-200 border-neutral-300;
    }

    &:active {
      @apply bg-neutral-100 border-neutral-200;
    }
  }
</style>
