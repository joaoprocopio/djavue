import type { RouteRecordRaw } from "vue-router"

import { LandingLayoutName } from "@/constants/layouts"
import { LandingPageName } from "@/constants/pages"

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
]
