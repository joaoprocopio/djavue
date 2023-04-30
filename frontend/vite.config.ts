import { alias, plugins } from "./configs"

import { defineConfig } from "vite"

const config = defineConfig(() => {
  return {
    plugins,
    server: {
      host: true,
      port: 3000,
    },
    resolve: {
      alias,
    },
    publicDir: "./src/public",
  }
})

export default config
