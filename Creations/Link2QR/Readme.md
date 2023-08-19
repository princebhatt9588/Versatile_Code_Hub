**QR Code Generator using Python**

**Introduction:**
This code is a simple implementation of a QR code generator using the `qrcode` library in Python. It takes user input in the form of a website URL, creates a QR code representing the input URL, and then saves the QR code image in JPG format. The generated QR code image can be used to quickly access the provided website using QR code scanning apps or devices.

**Usage:**
1. Install Required Libraries:
   Make sure you have the `qrcode` library installed. If not, you can install it using the following command:
   ```
   pip install qrcode[pil]
   ```

2. Code Explanation:
   - The code starts by importing necessary modules. The `qrcode` library is used for generating QR codes, and specifically, the `qrcode.image.svg` module is imported to generate the QR code as an SVG image.
   - The user is prompted to enter the website URL for which the QR code needs to be generated.
   - The `qrcode.QRCode` class is initialized with specific parameters like version, box size, and border size. These parameters define the visual characteristics of the QR code.
   - The user-input URL is added to the QR code data using the `q.add_data()` method.
   - The `q.make(fit=True)` function generates the QR code pattern and fits it within the designated size.
   - The QR code is generated as an image using the `q.make_image()` function. The `fill` parameter specifies the color of the QR code pattern, and the `back_color` parameter specifies the background color.
   - The generated QR code image is saved in the "static" folder with the filename "qrcode.jpg".

**Output:**
After running the code and providing the input URL, a QR code image named "qrcode.jpg" will be generated and saved in the "static" folder of your project directory. This image can be scanned using any QR code scanning application to quickly access the provided website.

**Note:**
- Make sure you have the required libraries installed before running the code.
- Ensure that the "static" folder exists in the same directory as the script, or modify the path where the image is saved if needed.
- This code is a basic example and can be enhanced with error handling and more advanced features as needed.

**Sample Output:**
For example, if the user enters the website URL "https://www.example.com", the generated QR code will represent this URL, and the output QR code image will be saved as "qrcode.jpg" in the "static" folder.

Feel free to modify and adapt this code for your specific use case or integrate it into a larger project.