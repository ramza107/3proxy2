import type { Config } from "tailwindcss";

const config: Config = {
  content: [
    "./src/pages/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/components/**/*.{js,ts,jsx,tsx,mdx}",
    "./src/app/**/*.{js,ts,jsx,tsx,mdx}",
  ],
  theme: {
    extend: {
      colors: {
        lime: {
          DEFAULT: "#c8ff00",
          dim: "#9fcc00",
          glow: "#e8ff66",
        },
        void: "#050507",
        ink: "#0a0a0f",
        mist: "#8a8f9e",
      },
      fontFamily: {
        display: ["var(--font-bebas)", "system-ui", "sans-serif"],
        sans: ["var(--font-dm)", "system-ui", "sans-serif"],
      },
      backgroundImage: {
        "grid-fade":
          "linear-gradient(to bottom, rgba(5,5,7,0) 0%, rgba(5,5,7,0.85) 55%, rgba(5,5,7,1) 100%), radial-gradient(ellipse 80% 50% at 50% -20%, rgba(200,255,0,0.12), transparent)",
        noise:
          "url(\"data:image/svg+xml,%3Csvg viewBox='0 0 256 256' xmlns='http://www.w3.org/2000/svg'%3E%3Cfilter id='n'%3E%3CfeTurbulence type='fractalNoise' baseFrequency='0.85' numOctaves='4' stitchTiles='stitch'/%3E%3C/filter%3E%3Crect width='100%25' height='100%25' filter='url(%23n)' opacity='0.04'/%3E%3C/svg%3E\")",
      },
      animation: {
        "slow-pan": "pan 22s ease-in-out infinite alternate",
        shimmer: "shimmer 3s ease-in-out infinite",
      },
      keyframes: {
        pan: {
          "0%": { transform: "translateY(0) scale(1)" },
          "100%": { transform: "translateY(-2%) scale(1.02)" },
        },
        shimmer: {
          "0%, 100%": { opacity: "0.45" },
          "50%": { opacity: "1" },
        },
      },
    },
  },
  plugins: [],
};

export default config;
