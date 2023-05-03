import "vuetify/styles"

import { createVuetify } from "vuetify"
import { aliases, md } from "vuetify/iconsets/md"

import * as components from "vuetify/components"
import * as directives from "vuetify/directives"

export const vuetifyPlugin = createVuetify({
  defaults: {
    global: {
      elevation: "0",
      variant: "text",
    },
  },
  components,
  directives,
  icons: {
    defaultSet: "md",
    aliases,
    sets: {
      md,
    },
  },
})
