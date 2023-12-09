import { createVuetify } from "vuetify"
import { aliases, md } from "vuetify/iconsets/md"

export default defineNuxtPlugin((app) => {
    const vuetify = createVuetify({
        ssr: true,
        defaults: {
            global: {
                elevation: 0
            },
            VIcon: {
                class: "material-icons-outlined"
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
