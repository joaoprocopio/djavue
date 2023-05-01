import type { App } from "vue"

import { routerPlugin } from "~/router"
import { vuetifyPlugin } from "./vuetify"
import { piniaPlugin } from "./pinia"
import { layoutPlugin } from "./layout"

export const installPlugins = (app: App) => {
  app.use(piniaPlugin).use(vuetifyPlugin).use(routerPlugin).use(layoutPlugin)
}
