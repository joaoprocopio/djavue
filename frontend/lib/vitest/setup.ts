import { config } from "@vue/test-utils"
import { createTestingPinia } from "@pinia/testing"

import { router } from "~/router"
import { vuetify } from "~/plugins/vuetify"
import { layouts } from "~/plugins/layouts"

config.global.plugins = [createTestingPinia({ stubActions: false }), router, vuetify, layouts]

beforeAll(() => {
  global.ResizeObserver = class ResizeObserver {
    observe() {}
    unobserve() {}
    disconnect() {}
  }
})
