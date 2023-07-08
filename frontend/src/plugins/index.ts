import { type App } from "vue"

import { router } from "~/router"

import { pinia } from "./pinia"

export const install = (app: App) => {
  app.use(router)
  app.use(pinia)
}
