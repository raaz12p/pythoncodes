string = input("Enter a String ")
count = 0
for char in string:
    if char in "aeiouAEIOU":
        count += 1

        print("the number of vowels in the string is : ", count)
