import type { App } from "vue"

import { piniaPlugin } from "./pinia"

export const installPlugins = (Vue: App) => {
  Vue.use(piniaPlugin)
}
