#import other stuff here
from io import SEEK_END
import sys
import random
from colorama import force
x = 0
username = input("What is your username:")
password = input("""What is your password?
hint, 123:""")

if password == "123":
    print("user has been authorized")

elif password != ("123"):
    print("User has not been authorized")
    sys.exit()


read = open("songlist.txt", "rt")
songs = read.readlines()
songlist = []

score = 0

for i in range (length(songs)):
    songlist.append(songs[i].strip('\n'))

while x == 0:
    choice = random.choice(songlist)
    artist, song = choice.split(" ")

songs = songs.split()
letters = [word[0] for word in songs]

for x in range (0,2):
    print(artist, "".join(letters))
    guess = str(input("Guess the song:"))
    print("\n")
    if guess == song:
        if x ==0:
            score = score + 3
            break
        if x == 1:
            score = score + 1
        break
print("Your score is", score)
print("Be ready for the next one")
print("\n")

leaderboard = open("leaderboard.txt", "rt+")
leaderboard.write(username + "-" + "{}" .format(score))
leaderboard.close()
leaderboard.open("leaderboard.txt", "rt+")
leaderboard_file = leaderboard.readlines()
print(leaderboard_file)
leaderboard.close()
