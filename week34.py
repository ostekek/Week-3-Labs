p1= input()
p2= input()

if p1 == 'rock':
    if p2 == "scissors":
        print('Player 1 wins')
    elif p2 == "paper":
        print('Player 2 wins')
    elif p2 == p1:
        print('Tie')

if p1 == 'paper':
    if p2 == "rock":
        print('Player 1 wins')
    elif p2 == "scissors":
        print('Player 2 wins')
    elif p2 == p1:
        print('Tie')
        
if p1 == 'scissors':
    if p2 == "paper":
        print('Player 1 wins')
    elif p2 == "rock":
        print('Player 2 wins')
    elif p2 == p1:
        print('Tie')
