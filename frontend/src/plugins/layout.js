import { DefaultLayout, ErrorLayout, SimpleLayout } from "~/layouts"

const layoutPlugin = {
  install(Vue) {
    Vue.component("DefaultLayout", DefaultLayout)
    Vue.component("ErrorLayout", ErrorLayout)
    Vue.component("SimpleLayout", SimpleLayout)
  },
}

export { layoutPlugin }
