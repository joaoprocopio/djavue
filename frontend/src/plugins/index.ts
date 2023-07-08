import { type App } from "vue"

import { pinia } from "./pinia"
import { vuetify } from "./vuetify"

export const install = (app: App) => {
  app.use(pinia)
  app.use(vuetify)
}
