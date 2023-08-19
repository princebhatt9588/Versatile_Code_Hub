#Doc_to_PDF_Converter

# -*- coding: utf-8 -*-

import os
import PyPDF2
import docx2txt
from reportlab.pdfgen import canvas

def convert_to_pdf(input_path, output_path):
    _, input_extension = os.path.splitext(input_path)
    _, output_extension = os.path.splitext(output_path)

    if input_extension.lower() == '.docx':
        text = docx2txt.process(input_path)
    else:
        raise ValueError("Unsupported input format")

    if output_extension.lower() == '.pdf':
        c = canvas.Canvas(output_path)
        width, height = c._pagesize

        text_lines = text.split('\n')
        y = height - 50

        for line in text_lines:
            c.drawString(50, y, line)
            y -= 15

        c.save()
    else:
        raise ValueError("Unsupported output format")

if os.path.isdir("temp") == False:
    os.mkdir("temp")

input_path = input("Enter the path of your input document: ")
output_path = input("Enter the path for the output PDF file: ")

convert_to_pdf(input_path, output_path)
