/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./pages/*.jsx",
    "./App.jsx",
    "./main.jsx",
  ],
  theme: {
    extend: {
      animation: {
        'bounce': 'bounce 1s infinite',
      },
    },
  },
  plugins: [],
}
