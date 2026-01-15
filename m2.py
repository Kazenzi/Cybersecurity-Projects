#funtions  a section of code that can be reused -improve efficiency
#user defined 
#def keyword for function

def greetemployee():
    print("Welcome 2 yes")

greetemployee()


# parameter an object used in a function
# range (start , stop)

def greetemployee(name):
    print("Welcome 2 yes", name)

greetemployee("jess")

# argument data brought in a funtion when called 

def calculatefails(total, failed):
    # prevent division by zero
    if total == 0:
        return 0

    failure = failed / total
    return failure


# call the function
result = calculatefails(4, 2)

# display the result
print("Failure rate:", result)
 
# return retuen information from a function



print(type ("secuity"))
print(type(75));


names=["jess","francy","anna","kaz"]
print(sorted(names))
print(names)

print (len("tess"))
print("Hello".index("l"))

