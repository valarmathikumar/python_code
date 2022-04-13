"""Given an array of integers. Find the largest sum of 3 integersGiven an array of integers. Find the largest sum of 3 integers"""

array=[1,5,8,6,7,9,9,9]
print("Enter the array:",array)

# convert list to set for remove duplicate values and make it in ascending order
number_set=set(array)
new_list=list(number_set)

total = new_list[len(new_list)-1] + new_list[len(new_list)-2] + new_list[len(new_list)-3]

print("sum of three largest number:",total)