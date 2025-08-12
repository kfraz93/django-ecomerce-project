/** @type {import('tailwindcss').Config} */
module.exports = {
  // Add the path to your input.css file to the content array.
  content: [
    './**/*.html',
    './**/*.js',
    './**/*.css', // <-- Make sure this line is included
    '!./node_modules/**',
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
}
