"""To know the theory of coroutines, please check the file "Coroutine.txt"""
def searcher():
    import time
    # Some 4 seconds time consuming task
    book = "This is a book on harry and code with harry and good"
    time.sleep(4)

"""This sleep time is added to make a delay of 4 seconds in the demonstration as like "the coroutine is reading a very big file 
and it takes some time to completely read that big file. After the big file being read, the next program will run faster without 
taking much time as our coroutine has read the big file and taken that time to read"""

    while True:
        text = (yield)
        if text in book:
            print("Your text is in the book")
        else:
            print("Text is not in the book")
#the whole above block is a coroutine the except comment.


search = searcher()
print("search started")
next(search)
print("Next method run")
search.send("harry")

search.close()
search.send("harry")
# input("press any key")
# search.send("harry and")
# input("press any key")
# search.send("thi si")
# input("press any key")
# search.send("joker")
# input("press any key")
# search.send("like this video")

