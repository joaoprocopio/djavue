import { mergeConfig } from "vite"
import { configDefaults, defineConfig } from "vitest/config"
import { fileURLToPath } from "node:url"

import viteConfig from "./vite.config"

export default mergeConfig(
  viteConfig,
  defineConfig({
    test: {
      environment: "jsdom",
      exclude: [...configDefaults.exclude],
      root: fileURLToPath(new URL("./src", import.meta.url)),
    },
  })
)
