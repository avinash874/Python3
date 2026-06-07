'''
• L1.fort): updates the list to [1,2,7,8, 15,21]
• L1.reverse(): updates the list to [15,21,2,7,8, 1]
• L1.append(8): adds 8 at the end of the list
• L1.insert(3,8): This will add 8 at 3 index
• L1.pop(2): Will delete element at index 2 and return its value.
• L1.remove(21): Will remove 21 from the list.
• L1.clear(): Will clear the list and make it empty.
'''


friends = ["apple", "Orange" , 5, 355.06, "false", "Avinash", "Rahul"]
# print(friends)
friends.append("Shreya")
# print(friends)
friends.insert(3, "Vikas")
# print(friends)


l1 = [1,4,6,8,9,33,44,22,11]
l1.sort()
l1.reverse()
l1.insert(3,33333) #This will add 33333 at 3 index
l1.remove(22) #Will remove 22 from the list.
print(l1)
