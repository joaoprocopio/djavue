import { type RouteRecordRaw } from "vue-router"

import { LandingPageName } from "@/lib/constants/pages"

const lazyLayout = (layout: string) => () =>
  // @ts-ignore
  import(`~/layouts`).then(({ [layout]: Layout }) => Layout)

const lazyPage = (page: string) => () =>
  // @ts-ignore
  import(`~/pages`).then(({ [page]: Page }) => Page)

export const routes: Readonly<RouteRecordRaw[]> = [
  {
    path: "/",
    component: lazyLayout("LandingLayout"),
    children: [
      {
        name: LandingPageName,
        path: "/",
        component: lazyPage("LandingPage")
      },
      {
        path: "/:pathMatch(.*)*",
        component: lazyPage("ErrorPage")
      }
    ]
  }
]
