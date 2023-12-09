import { createVuetify } from "vuetify"

export default defineNuxtPlugin((app) => {
    const vuetify = createVuetify({
        ssr: true,
        defaults: {
            global: {
                elevation: 0
            }
        }
    })

    app.vueApp.use(vuetify)
})
