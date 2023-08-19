# OTP Generator

This is a simple OTP (One-Time Password) generator program written in Python. The program generates numeric OTPs of a specified length and allows you to generate multiple OTPs at once. Each OTP is valid for 10 minutes.

## Usage

1. Clone this repository to your local machine or download the [Python script](otp_generator.py) directly.
2. Make sure you have Python installed on your machine.
3. Open a terminal or command prompt and navigate to the directory containing the `otp_generator.py` file.
4. Run the script using the following command:

   ```
   python otp_generator.py
   ```

5. Follow the on-screen instructions to provide the desired OTP length (minimum 4) and the number of OTPs you want to generate.

## Example

Suppose you want to generate 3 numeric OTPs, each with a length of 6 digits. Here's an example interaction with the program:

```
Welcome to OTP Generator!
Enter the number of digits for OTP (minimum 4): 6
How many numeric OTPs do you want to generate? 3
Generated Numeric OTP: 593816
This OTP is valid for 10 minutes.
Time left: 09:59
Generated Numeric OTP: 421739
This OTP is valid for 10 minutes.
Time left: 09:58
Generated Numeric OTP: 874560
This OTP is valid for 10 minutes.
Time left: 09:57
OTP generation completed.
```

In this example, the program generates three numeric OTPs, each with a length of 6 digits. It displays each OTP along with a countdown timer indicating the time left for its validity.
