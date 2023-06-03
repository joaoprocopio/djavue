import { config } from "@vue/test-utils"

import { routerPlugin } from "~/router"
import { vuetifyPlugin } from "~/plugins/vuetify"
import { layoutPlugin } from "~/plugins/layout"

config.global.plugins = [vuetifyPlugin, routerPlugin, layoutPlugin]
