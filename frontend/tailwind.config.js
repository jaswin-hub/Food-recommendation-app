/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  darkMode: 'class',
  theme: {
    extend: {
      colors: {
        primary: "#F97316", // deep orange
        background: {
          light: "#FFF7ED", // cream white
          dark: "#1C1917",
        },
        surface: {
          light: "#FFFFFF",
          dark: "#292524",
        },
        text: {
          light: "#292524",
          dark: "#FEF3C7",
        },
        accent: {
          green: "#84CC16",
          brown: "#78350F",
        }
      },
      fontFamily: {
        sans: ['Inter', 'sans-serif'],
      }
    },
  },
  plugins: [],
}
