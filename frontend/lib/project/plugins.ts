import type { PluginOption } from "vite"
import vue from "@vitejs/plugin-vue"
import vuetify from "vite-plugin-vuetify"

export const plugins: PluginOption[] = [vue(), vuetify()]
