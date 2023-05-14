/// <reference types="vite/client" />

import "vue-router"

interface ImportMetaEnv {
  readonly _MOCK: string
  readonly _API_URL: string
}

interface RouterLayoutMeta {
  name?: string
  isSimple?: boolean
}

declare module "vue-router" {
  interface RouteMeta {
    layout?: RouterLayoutMeta
  }
}
