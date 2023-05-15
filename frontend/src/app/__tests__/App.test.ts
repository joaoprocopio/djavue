import App from "../App.vue"

import { render } from "@testing-library/vue"

const component = (options = {}) =>
  render(App, {
    ...options,
  })

describe("App", () => {
  it("Theme renders - light", () => {
    const { html } = component()

    // TODO: Unknown file extension ".css"

    expect(html()).toMatchSnapshot()
  })
})
