import random
import sys
lcase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
ucase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'G', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
num = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
special = ['"', "'", ';', ':', ',', '.', '/', '?', ']', '[', '{', '}', '-', '+', '=', '_', '|', '*', '>', '<', '&', ')', '(', '^', '%', '$', '#', '@', '!', '`', '~']
try:
    length = int(sys.argv[1])
except:
    length = int(input("Please enter the length you want your password to be\n--$ "))
p = ""
for i in range(0, length):
    sym = random.randrange(0,4)
    match sym:
        case 0:
            p = p + random.choice(lcase)
        case 1:
            p = p + random.choice(ucase)
        case 2:
            p = p + random.choice(num)
        case 3:
            p = p + random.choice(special)
print(p)
