import { join, resolve } from "node:path"

const BASE_URL = join(__dirname, "..", "..")

export const alias = {
  "@": resolve(BASE_URL),
  "~": resolve(BASE_URL, "src"),
}
