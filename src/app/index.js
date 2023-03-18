import { createApp } from "vue"

import { installPlugins } from "~/plugins"

import App from "./App.vue"

export const app = createApp(App)

installPlugins(app)

app.mount("#__vue")
