/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{html,js}"],
  theme: {
    extend: {textShadow: {
      'default': '2px 2px 4px rgba(0, 0, 0, 0.5)',
      'lg': '3px 3px 6px rgba(0, 0, 0, 0.5)',
      'xl': '4px 4px 8px rgba(0, 0, 0, 0.5)',
      'white': '2px 2px 4px rgba(255, 255, 255, 0.5)',
    },
    colors: {
      'sexyblue': '#7776B3',
      'purpleblue' : '#5A639C',
      'pinkpurple' : '#9B86BD',
      'lightpink' : '#E2BBE9'// Define the custom color with a name
    },},
  },
  plugins: [function ({ addUtilities }) {
    const newUtilities = {
      '.text-shadow': {
        'text-shadow': '2px 2px 4px rgba(0, 0, 0, 0.5)',
      },
      '.text-shadow-lg': {
        'text-shadow': '3px 3px 6px rgba(0, 0, 0, 0.5)',
      },
      '.text-shadow-xl': {
        'text-shadow': '4px 4px 8px rgba(0, 0, 0, 0.5)',
      },
      '.text-shadow-white': {
        'text-shadow': '2px 2px 4px rgba(255, 255, 255, 0.5)',
      },
      '.text-shadow-none': {
        'text-shadow': 'none',
      },
    }

    addUtilities(newUtilities, ['responsive', 'hover'])
  },],
}

