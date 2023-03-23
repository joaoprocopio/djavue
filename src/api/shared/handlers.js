export const resolve = (response) => response

export const reject = ({ response }) => {
  Promise.reject(response)

  return response
}
