import axios from "axios"

import { env } from "~/configs"

export const $axios = axios.create({
  baseURL: env.isDev && env.isMock ? "/api" : env.apiUrl,
  withCredentials: true,
  xsrfHeaderName: "X-CSRFToken",
  xsrfCookieName: "csrftoken",
})
