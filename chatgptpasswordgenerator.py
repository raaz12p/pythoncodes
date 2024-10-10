import random
import string

def generate_password(length=int(input())):
    # Combine letters, digits, and punctuation
    characters = string.ascii_letters + string.digits + string.punctuation
    # Randomly select characters from the combined string
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

# Generate a random password of specified length
password_length = (int(input))
random_password = generate_password(password_length)
print(f"Generated Password: {random_password}")
