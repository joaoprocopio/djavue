const fs = require("fs")
const path = require("path")

module.exports = {
  user: JSON.parse(fs.readFileSync(path.resolve(__dirname, "user.json"))),
}
