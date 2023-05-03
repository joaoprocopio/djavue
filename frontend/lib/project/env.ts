export const env = {
  DEV: import.meta.env.MODE === "development",
  MOCK: import.meta.env._MOCK === "true",
  API_URL: import.meta.env._API_URL,
}
