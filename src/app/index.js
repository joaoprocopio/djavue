import { createApp } from "vue"

import { mockServer } from "~/mocks"
import { installPlugins } from "~/plugins"
import { env } from "~/configs"

if (env.isDev && env.isMock) {
  mockServer()
}

import App from "./App.vue"

export const app = createApp(App)

installPlugins(app)

app.mount("#__vue")
