import { AppFooter, AppNavbar } from "~/components/app"

const appPlugin = {
  install(Vue) {
    Vue.component("AppFooter", AppFooter)
    Vue.component("AppNavbar", AppNavbar)
  },
}

export { appPlugin }
