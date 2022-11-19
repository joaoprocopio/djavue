import { AppFooter, AppHeader } from "~/components/app"

const appPlugin = {
  install(Vue) {
    Vue.component("AppFooter", AppFooter)
    Vue.component("AppHeader", AppHeader)
  },
}

export { appPlugin }
