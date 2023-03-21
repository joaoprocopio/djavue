import { tasksSeeds } from "~/mocks/shared"

export const seeds = function (server) {
  server.loadFixtures()
  server.createList("task", tasksSeeds)
}
