import { vuetifyPlugin } from "./vuetify"

import { layoutPlugin } from "./layout"

import { piniaPlugin } from "./pinia"
import { routerPlugin } from "~/router"

export function registerPlugins(app) {
  app.use(piniaPlugin)
  app.use(routerPlugin)
  app.use(vuetifyPlugin)
  app.use(layoutPlugin)
}
