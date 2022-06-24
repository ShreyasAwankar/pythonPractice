"""List Comprehension."""
# ls = []
# for i in range (100):
#     if i%3 == 0:
#         ls.append(i)
# print (ls) #This is a normal method.
#
# ls = [i for i in range(100) if i%3==0]
# print (ls) #List comprehension for same program as above.

# item_no = int(input("How many items do you want to input: "))
# user_list1 = [list(map(int, input(f'Enter value : ').split())) for i in range(item_no)] #We can take the inputs from user as list of lists.
# print (user_list1)
# a = input("Enter the main list no. you wish to fetch an element from : ")
# b = input("Enter the index of a number from secondary list :")
# print (user_list1[int(a)][int(b)])

# user_list2 = [input(f'Enter value : ') for i in range(item_no)]
# print (user_list2)

"""Dictionary Comprehension."""
dict = {i:f"item{i}" for i in range(100) if i%10==0} #A dictionary has been created with a one liner.
reversd_dict= {v:i for i,v in dict.items()} #A dictionary can be reversed using dictionary comprehension.
print (reversd_dict,"\n\n",dict,"\n")
dict [50] = "Genda"
print (dict)

"""Set Comprehension"""
# set is defined using curly braces and dose not repeat the values in it.
# list = [4,5,6,4,1,2,4,5,7,6,8]
# list[2]="K"
# s1 = set(list) #A set is made from the list.
# print (s1)

# colour_set = {colour for colour in ['blue','red','orange','red','yellow','blue','green']}
# print (colour_set)

"""Generator Comprehension"""
#Generatore Comprehensions are made using open parantheses '()'.
# evens = (i for i in range (100) if i%2 == 0)
# print (evens)
# print (evens.__next__())
# print (evens.__next__())
# print (evens.__next__())
# print (evens.__next__())




