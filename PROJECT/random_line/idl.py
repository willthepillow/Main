import random
bruh = open("idk.txt")
import random
def random_line(fname):
    lines = open(fname).read().splitlines()
    return random.choice(lines)
print(random_line("idk.txt"))
