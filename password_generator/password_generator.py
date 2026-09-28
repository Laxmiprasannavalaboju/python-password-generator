import random
import string


def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""

    for _ in range(length):
        password += random.choice(characters)

    return password


print("===== PASSWORD GENERATOR =====")

while True:
    try:
        length = int(input("Enter password length (minimum 4): "))

        if length < 4:
            print("Password length must be at least 4.")
        else:
            password = generate_password(length)

            print("\nGenerated Password:", password)

            again = input("\nGenerate another password? (yes/no): ").lower()

            if again != "yes":
                print("Password Generator closed.")
                break

    except ValueError:
        print("Please enter a valid number.")