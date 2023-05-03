import type { RouteRecordRaw } from "vue-router"

import { LandingPageName } from "@/config/constants/pages"

export const routes: Readonly<RouteRecordRaw[]> = [
  {
    path: "/",
    name: LandingPageName,
    component: () => import("~/pages").then(({ LandingPage }) => LandingPage),
  },
]
