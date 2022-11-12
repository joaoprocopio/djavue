/* eslint-env node */
require("@rushstack/eslint-patch/modern-module-resolution")
module.exports = {
  root: true,
  extends: [
    "eslint:recommended",
    "plugin:vue/vue3-essential",
    "plugin:prettier/recommended",
    "@vue/eslint-config-prettier",
    "plugin:storybook/recommended",
  ],
  overrides: [
    {
      files: ["cypress/e2e/**/*.{cy,spec}.{js,ts,jsx,tsx}"],
      extends: ["plugin:cypress/recommended"],
    },
  ],
  parserOptions: {
    ecmaVersion: "latest",
  },
}
