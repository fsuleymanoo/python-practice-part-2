# do not change the method name
def main():
    number = input(
        "Enter a 10-digit phone number, no spaces, special characters or spaces: ")
    if len(number) == 10:
        phone_number = f"({number[:3]}) {number[3:7]}-{number[6:]}"
        print(f"Formatted Phone Number: {phone_number}")
    else:
        print("Error: Please enter exactly 10 digits. \nNo spaces, special characters and alphabetical characters.")


# do not change the code below
if __name__ == "__main__":
    main()
