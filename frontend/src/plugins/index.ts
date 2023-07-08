import { type App } from 'vue'

import { vuetify } from './vuetify'

export const install = (app: App) => {
  app.use(vuetify)
}
