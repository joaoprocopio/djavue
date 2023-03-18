import { HomePageName } from "~/constants"
import { HomePageLazy } from "./lazy"

export const routes = [
  {
    path: "/",
    name: HomePageName,
    component: HomePageLazy,
  },
]
