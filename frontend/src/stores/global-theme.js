import { ref, computed } from "vue"
import { defineStore } from "pinia"

export const useGlobalTheme = defineStore("useGlobalTheme", () => {
  const theme = ref("light")

  const current = computed(() => theme.value)

  const toggleTheme = () =>
    (theme.value = theme.value === "light" ? "dark" : "light")

  return { theme, current, toggleTheme }
})
