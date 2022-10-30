const express = require("express")

const app = express()
const port = 8001

app.use(express.json())

const user = express.Router()

app.use("/api/user", user)

user.get("/whoami", (req, res) => {
  res.status(200).json({ authenticated: false })
})

app.listen(port, () => {
  console.log(`server running on: http://localhost:${port}`)
})
