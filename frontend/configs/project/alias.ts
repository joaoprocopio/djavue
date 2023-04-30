import { fileURLToPath, URL } from "node:url"

export const alias = {
  "@": fileURLToPath(new URL("../../", import.meta.url)),
  "~": fileURLToPath(new URL("../../src", import.meta.url)),
}
