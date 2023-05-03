import { createApp } from "vue"

import { env } from "@/configs/project/env"
import { installPlugins } from "~/plugins"
import App from "./App.vue"

if (env.DEV && env.MOCK) {
  // TODO: Mock related code
}

const app = createApp(App)

installPlugins(app)

app.mount("#__vue")
