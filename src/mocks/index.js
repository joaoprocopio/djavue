import { createServer } from "miragejs"

import { routes } from "./routes"
import { models } from "./models"
import { serializers } from "./serializers"
import { seeds } from "./seeds"
import { factories } from "./factories"

const config = function (environment) {
  const config = {
    environment,
    routes,
    models,
    serializers,
    seeds,
    factories,
  }

  return config
}

export const mockServer = function ({ environment = "development" } = {}) {
  return createServer(config(environment))
}
