import random
import string

def generate_password(length, complexity):
    if complexity == 1:
        characters = string.ascii_letters
    elif complexity == 2:
        characters = string.ascii_letters + string.digits
    elif complexity == 3:
        characters = string.ascii_letters + string.digits + string.punctuation
    else:
        print("Invalid complexity level. Choose between 1, 2, and 3.")
        return None
    
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def main():
    try:
        length = int(input("Enter the length of the password: "))
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
        return

    print("Choose the complexity level:")
    print("1. Letters only")
    print("2. Letters and digits")
    print("3. Letters, digits, and special characters")
    complexity = int(input("Enter the complexity level (1/2/3): "))

    password = generate_password(length, complexity)
    if password:
        print(f"Generated Password: {password}")

if __name__ == "__main__":
    main()
