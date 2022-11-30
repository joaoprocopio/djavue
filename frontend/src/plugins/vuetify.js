import "vuetify/styles"

import { createVuetify } from "vuetify"
import { aliases, md } from "vuetify/iconsets/md"

export default createVuetify({
  icons: {
    defaultSet: "md",
    aliases,
    sets: {
      md,
    },
  },
})
