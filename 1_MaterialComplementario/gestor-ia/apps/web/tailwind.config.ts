import type { Config } from "tailwindcss";

const config: Config = {
  content: ["./app/**/*.{ts,tsx}", "./components/**/*.{ts,tsx}"],
  theme: {
    extend: {
      colors: {
        ink: "#151515",
        cream: "#fff7ed",
        clay: "#f4b183",
        moss: "#2a7f62",
        ocean: "#0a3d62",
        ember: "#e4572e",
      },
      fontFamily: {
        display: ["\"Space Grotesk\"", "sans-serif"],
        body: ["\"IBM Plex Sans\"", "sans-serif"],
      },
      boxShadow: {
        card: "0 18px 40px rgba(0,0,0,0.12)",
      },
    },
  },
  plugins: [],
};

export default config;
