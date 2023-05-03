import { plugins } from "./config/project/plugins"
import { alias } from "./config/project/alias"

import { defineConfig } from "vite"

export default defineConfig(() => {
  return {
    plugins,
    server: {
      host: true,
      port: 3000,
    },
    resolve: {
      alias,
    },
  }
})
