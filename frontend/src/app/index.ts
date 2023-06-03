import { createApp } from "vue"

import { install } from "~/plugins"
import App from "./App.vue"

const app = createApp(App)

install(app)

app.mount("#__vue")
