import { fileURLToPath, URL } from "node:url"

import { defineConfig } from "vite"
import vue from "@vitejs/plugin-vue"

// https://vitejs.dev/config/
export default defineConfig({
  plugins: [vue()],
  preview: {
    host: false,
    port: 3001,
  },
  server: {
    host: false,
    port: 3000,
  },
  envPrefix: "_",
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./", import.meta.url)),
      "~": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
})
