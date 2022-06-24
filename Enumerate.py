"""
What enumerate function does is, it assigns an index to every element or value
in the object that we want to iterate, so we do not have to assign a specific
variable for incremental function, instead we have to apply a for loop, and our
function will start working.
"""
# l1 = ["Bhindi", "Aloo", "chopsticks", "chowmein"]
# i = 1
# for item in l1:
#    if i%2 == 0:
#         print(f"Jarvis please buy {item}")
#    i += 1
#
# for i,v in enumerate(l1,1): #its not necessary but as a better practice, we can use index, item (for dictionary- key,value) instead of i,v for better understanding of the code.
#     if i % 2 == 0:
#         print(f"Please buy {v}")

# """New Code"""
# list_2 = ["Python", "Programming", "Is", "Fun"]
# # # Index value starts from 1
# result=enumerate(list_2,1)
# print (result) #enumerate just creates an object and dose not print anything unless we make it into a list
# # print(list(result),"\n") #We need to typecast the enumerate into a list so as to display it.
# # """OR"""
# print (list(enumerate(list_2,1)))



