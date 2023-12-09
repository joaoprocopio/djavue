import { createVuetify } from "vuetify"
import { aliases, md } from "vuetify/iconsets/md"

export default defineNuxtPlugin((app) => {
    const vuetify = createVuetify({
        ssr: true,
        defaults: {
            global: {
                elevation: 0
            }
        },
        icons: {
            defaultSet: "md",
            aliases,
            sets: { md }
        }
    })

    app.vueApp.use(vuetify)
})
