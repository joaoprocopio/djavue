import { devices, defineConfig } from "@playwright/test"

const baseURL = {
  preview: "http://localhost:3001",
  dev: "http://localhost:3000",
}

export default defineConfig({
  testDir: "./e2e",
  fullyParallel: true,
  forbidOnly: !!process.env.CI,
  retries: process.env.CI ? 2 : 0,
  workers: process.env.CI ? 1 : undefined,
  reporter: "html",
  use: {
    headless: true,
    baseURL: process.env.CI ? baseURL.preview : baseURL.dev,
    trace: "on-first-retry",
  },
  projects: [
    {
      name: "chromium",
      use: { ...devices["Desktop Chrome"] },
    },

    {
      name: "firefox",
      use: { ...devices["Desktop Firefox"] },
    },
    {
      name: "webkit",
      use: { ...devices["Desktop Safari"] },
    },
  ],
  webServer: {
    command: process.env.CI ? "npm run preview" : "npm run dev",
    url: process.env.CI ? baseURL.preview : baseURL.dev,
    reuseExistingServer: !process.env.CI,
  },
})
