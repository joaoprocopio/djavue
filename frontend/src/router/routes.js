import LandingPage from "~/pages/LandingPage.vue"
import ErrorPage from "~/pages/ErrorPage.vue"

const routes = [
  {
    path: "/",
    name: "landing",
    component: LandingPage,
  },
  {
    path: "/:pathMatch(.*)*",
    name: "not-found",
    component: ErrorPage,
    meta: {
      layout: {
        name: "ErrorLayout",
      },
    },
  },
]

export { routes }
