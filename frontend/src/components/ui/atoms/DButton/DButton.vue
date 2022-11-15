<template>
  <component
    :is="$props.tag"
    :disabled="$props.disabled"
    :class="{
      'd-button': true,
      'd-button--block': $props.block,
      [`d-button--${$props.variant}`]: true,
      [`text-${$props.color}`]: $props.color,
    }"
    v-bind="$attrs">
    <span class="d-button__label">
      <slot />
    </span>
  </component>
</template>

<script setup>
  import "./DButton.scss"

  const $props = defineProps({
    tag: {
      type: String,
      default: "button",
      validator: (value) =>
        ["button", "a", "label", "RouterLink"].includes(value),
    },
    variant: {
      type: String,
      default: "filled",
      validator: (value) => ["filled", "outlined", "text"].includes(value),
    },
    background: {
      type: String,
      default: "green-900",
    },
    color: {
      type: String,
      default: "green-900",
    },
    block: {
      type: Boolean,
      default: false,
    },
    disabled: {
      type: Boolean,
      default: false,
    },
    // loading: boolean
  })
</script>
