// imports
const express = require("express")
const cors = require("cors")
const crypto = require("node:crypto")

// startup and configuration
const app = express()
const port = 8001

// middleware
app.use(express.json())
app.use(cors())

// routers
const user = express.Router()
app.use("/api/user", user)
user.post("/login", (request, response) => {
  const { username, password } = request.body

  try {
    const user = db.user.find((user) => {
      user.username === username && user.password === password
    })

    const sessionid = crypto.randomUUID()
    const lastLogin = new Date().toUTCString()

    user.last_login = lastLogin

    response
      .cookie("sessionid", sessionid, { httpOnly: true })
      .status(200)
      .send({
        id: user.id,
        name: user.name,
        username: user.username,
        first_name: user.first_name,
        last_name: user.last_name,
        email: user.email,
        last_login: lastLogin,
      })
  } catch {
    response.status(404).send({}).end()
  }
})

user.get("/whoami", (request, response) => {
  try {
    response.status(200).send({
      user: {
        id: user.id,
        name: user.name,
        username: user.username,
        first_name: user.first_name,
        last_name: user.last_name,
        email: user.email,
      },
      authenticated: true,
    })
  } catch {
    response.status(404).send({
      authenticated: false,
    })
  }
})

// server
app.listen(port, () => {
  console.log(`server running on: http://localhost:${port}`)
})
