<template>
  <span
    :class="{ [variant]: true, [size]: $props.size }"
    v-text="$props.icon" />
</template>

<script setup>
  import { computed } from "vue"

  const $props = defineProps({
    icon: {
      type: String,
      required: true,
    },
    size: {
      type: String,
      default: "2xl",
      validator: (value) =>
        [
          "xs",
          "sm",
          "md",
          "lg",
          "xl",
          "2xl",
          "3xl",
          "4xl",
          "5xl",
          "6xl",
          "7xl",
          "8xl",
          "9xl",
        ].includes(value),
    },
    variant: {
      type: String,
      default: "filled",
      validator: (value) =>
        ["outlined", "filled", "rounded", "sharp", "two-tone"].includes(value),
    },
  })

  const variant = computed(() => {
    if ($props.variant === "filled") return "material-icons"

    return `material-icons-${$props.variant}`
  })

  const size = computed(() => {
    return `d-icon--size-${$props.size}`
  })
</script>

<style lang="scss">
  .d-icon {
    &--size-xs {
      font-size: 0.75rem;
    }
    &--size-sm {
      font-size: 0.875rem;
    }
    &--size-md {
      font-size: 1rem;
    }
    &--size-lg {
      font-size: 1.125rem;
    }
    &--size-xl {
      font-size: 1.25rem;
    }
    &--size-2xl {
      font-size: 1.5rem;
    }
    &--size-3xl {
      font-size: 1.875rem;
    }
    &--size-4xl {
      font-size: 2.25rem;
    }
    &--size-5xl {
      font-size: 3rem;
    }
    &--size-6xl {
      font-size: 3.75rem;
    }
    &--size-7xl {
      font-size: 4.5rem;
    }
    &--size-8xl {
      font-size: 6rem;
    }
    &--size-9xl {
      font-size: 8rem;
    }
  }
</style>
