// TODO: quebrar test para vitest config

import { plugins } from "./lib/project/plugins"
import { alias } from "./lib/project/alias"

import { defineConfig } from "vite"
import { configDefaults } from "vitest/config"

export default defineConfig({
  plugins,
  resolve: {
    alias,
  },
  envPrefix: "_",
  server: {
    host: true,
    port: 3000,
  },
  preview: {
    host: true,
    port: 3001,
  },
  test: {
    globals: true,
    environment: "jsdom",
    exclude: [...configDefaults.exclude, "./e2e/**"],
  },
})
