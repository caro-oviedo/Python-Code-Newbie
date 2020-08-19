from pprint import pprint 

def print_board(board): 
    print(f"{board['top-L']}|{board['top-M']}|{board['top-R']} ")
    print("-+--+-")
    print(f"{board['mid-L']}|{board['mid-M']}|{board['mid-R']} ")
    print("-+--+-")
    print(f"{board['low-L']}|{board['low-M']}|{board['low-R']} ")


theboard = {'top-L': '?', 'top-M': '?', 'top-R': '?', 
'mid-L': '?', 'mid-M': '?', 'mid-R': '?', 
'low-L': '?', 'low-M': '?', 'low-R': '?'}


turn = 'X'
for i in range(9):
    print_board(theboard)
    print(f"Turn for {turn}. Move on which space? (Example: top-L , mid-M, low-R ")
    print("Press 'q' to quit")
    move = input()
    if move == 'q': 
        break
    theboard[move] = turn
    if turn == 'X':
        turn = 'O'
    else: 
        turn ='X'
    
print_board(theboard)