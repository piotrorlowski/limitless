/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    '../**/static/**/*.js',
    '../**/templates/**/*.html',
    '../**/templates/**/*.svg',
    '../limitless/settings.py',
    './src/**/*.{vue,js,ts,jsx,tsx}'
  ],
  theme: {
    extend: {},
    fontFamily: {
      sans: ['Roboto', 'ui-sans-serif', 'system-ui', 'sans-serif']
    }
  },
  plugins: [require('daisyui')],
  daisyui: {
    themes: ['cupcake']
  },
  future: {
    hoverOnlyWhenSupported: true
  }
}
