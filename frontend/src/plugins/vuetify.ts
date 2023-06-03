import "vuetify/styles"

import { createVuetify } from "vuetify"
import { aliases, md } from "vuetify/iconsets/md"

export const vuetifyPlugin = createVuetify({
  defaults: {
    global: {
      elevation: 0,
    },
  },
  icons: {
    defaultSet: "md",
    aliases,
    sets: {
      md,
    },
  },
})
