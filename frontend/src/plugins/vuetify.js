import "vuetify/styles"

import { createVuetify } from "vuetify"
import { aliases, md } from "vuetify/iconsets/md"

const vuetifyPlugin = createVuetify({
  icons: {
    defaultSet: "md",
    aliases,
    sets: {
      md,
    },
  },
})

export { vuetifyPlugin }
