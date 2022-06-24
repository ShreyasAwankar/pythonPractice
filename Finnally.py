def divide(a, b):
    try:
        print(f'{a}/{b} is {int(a) /int(b)}')
    except: #If 'except:' runs, 'else' will not run.
        print("Invalid input!")
    else: #If 'except:' dose not run, 'else' will run.
        print("No Exception")
    finally: #'finally:' is executed in any case.
        print ("Try more examples and have fun...!")

a = input ("Enter the first no."+ "\n")
b = input ("Enter the second no."+ "\n")
divide(a,b)

