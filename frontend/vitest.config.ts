import { mergeConfig } from "vite"
import { configDefaults, defineConfig } from "vitest/config"

import viteConfig from "./vite.config"

export default mergeConfig(
  viteConfig,
  defineConfig(() => {
    return {
      test: {
        environment: "jsdom",
        exclude: [...configDefaults.exclude, "./e2e/**"],
      },
    }
  })
)
