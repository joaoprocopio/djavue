import { HomePageName } from "~/constants"

export const routes = [
  {
    path: "/",
    name: HomePageName,
    component: () =>
      import("~/pages/HomePage").then(({ HomePage }) => HomePage),
  },
]
