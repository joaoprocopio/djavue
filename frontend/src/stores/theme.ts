import { ref } from "vue"
import { defineStore } from "pinia"

export const useThemeStore = defineStore("theme", () => {
  const current = ref("dark")

  const toggleTheme = () => (current.value = current.value === "light" ? "dark" : "light")

  return { current, toggleTheme }
})
