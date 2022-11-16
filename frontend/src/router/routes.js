import HomePage from "~/pages/HomePage.vue"
import ErrorPage from "~/pages/ErrorPage.vue"

const routes = [
  {
    path: "/",
    name: "home",
    component: HomePage,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "error",
    component: ErrorPage,
    meta: {
      layout: {
        name: "ErrorLayout",
      },
    },
  },
]

export { routes }
