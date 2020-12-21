#import other stuff here
import sys 
import random
import numpy
x = 0
username = input("What is your username:")
password = input("""What is your password?
hint, 123:""")

if password != ("123"):
    print("user has not been authorised!")
    sys.exit()


if password == ("123"):
    print("""user has been authorised
    """) # this break in the line is to make the leaderboard easier to read


score = 0





arr = numpy.array([1, 2, 3, 4])
songlist = open("songlist.txt", "rt")
print(arr)



#username_O = open("leaderboard.txt", "r+")
#username_R = username_O.read()
#print(username_R)