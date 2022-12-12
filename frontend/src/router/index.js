import { createRouter, createWebHistory } from "vue-router"
import { routes } from "./routes"

const routerPlugin = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})

export { routerPlugin }
