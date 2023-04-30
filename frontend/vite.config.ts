import { alias, plugins } from "./configs"

import { defineConfig } from "vite"

export default defineConfig({
  plugins,
  server: {
    host: true,
    port: 3000,
  },
  resolve: {
    alias,
  },
  publicDir: "./src/public",
})
