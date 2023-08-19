# PDF to Text Converter

This is a Python program that converts the text content from a PDF file into a text file. It utilizes the PyPDF2 library to read the PDF and extract text from its pages. The extracted text is then saved into a specified text file.

## Getting Started

1. **Installation**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Library Installation**: The program uses the PyPDF2 library. You can install it using the following command:
   ```
   pip install PyPDF2
   ```

3. **Running the Program**: To run the program, follow these steps:
   - Save the provided code in a Python file, e.g., `pdf_to_text_converter.py`.
   - Open a terminal or command prompt and navigate to the directory containing the `pdf_to_text_converter.py` file.
   - Run the program using the following command:
     ```
     python pdf_to_text_converter.py
     ```
   - Follow the prompts to input the paths for the PDF file and the desired output text file.

## Program Explanation

1. The program checks if a directory named "temp" exists. If not, it creates one to store temporary files.

2. It prompts the user to provide the paths for the PDF file and the output text file.

3. The program calculates a base directory (`BASEDIR`) where text files will be stored if no specific path is provided.

4. If no output text file path is provided, the program generates a default text file path based on the PDF file's name.

5. The PDF file is opened in binary read mode using the `open` function.

6. The PyPDF2 library is used to read the PDF file and extract the number of pages.

7. For each page in the PDF, the program extracts the text content using `getPage` and `extractText` methods.

8. The extracted text is appended to the specified text file using the `with open` statement.

9. The extracted text is also printed to the console for overview purposes.

10. After processing all pages, the PDF file is closed.

## Example Output

Suppose you have a PDF file named `sample.pdf` containing multiple pages with text content. You run the program and provide the following inputs:

```
Enter the name of your pdf file - please use backslash when typing in the directory path: /path/to/sample.pdf
Enter the name of your txt file - please use backslash when typing in the directory path: /path/to/output.txt
```

The program will read the PDF file, extract text from each page, and save the extracted text into the `output.txt` file. You can open the `output.txt` file to view the extracted text content.

---

Please replace `/path/to/sample.pdf` and `/path/to/output.txt` with the actual file paths you intend to use. Additionally, make sure to customize the README file according to your needs before including it in your project repository.

