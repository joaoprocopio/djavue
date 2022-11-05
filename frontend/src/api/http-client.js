import axios from "axios"

const httpClient = axios.create({
  xsrfHeaderName: "X-CSRFToken",
  xsrfCookieName: "csrftoken",
  baseURL: "http://localhost:8000",
  withCredentials: true,
  timeout: 60000,
})

export { httpClient }
