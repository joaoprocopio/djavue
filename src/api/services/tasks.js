import { reject, resolve, get } from "~/api"

const getTasks = async (params) =>
  get("/tasks", params)
    .then((response) => resolve(response))
    .catch((response) => reject(response))

export const TasksServices = {
  getTasks,
}
