import type { RouteRecordRaw } from "vue-router"

import { LandingLayoutName } from "@/constants/layouts"
import { LandingPageName, ErrorPageName } from "@/constants/pages"

export const routes: Readonly<RouteRecordRaw[]> = [
  {
    path: "/",
    name: LandingPageName,
    meta: {
      layout: {
        name: LandingLayoutName,
      },
    },
    component: () => import("~/pages").then(({ LandingPage }) => LandingPage),
  },
  {
    path: "/:pathMatch(.*)*",
    name: ErrorPageName,
    meta: {
      layout: {
        name: LandingLayoutName,
        isSimple: true,
      },
    },
    component: () => import("~/pages").then(({ ErrorPage }) => ErrorPage),
  },
]
