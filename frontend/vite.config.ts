import { defineConfig } from "vite"
import { fileURLToPath, URL } from "node:url"

import vue from "@vitejs/plugin-vue"

export default defineConfig({
  plugins: [vue()],
  server: {
    host: "0.0.0.0",
    port: 3000,
  },
  resolve: {
    alias: {
      "@": fileURLToPath(new URL("./src", import.meta.url)),
    },
  },
})
