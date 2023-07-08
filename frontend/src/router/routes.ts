import { type RouteRecordRaw } from "vue-router"

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
        path: "/",
        component: lazyPage("LandingPage")
      }
    ]
  }
]
