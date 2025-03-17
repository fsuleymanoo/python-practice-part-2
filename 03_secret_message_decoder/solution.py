# do not change the method name
def main():
    encoded = input("Enter the encoded message: ")
    step = int(input("Enter the step size: "))
    is_valid = step > 0
    is_valid or print("Error message")
    decoded = encoded[::step]
    print(f"Decoded Message: {decoded}")
# do not change the following lines:    
if __name__ == "__main__":
    main()