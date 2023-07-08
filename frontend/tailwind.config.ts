import { type Config } from "tailwindcss"

import { fontFamily } from "tailwindcss/defaultTheme"

const config: Config = {
  content: ["./index.html", "./src/**/*.vue"],
  theme: {
    extend: {
      fontFamily: {
        sans: ["Inter", ...fontFamily.sans]
      }
    }
  },
  plugins: []
}

export default config
