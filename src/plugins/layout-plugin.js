import { DefaultLayout } from "~/layouts"
import { DefaultLayoutName } from "~/constants"

export const layoutPlugin = {
  install(Vue) {
    Vue.component(DefaultLayoutName, DefaultLayout)
  },
}
