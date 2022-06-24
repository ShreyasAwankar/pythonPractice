"""
1.'else' statement works with 'for' loop when 'for' loop ends normally
i.e. there is no any break statement or some condition that will end
the 'for' loop without completing its all iterations.
2.'else' with 'for' is used when the item we want to find in string,list,etc.,
is not found and we want to perform an operation or display some message to the user
"""
menu = ['Vadapaw', 'Panipuri', 'Burger', 'Noodles', 'Pizza', 'Samosa', 'Kachori', 'Dabeli']
order = input("What do you wanna order? \n")
for i in menu:
    if i == order:
        print ("Grab a table. We will get your order ready soon....")
        break
else:
    print ("The food item you are looking for"
           " is not in our menu.")
    # menu.append(order)
    # print (f"New menu: {menu}")


