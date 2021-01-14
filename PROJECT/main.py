
#import other stuff here
import sys
import random
x = 0
username = input("What is your username:")
password = input("""What is your password?
hint, 123:""")

if password ==  "123":
    print("user has been authorized")
    print ("-" * 50)
    print ("-" * 18 +" STARTING GAME " + "-" * 17)
    print ("-" * 50)
#this checks if the password is correct

elif password != ("123"):
    print("User has not been authorized")
    sys.exit()
#this runs if the password has not been written correctly, and exits the program

def random_song(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
#this function selects a random line

user_score = 0
post = 1

while post == 1:
    song_list = random_song("songlist.txt")
    songname, artist = song_list.split(";")#this splits the songlist.txt file where there is a ";"
    user_guess = input  ("""Whats the name of the song?
    hint, it begins with...""" + songname[0] + ":")
     #this asks the user the songname and gives them a hint
    if user_guess == songname:
        user_score = user_score + 1 #if the user is correct, they score a point
        print ("correct, your score is now: " + str(user_score) + " points")#this prints the user score
    else:
        user_guess = input("incorrect, try again:") #if the user gets the first guess wrong, they get another chance
        if user_guess == songname:
            user_score = user_score + 1 #if the user guess correctly, they get another point and they get to try another song
            print ("correct, your score is now: " + str(user_score) + " points") #^^
        else:
            print ("incorrect, game over.") #if they get the 2 chances wrong, the loop ends
            print ("Score = " + str(user_score)) #this prints the user score
            post == 0
            break
        

score_1 = str(user_score) 

print("\n") #the \n just creates an empty line to make the program more visualy pleasing to the user/ more aesthetic
print ("-" * 40)
print("-" * 15 + "LEADERBOARD" + "-" * 14)
print ("-" * 40)
print("\n") #this is just a banner presenting the scoreboard

leaderboard = open("leaderboard.txt", "r+")
leaderboard.write(username + "-" + '{}'.format(user_score)) #this writes the user's score into the leaderboard.txt file
leaderboard.close()
leaderboard = open("leaderboard.txt", "r+")
leaderboard_list = leaderboard.readlines()
print(leaderboard_list) #this prints the user/ user's score underneath the leaderboard banner
leaderboard.close()
