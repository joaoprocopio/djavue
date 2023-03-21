import { ActiveModelSerializer } from "miragejs"

export const serializers = {
  task: ActiveModelSerializer.extend({
    embed: true,
    root: false,
  }),
}
