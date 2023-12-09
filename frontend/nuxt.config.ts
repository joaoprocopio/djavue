// https://nuxt.com/docs/api/configuration/nuxt-config
export default defineNuxtConfig({
    srcDir: "src",
    app: {
        head: {
            htmlAttrs: { lang: "pt-br" },
            charset: "utf-8",
            viewport: "width=device-width, initial-scale=1",
            title: "Construindo plataformas com qualidade",
            titleTemplate: "%s | Djavue",
            link: [
                { rel: "icon", type: "image/svg+xml", href: "/favicon.svg" },
                { rel: "preconnect", href: "https://fonts.googleapis.com" },
                { rel: "preconnect", href: "https://fonts.gstatic.com", crossorigin: "" },
                {
                    rel: "stylesheet",
                    href: "https://fonts.googleapis.com/css2?family=Roboto:wght@100;300;400;500;700;900&display=swap"
                },
                {
                    rel: "stylesheet",
                    href: "https://fonts.googleapis.com/css?family=Material+Icons|Material+Icons+Outlined|Material+Icons+Two+Tone|Material+Icons+Round|Material+Icons+Sharp"
                }
            ]
        }
    },
    devtools: { enabled: true }
})
