import type { Plugin } from "vue"

import { AppLayoutName, LandingLayoutName } from "@/constants/layouts"
import { AppLayout, LandingLayout } from "~/layouts"

export const layoutPlugin: Plugin = {
  install(app) {
    app.component(AppLayoutName, AppLayout)
    app.component(LandingLayoutName, LandingLayout)
  },
}
