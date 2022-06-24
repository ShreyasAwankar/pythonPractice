"""
What opening a file with "With block" actually does is to create a context manager that automatically closes
a file after processing it. Another benefit of using a “With block” is that we can open multiple files in a
single block by separating them using a comma. All the files could have different modes of opening. For example,
we can access one file for reading and another one for writing purposes. Both files should have different objects referring to them.
"""
with open("WithBlock.txt") as f:

    print (f.readline())
    print (f.tell(s))
