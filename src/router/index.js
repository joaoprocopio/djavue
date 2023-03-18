import { createRouter, createWebHistory } from "vue-router"
import { routes } from "./routes"

export const routerPlugin = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes,
})
