// imports
const db = require("./db")
const express = require("express")
const crypto = require("node:crypto")

// startup and configuration
const app = express()
const port = 8001

// middleware
app.use(express.json())

// routers
const user = express.Router()
app.use("/api/user", user)
user.post("/login", (req, res) => {
  const { username, password } = req.body

  try {
    const user = db.user.find(
      (user) => user.username === username && user.password === password
    )

    const sessionid = crypto.randomUUID()

    res.cookie("sessionid", sessionid).status(200).send({
      id: user.id,
      name: user.name,
      username: user.username,
      first_name: user.first_name,
      last_name: user.last_name,
      email: user.email,
    })
  } catch (error) {
    res.status(404).send({ error: error }).end()
  }
})

// server
app.listen(port, () => {
  console.log(`server running on: http://localhost:${port}`)
})
