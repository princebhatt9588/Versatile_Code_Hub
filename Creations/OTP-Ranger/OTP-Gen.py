import random
import time

# s_char for small letters
s_char = "abcdefghijklmnopqrstuvwxyz"
# b_char for capital letters
b_char = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# d_char for digits
d_char = "123456789"


class Otp:
    def __init__(self, len):
        self.len = len

    def generate_otp(self, char_set):
        result = random.sample(char_set, self.len)
        otp = "".join(result)
        return otp

    def generate_numeric_otp(self):
        return self.generate_otp(d_char)

    def generate_bd_otp(self):
        char_set = b_char + d_char
        return self.generate_otp(char_set)

    def generate_sd_otp(self):
        char_set = s_char + d_char
        return self.generate_otp(char_set)

    def generate_sbd_otp(self):
        char_set = s_char + b_char + d_char
        return self.generate_otp(char_set)


def main():
    print("Welcome to OTP Generator!")

    while True:
        try:
            otp_length = int(input("Enter the number of digits for OTP (minimum 4): "))
            if otp_length < 4:
                print("Please enter a value of at least 4.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    while True:
        try:
            otp_count = int(input("How many numeric OTPs do you want to generate? "))
            if otp_count < 1:
                print("Please enter a value of at least 1.")
            else:
                break
        except ValueError:
            print("Please enter a valid number.")

    otp_generator = Otp(otp_length)

    for _ in range(otp_count):
        numeric_otp = otp_generator.generate_numeric_otp()
        print(f"Generated Numeric OTP: {numeric_otp}")
        print("This OTP is valid for 10 minutes.")

        start_time = time.time()
        validity_period = 10 * 60  # 10 minutes in seconds

        while True:
            current_time = time.time()
            elapsed_time = current_time - start_time

            if elapsed_time >= validity_period:
                print("OTP has expired.")
                break

            time_left = int(validity_period - elapsed_time)
            mins, secs = divmod(time_left, 60)
            print(f"Time left: {mins:02d}:{secs:02d}", end="\r")

            time.sleep(1)

        print()

    print("OTP generation completed.")

if __name__ == "__main__":
    main()
