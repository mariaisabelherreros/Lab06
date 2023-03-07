def encoder(password):
    new_password = ""
    for element in password:
        element = int(element)
        element += 3
        element = str(element)
        new_password += element
    return new_password

def decoder(password):
    new_password = ""
    for element in password:
        element = int(element)
        element -= 3
        element = str(element)
        new_password += element
    return new_password

def main():
    while True:
        print("Menu")
        print("-------------")
        print("1. Encode ")
        print("2. Decode ")
        print("3. Quit")
        print()
        option = int(input("Please enter an option: "))
        print()

        if option == 1:
            password = input("Please enter your password to encode: ")
            print("Your password has been encoded and stored!")
            encoded_password = encoder(password)
            print()

        elif option == 2:
            print(f"The encoded password is {encoded_password}, and the original password is {password}.")
            print()

        elif option == 3:
            break

if __name__ == "__main__":
    main()
