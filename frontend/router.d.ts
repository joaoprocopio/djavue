import "vue-router"

interface RouterLayoutMeta {
  name?: string
  isSimple?: boolean
}

declare module "vue-router" {
  interface RouteMeta {
    layout?: RouterLayoutMeta
  }
}
