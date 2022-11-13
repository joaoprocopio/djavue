import { DButton } from "~/components/app/atoms"

const atomsPlugin = {
  install(Vue) {
    Vue.component("DButton", DButton)
  },
}

export { atomsPlugin }
