import time
print ("Time in secs since epoch i.e 1st Jan 1970", time.time())

# print ("Gmtimeoutput:", time.gmtime(60))

# Current_time = time.ctime()
# print (Current_time)
# #OR
# print (time.ctime(3655)) #This takes seconds as argument. If no argument is provided, it will calculate since epoch i.e it will show the current time.

for i in range(1,4):
    # using sleep() to hault execution
    time.sleep(3)
    print("Iteration no.", i)

# print (time.localtime())
# print (time.gmtime())
# print (time.mktime(time.localtime()))
# print (time.asctime())
# print (time.ctime())