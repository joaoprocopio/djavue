import { mount, type VueWrapper } from "@vue/test-utils"

// import { useThemeStore } from "~/stores"

import App from "../App.vue"

let component: VueWrapper

const render = () => mount(App)

describe("App", () => {
  beforeEach(() => {
    component = render()
  })

  afterEach(() => {
    component.unmount()
  })

  test("It renders correctly", () => {
    expect(component.html()).toMatchSnapshot()
  })

  test("It renders with a theme - light", () => {
    expect(component.classes()).toContain("v-theme--light")
  })

  test("It renders with a theme - dark", () => {
    expect(component.classes()).toContain("v-theme--dark")
  })
})
