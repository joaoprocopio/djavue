import { Response } from "miragejs"

export const tasks = function (server) {
  server.config({
    routes() {
      this.namespace = "/api/tasks/"

      this.get("/", function (schema) {
        return new Response(
          200,
          {},
          {
            tasks: this.serialize(schema.tasks.all()),
          }
        )
      })
    },
  })
}
