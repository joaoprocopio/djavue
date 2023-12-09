// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    app: {
        head: {
            htmlAttrs: {
                lang: "pt-br"
            },
            charset: "utf-8",
            viewport: "width=device-width, initial-scale=1",
            title: "Construindo plataformas com qualidade",
            titleTemplate: "%s | Djavue",
            link: [{ rel: "icon", type: "image/svg+xml", href: "/favicon.svg" }]
        }
    },
    devtools: {
        enabled: true
    },
    srcDir: "src"
})
