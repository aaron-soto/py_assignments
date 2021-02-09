import random


def randInt(minNum=0, maxNum=100):
    num = random.random() * (maxNum - minNum) + minNum
    return round(num)


print(randInt(minNum=50, maxNum=500))
# print(randInt()) 		    # should print a random integer between 0 to 100
# print(randInt(max=50)) 	    # should print a random integer between 0 to 50
# print(randInt(min=50)) 	    # should print a random integer between 50 to 100
# print(randInt(min=50, max=500))    # should print a random integer between 50 and 500


# random.random()           ## returns a random number between 0 and 1
# random.random() * 50      ## returns a random number between 0 and 50
# random.random() * 25 + 10 ## returns a random number between 10 and 35
# round(num)                ## returns the rounded integer value of num
