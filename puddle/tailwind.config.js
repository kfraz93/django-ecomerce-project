/** @type {import('tailwindcss').Config} */
module.exports = {
  // Configure Tailwind to scan your Django templates for class names
  content: [
    // Scan all HTML files in any subdirectory
    './**/*.html',
    // Scan all JS files in any subdirectory, BUT IGNORE node_modules
    './**/*.js',
    '!./node_modules/**', // EXCLUDE node_modules directory
  ],
  darkMode: 'class',
  theme: {
    extend: {},
  },
  plugins: [],
}