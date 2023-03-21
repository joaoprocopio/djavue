import { Factory } from "miragejs"
import { faker } from "@faker-js/faker"

export const task = Factory.extend({
  title() {
    return faker.word.verb()
  },
})
