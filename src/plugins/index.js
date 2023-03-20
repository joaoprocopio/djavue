import { routerPlugin } from "~/router"
import { layoutPlugin } from "./layout-plugin"
import { piniaPlugin } from "./pinia-plugin"
import { vuetifyPlugin } from "./vuetify-plugin"

export const installPlugins = (app) => {
  app.use(routerPlugin)
  app.use(layoutPlugin)
  app.use(piniaPlugin)
  app.use(vuetifyPlugin)
}
