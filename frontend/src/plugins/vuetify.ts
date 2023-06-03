import "vuetify/styles"

import { createVuetify } from "vuetify"

import { aliases, md } from "vuetify/iconsets/md"

import * as components from "vuetify/components"
import * as labsComponents from "vuetify/labs/components"
import * as directives from "vuetify/directives"

export const vuetify = createVuetify({
  directives,
  components: {
    ...components,
    ...labsComponents,
  },
  icons: {
    defaultSet: "md",
    aliases,
    sets: {
      md,
    },
  },
})
