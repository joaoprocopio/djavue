export const env = {
  isDev: import.meta.env.MODE === "development",
  isMock: import.meta.env.VITE_API_MOCK === "true",
  apiUrl: import.meta.env.VITE_API_URL,
}
