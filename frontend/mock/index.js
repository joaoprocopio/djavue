import { db } from "./db/index.js"
import express from "express"
import cors from "cors"
import dayjs from "dayjs"
import utc from "dayjs/plugin/utc.js"
import { randomUUID } from "node:crypto"

const app = express()
const port = 8001

app.use(express.json())
app.use(cors())

dayjs.extend(utc)

const user = express.Router()
app.use("/api/user", user)
user.post("/login", async (request, response) => {
  const { username, password } = request.body

  try {
    const user = db.data.user.find(
      (user) => user.username === username && user.password === password
    )

    const lastLogin = dayjs().utc().toString()
    const expireDate = dayjs().utc().add(15, "days").toString()

    const sessionid = randomUUID()

    user.last_login = lastLogin

    db.data.session.push({
      session_key: sessionid,
      session_data: user,
      expire_date: expireDate,
    })

    await db.write()

    response
      .cookie("sessionid", sessionid, { httpOnly: true })
      .status(200)
      .send(user)
  } catch {
    response.status(404).send({}).end()
  }
})

user.get("/whoami", (request, response) => {
  try {
    response.status(200).send({
      user: user,
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
