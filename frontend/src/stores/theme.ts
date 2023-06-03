import { computed, ref } from "vue"
import { defineStore } from "pinia"

const THEME = {
  light: "light",
  dark: "dark",
}

export const useThemeStore = defineStore("theme", () => {
  const current = ref(THEME.light)

  const theme = computed(() => current.value)

  const toggleTheme = () =>
    (current.value = current.value === THEME.light ? THEME.dark : THEME.light)

  return { current, theme, toggleTheme }
})
