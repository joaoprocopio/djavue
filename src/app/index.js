import { createApp } from "vue"

import { installPlugins } from "~/plugins"

import App from "./App.vue"
import "~/assets/main.css"

export const app = createApp(App)

installPlugins(app)

app.mount("#__vue")
