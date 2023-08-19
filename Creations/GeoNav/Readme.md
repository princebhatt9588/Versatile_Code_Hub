# Location Search App

This is a simple Python application built using the Tkinter library to create a graphical user interface (GUI) for searching locations on Google Maps. The app allows users to input a location and opens the Google Maps webpage for the specified location using the default web browser.

## Features

- User-friendly graphical interface.
- Input field to enter the location to be searched.
- "Search" button to initiate the search process.
- Utilizes the `webbrowser` module to open the Google Maps webpage with the entered location.

## Dependencies

- Python 3.x (Tested on Python 3.7)
- Tkinter: Python's standard GUI (Graphical User Interface) package.
- Pyperclip: A cross-platform clipboard module for copying and pasting text.

## Installation

1. Ensure you have Python 3.x installed on your system.
2. Install the required dependencies using the following command:
   ```
   pip install pyperclip
   ```

## Usage

1. Run the provided code using a Python interpreter.
2. A GUI window will appear with an input field and a "Search" button.
3. Enter the location you want to search in the input field.
4. Click the "Search" button.
5. The default web browser will open, directing you to the Google Maps webpage for the entered location.

## Code Explanation

The code uses Tkinter to create the GUI elements and Pyperclip to interact with the clipboard for copying and pasting text. Here's a breakdown of the code's structure:

- Import necessary modules: `tkinter`, `pyperclip`, and `webbrowser`.
- Set up the dimensions and appearance of the main window.
- Define a search function that opens the Google Maps webpage for the entered location.
- Create the GUI components: canvas, frame, entry, label, and button.
- Bind the search function to the "Search" button.
- Start the main event loop using `root.mainloop()`.


---

Feel free to modify and enhance the code as needed for your use case!

For a more interactive experience, you can explore the code further and experiment with different features and design elements.

For any questions or assistance, please reach out!