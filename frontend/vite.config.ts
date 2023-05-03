import { plugins } from "./configs/project/plugins"
import { alias } from "./configs/project/alias"

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
