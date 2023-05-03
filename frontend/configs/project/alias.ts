import type { AliasOptions } from "vite"
import { join, resolve } from "node:path"

const BASE_URL = join(__dirname, "..", "..")

export const alias: AliasOptions = {
  "@": resolve(BASE_URL),
  "~": resolve(BASE_URL, "src"),
}
