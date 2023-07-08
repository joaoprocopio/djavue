<template>
  <component :is="$props.component" class="max-w-6xl mx-auto">
    <div class="h-full px-8" :class="$props.contentClass">
      <slot />
    </div>
  </component>
</template>

<script setup lang="ts">
  const $props = defineProps({
    component: {
      type: String,
      default: "div"
    },
    contentClass: {
      type: String,
      default: ""
    }
  })
</script>
