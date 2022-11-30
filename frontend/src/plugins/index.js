import vuetify from "./vuetify"

import { layoutPlugin } from "./layout"

import router from "~/router"
import { createPinia } from "pinia"

const pinia = createPinia()

export function registerPlugins(app) {
  app.use(pinia)
  app.use(router)
  app.use(vuetify)
  app.use(layoutPlugin)
}
