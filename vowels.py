"""Find vowels in a word"""

word = input("Enter the sentence:")
string = word.lower()

# get each character from string and increment the count variable if that char is found in vowels list
count = 0
vowels = ['a','e','i','o','u']
vowels_found = []
for char in string:
    if char in vowels:
        count = count+1
        vowels_found.append(char)

print("Number of vowels: ",count,"(",''.join(vowels_found),")")