import type { App } from "vue"

import { DefaultLayoutName } from "@/configs/constants"
import { DefaultLayout } from "~/layouts"

export const layoutPlugin = {
  install(app: App) {
    app.component(DefaultLayoutName, DefaultLayout)
  },
}
