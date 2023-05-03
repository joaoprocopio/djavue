import type { AliasOptions } from "vite"

import { fileURLToPath, URL } from "node:url"

const BASE_URL = "../../"

export const alias: AliasOptions = {
  "@": fileURLToPath(new URL(BASE_URL + "lib", import.meta.url)),
  "~": fileURLToPath(new URL(BASE_URL + "src", import.meta.url)),
}
