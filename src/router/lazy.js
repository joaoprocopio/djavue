export const HomePageLazy = () =>
  import("~/pages/HomePage").then(({ HomePage }) => HomePage)
