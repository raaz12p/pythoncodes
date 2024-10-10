'''import random
import string
print("Welcome to Random Password Generator Program")
def main():

     length = int(input("Enter the length of password:"))
     lowerD = ascii_letters
     upperD = ascii_uppercase
     digitD = digits
     symbolsD = punctuation
     combine = lowerD+upperD+digitD+symbolsD
     x = random.sample(combine,length)
     password = "".join(x)
     print(password)
     main()
main()'''

import random
from string import ascii_letters, ascii_uppercase, digits, punctuation

print("Welcome to Random Password Generator Program")


def main():
     length = int(input("Enter the length of password:"))
     lower = ascii_letters
     upper = ascii_uppercase
     digit = digits
     symbols = punctuation
     combine = lower + upper + digit + symbols
     x = random.sample(combine, length)
     password = "".join(x)
     print(password)


main()