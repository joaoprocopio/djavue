export const reject = (error) => {
  Promise.reject(error)

  return error.response
}
