import { DefaultLayout, ErrorLayout } from "~/layouts"

const layoutPlugin = {
  install(Vue) {
    Vue.component("DefaultLayout", DefaultLayout)
    Vue.component("ErrorLayout", ErrorLayout)
  },
}

export { layoutPlugin }
