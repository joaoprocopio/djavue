import { $axios } from "~/api"

export const get = (resource, params) => {
  return $axios.get(resource, { params })
}

export const post = (resource, data, params) => {
  return $axios.post(resource, data, { params })
}
