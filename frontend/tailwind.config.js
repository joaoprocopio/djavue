/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/app/**/*.{vue,js}",
    "./src/layouts/**/*.{vue,js}",
    "./src/pages/**/*.{vue,js}",
    "./src/components/app/**/*.{vue,js}",
    "./src/components/ui/atoms/**/*.{vue,js}",
    "./src/components/ui/molecules/**/*.{vue,js}",
  ],
  safelist: [
    {
      pattern: /(bg|text)-./,
    },
  ],
  theme: {
    fontFamily: {
      sans: ["Roboto"],
      mono: ["Roboto Mono"],
      serif: ["Roboto Slab"],
    },
    extend: {},
  },
  plugins: [],
}
