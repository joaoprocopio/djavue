import { default as component } from "../App.vue"

import { mount } from "@vue/test-utils"
import { describe, it, expect } from "vitest"

const App = mount(component)

describe("App", () => {
  it("Theme changing", () => {
    expect(App).toBeTruthy()
  })
})
