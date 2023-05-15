import { plugins } from "./lib/project/plugins"
import { alias } from "./lib/project/alias"

import { defineConfig } from "vite"
import { configDefaults } from "vitest/config"

export default defineConfig(() => {
  return {
    plugins,
    envPrefix: "_",
    server: {
      host: true,
      port: 3000,
    },
    resolve: {
      alias,
    },
    test: {
      globals: true,
      environment: "jsdom",
      exclude: [...configDefaults.exclude, "./e2e/**"],
    },
  }
})
