import component from "../App.vue"

import { useThemeStore } from "~/stores"

import { render } from "@testing-library/vue"
import { createTestingPinia } from "@pinia/testing"
import { describe, it, expect, vi } from "vitest"

const App = render(component, {
  global: {
    plugins: [
      createTestingPinia({
        createSpy: vi.fn(),
      }),
    ],
  },
})

const $theme = useThemeStore()

describe("App", () => {
  it("Theme renders - light", () => {
    $theme.current = "light"

    // TODO: consertar o vitest não resolvendo os componentes

    expect(App).toMatchSnapshot()
  })
})
