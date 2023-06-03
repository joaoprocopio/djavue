import type { Plugin } from "vue"

import { LandingLayoutName, AppLayoutName } from "@/lib/constants/layouts"
import { LandingLayout, AppLayout } from "~/layouts"

export const layouts: Plugin = {
  install(app) {
    app.component(LandingLayoutName, LandingLayout)
    app.component(AppLayoutName, AppLayout)
  },
}
