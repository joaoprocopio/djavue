import type { RouteRecordRaw } from "vue-router"

import { LandingPageName } from "@/configs/constants"

export const routes: Readonly<RouteRecordRaw[]> = [
  {
    path: "/",
    name: LandingPageName,
    component: () => import("~/pages").then(({ LandingPage }) => LandingPage),
  },
]
