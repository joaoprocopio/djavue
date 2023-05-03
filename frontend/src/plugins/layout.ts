import type { Plugin } from "vue"

import { DefaultLayoutName } from "@/configs/constants/layouts"
import { DefaultLayout } from "~/layouts"

export const layoutPlugin: Plugin = {
  install(app) {
    app.component(DefaultLayoutName, DefaultLayout)
  },
}
