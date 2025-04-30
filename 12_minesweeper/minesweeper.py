import random
import sys 

# Define emojis
MINE = '💣'
SAFE = '✅'
EMPTY = ' '

nums = [1,2,3,4,5,6,7,8,9]
def layout(board):
    print(str(board[0]) + "|" + str(board[1]) + " |" + str(board[2]))
    print("-----")
    print(str(board[3]) + "|" + str(board[4]) + " |" + str(board[5]))
    print("-----")
    print(str(board[6]) + "|" + str(board[7]) + " |" + str(board[8]))

layout(nums)

def game():
    nums = [1,2,3,4,5,6,7,8,9]
    mine = random.choice(nums)
    print('\nMINESWEEPER BY MAZZ ATHER')
    while True:
        numCOUNT = len(list(filter(lambda x: x != EMPTY and x != SAFE, nums)))
        layout(nums)
        choice = int(input("Enter a number: "))
        if choice < 1 or choice >    9:
            print("Please enter a number between 1 and 9")
            continue
        nums[choice-1] = SAFE
        print('\n')
        if choice == mine:
            nums[choice-1] = MINE
            layout(nums)
            print("Game over! 💥")
            return
        elif numCOUNT == 2:
            layout(list(map(lambda x: x if x == choice - 1 else x, nums)))
            print("You won! 🎉")
            return

while True:
    game()
    playAgain = input("Do you want to play again? (yes or no) ")
    if playAgain.lower().startswith('y'):
        continue
    else:
        print("Thanks for playing! 👋")
        sys.exit()