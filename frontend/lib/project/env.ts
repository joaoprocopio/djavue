export const env = {
  DEV: import.meta.env.MODE === "development",
  MOCK: import.meta.env.VITE_MOCK === "true",
  API_URL: import.meta.env.VITE_API_URL,
}
