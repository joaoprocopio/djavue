import type { App } from "vue"

import { router } from "~/router"
import { pinia } from "./pinia"
import { vuetify } from "./vuetify"
import { layouts } from "./layouts"

export const install = (app: App) => {
  app.use(pinia).use(router).use(vuetify).use(layouts)
}
