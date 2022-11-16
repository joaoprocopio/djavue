import { DIcon } from "~/components/ui/atoms"

const atomsPlugin = {
  install(Vue) {
    Vue.component("DIcon", DIcon)
  },
}

export { atomsPlugin }
