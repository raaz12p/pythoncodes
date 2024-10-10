import random

from Palindrome import string
from string import ascii_letters, ascii_uppercase, digits, punctuation

 print("Welcome to Random Password Generator Program")
    def main():
     length = int(input("Enter the length of password:"))
     lower = ascii_letters
     upper = ascii_uppercase
     digit = string.digits
     symbols = string.punctuation
     combine = lower + upper + digit + symbols
     x = random.sample(combine, length)
     password = "".join(x)
     print(password)

main()