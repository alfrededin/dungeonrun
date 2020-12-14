from os import system, name




# Python program to print 
# colored text and background 
class colors: 

    class fg: 
        black='\033[30m'
        red='\033[31m'
        green='\033[32m'
        orange='\033[33m'
        blue='\033[34m'
        purple='\033[35m'
        cyan='\033[36m'
        lightgrey='\033[37m'
        darkgrey='\033[90m'
        lightred='\033[91m'
        lightgreen='\033[92m'
        yellow='\033[93m'
        lightblue='\033[94m'
        pink='\033[95m'
        lightcyan='\033[96m'
        reset='\033[0m'
    class bg: 
        black='\033[40m'
        red='\033[41m'
        green='\033[42m'
        orange='\033[43m'
        blue='\033[44m'
        purple='\033[45m'
        cyan='\033[46m'
        lightgrey='\033[47m'
  
 

map_size = 8
room = ["[X]"]

dungeon = [room*map_size for i in range(map_size)]


def print_dungeon(x, y):
    dungeon[x][y] = "[O]"
    for i in range(map_size):
        for j in range(map_size):
            x = ""
            if j == map_size - 1:
                x = "\n"
            if dungeon[i][j] == "[O]":
                print(colors.fg.orange, dungeon[i][j], end=x)
            else:
                print(colors.fg.purple, dungeon[i][j], end=x+colors.fg.reset)
def clear_screen():
    if name == 'nt':
        _ = system('cls')
    else:
        _ = system('clear')

clear_screen()


