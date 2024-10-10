character = input("Please enter your string :")
count: int= 0
for char in character :
    if char in "aeiouAEIOU":
     count +=1
print(count)


'''
string=input("Enter string:")
vowels=0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
print("Number of vowels are:")
print(vowels)
'''