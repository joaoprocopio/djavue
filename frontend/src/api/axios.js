import axios from "axios"

const $axios = axios.create({
  xsrfHeaderName: "X-CSRFToken",
  xsrfCookieName: "csrftoken",
  baseURL: "http://localhost:8000/api/",
  withCredentials: true,
  timeout: 60000,
})

export { $axios }
