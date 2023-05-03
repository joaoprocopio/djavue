import axios from "axios"

import { env } from "@/project/env"

export const $axios = axios.create({
  baseURL: env.DEV && env.MOCK ? "/api" : env.API_URL,
  withCredentials: true,
  xsrfHeaderName: "X-CSRFToken",
  xsrfCookieName: "csrftoken",
})
