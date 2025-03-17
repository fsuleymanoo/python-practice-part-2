# do not change the method name
def main():
    message = input("Enter a message: ")
    message = message.replace("with ", " w/ ")
    message = message.replace("for ", " 4 ")
    message = message.replace("to ", " 2 ")
    message = message.replace("and ", " & ")
    message = message.replace("at ", " @ ")
    if len(message) > 160:
        short_message = message.strip()
        print(f"Shortened message (160 chars): {short_message[:157]}" + "...")
    else: 
        print(f"{message}")    


# do not change the following lines:
main()
