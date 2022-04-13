"""QUESTION: find intersection of two arrays"""

list1=[1,2,3,4,5,6]
list2=[1,3,5]
list3=[]
# I used in operator so it will check all the numbers in the list, even we change the size of list2 to higher than list1
for i in list1:
    if i in list2:
        list3.append(i)
print("Answer is:\n",list3)