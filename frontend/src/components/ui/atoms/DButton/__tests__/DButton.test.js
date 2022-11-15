import { render } from "@testing-library/vue"

import { describe, test, expect } from "vitest"

import DButton from "../DButton.vue"

describe("DButton", () => {
  test("Renders like expected.", () => {
    const { html } = render(DButton)
    expect(html()).toMatchSnapshot()
  })
})
