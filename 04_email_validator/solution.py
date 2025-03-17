# do not change the method name
def main():
    email = input("Enter an email address: ")
    at_index=email.find("@")
    dot_index=email.rfind(".")

    if (
        "@" in email
        and "." in email
        and " " not in email
        and email.count("@") == 1
        and 0 < email.find("@") < len(email) - 1
        and 0 < email.find(".") < len(email) - 1
        and at_index + 1 < dot_index
    ):

        print("Valid email address!")
    else:
        print("Invalid email")


        # do not change the following lines:
main()
