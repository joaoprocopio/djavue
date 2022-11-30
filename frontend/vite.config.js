import vue from "@vitejs/plugin-vue"
import vuetify from "vite-plugin-vuetify"

import { fileURLToPath, URL } from "node:url"
import { defineConfig } from "vite"

// https://vitejs.dev/config/
export default defineConfig(() => {
  return {
    plugins: [vue(), vuetify({ autoImport: true })],
    resolve: {
      alias: {
        "~": fileURLToPath(new URL("./src", import.meta.url)),
        "@": fileURLToPath(new URL("./", import.meta.url)),
      },
    },
    build: {
      sourcemap: true,
    },
    server: {
      host: "0.0.0.0",
      port: 3000,
    },
    test: {
      root: "src/",
      environment: "jsdom",
    },
    publicDir: "./src/public/",
  }
})
