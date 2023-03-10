/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["../ming/routes/templates/*.html", "../ming/routes/templates/static/js/*.js"],
  theme: {
    extend: {},
  },
  plugins: [require('@tailwindcss/forms')],
}
