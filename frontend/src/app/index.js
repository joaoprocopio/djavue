import { createApp } from "vue"
import { createPinia } from "pinia"
import { router } from "~/router"
import { layoutPlugin } from "~/plugins"
import App from "~/app/App.vue"

const app = createApp(App)
const pinia = createPinia()

app.use(pinia)
app.use(router)
app.use(layoutPlugin)

app.mount("#app")

export { app }
