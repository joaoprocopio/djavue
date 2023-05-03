export const env = {
  get DEV(): boolean {
    return import.meta.env.MODE === "development"
  },
  get MOCK(): boolean {
    return import.meta.env.VITE_MOCK === "true"
  },
  get API_URL(): string {
    return import.meta.env.VITE_API_URL
  },
}
