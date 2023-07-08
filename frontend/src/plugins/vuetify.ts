import "vuetify/styles"
import { createVuetify } from "vuetify"
import { aliases, md } from "vuetify/iconsets/md"

export const vuetify = createVuetify({
  defaults: {
    global: {
      elevation: 0
    }
  },
  icons: {
    defaultSet: "md",
    aliases,
    sets: {
      md
    }
  }
})
