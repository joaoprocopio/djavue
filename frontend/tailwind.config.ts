import { type Config } from "tailwindcss"

const config: Config = {
  important: true,
  corePlugins: {
    preflight: false
  },
  content: ["./index.html", "./src/**/*.vue"],
  theme: {
    extend: {}
  },
  plugins: []
}

export default config
