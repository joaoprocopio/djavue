import App from "../App.vue"

import { useThemeStore } from "~/stores"

import { render } from "@testing-library/vue"
import { createTestingPinia } from "@pinia/testing"

const wrapper = render(App, {
  global: {
    plugins: [createTestingPinia()],
  },
})

const $theme = useThemeStore()

describe("App", () => {
  it("Theme renders - light", () => {
    $theme.current = "light"

    console.log(wrapper.html())
  })
})
