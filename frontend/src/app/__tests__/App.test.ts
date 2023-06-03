import { createPinia, setActivePinia } from "pinia"
import { mount, type VueWrapper } from "@vue/test-utils"

import App from "../App.vue"

let wrapper: VueWrapper
const render = () => mount(App)

beforeAll(() => {
  global.ResizeObserver = class ResizeObserver {
    observe() {}
    unobserve() {}
    disconnect() {}
  }
})

describe("App", () => {
  beforeEach(() => {
    setActivePinia(createPinia())

    wrapper = render()
  })

  afterEach(() => {
    wrapper.unmount()
  })

  it("Theme renders - light", () => {
    expect(wrapper.html()).toMatchSnapshot()
  })
})
