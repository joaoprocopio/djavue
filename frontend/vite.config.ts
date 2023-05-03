import { plugins } from "./lib/project/plugins"
import { alias } from "./lib/project/alias"

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
