import { DButton } from "~/components/ui/atoms"

const atomsPlugin = {
  install(Vue) {
    Vue.component("DButton", DButton)
  },
}

export { atomsPlugin }
