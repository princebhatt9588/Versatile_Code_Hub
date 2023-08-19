# Document to PDF Converter

This Python program allows you to convert various document formats (such as DOCX) to PDF. It utilizes the `docx2txt` library to extract text content from DOCX files and the `reportlab` library to generate PDFs. The program provides a simple way to convert documents to PDF format, preserving the text content.

## Getting Started

1. **Installation**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Library Installation**: The program requires the `docx2txt` and `reportlab` libraries. Install them using the following commands:
   ```
   pip install python-docx2txt
   pip install reportlab
   ```

3. **Running the Program**: To use the program, follow these steps:
   - Save the provided code in a Python file, e.g., `document_to_pdf_converter.py`.
   - Open a terminal or command prompt and navigate to the directory containing the `document_to_pdf_converter.py` file.
   - Run the program using the following command:
     ```
     python document_to_pdf_converter.py
     ```
   - Follow the prompts to input the path of the input document and the desired output PDF file.

## Program Explanation

1. The program checks if a directory named "temp" exists. If not, it creates one to store temporary files.

2. It prompts the user to provide the path of the input document and the path for the output PDF file.

3. The `convert_to_pdf` function is responsible for handling the conversion process. It first checks the extensions of the input and output paths to determine compatibility.

4. If the input document is a DOCX file, the `docx2txt` library is used to extract text content.

5. The extracted text is then added to a PDF using the `reportlab` library. The text is placed line by line on the PDF page.

6. The generated PDF is saved to the specified output path.

## Example Output

Suppose you have a DOCX file named `sample.docx` containing text content. You run the program and provide the following inputs:

```
Enter the path of your input document: /path/to/sample.docx
Enter the path for the output PDF file: /path/to/output.pdf
```

The program will convert the content of the `sample.docx` document into a PDF and save it as `output.pdf`. You can open the `output.pdf` file to view the converted content.

Please ensure to replace `/path/to/sample.docx` and `/path/to/output.pdf` with the actual file paths you intend to use. Adjust the README file to match your project's specifics before including it in your repository.
