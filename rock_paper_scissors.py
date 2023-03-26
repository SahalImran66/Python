import random
def choices():
    option=["rock","scissors","paper"]
    player_choice=input("enter a choice, rock ,paper,scissors: ").lower()
    computer_choice=random.choice(option)
    choices={"player":player_choice,"computer":computer_choice}
    
    return choices

reponse=choices()
print(reponse)
def check_win(player,computer):
    print(f"You chose {player} , computer chose {computer}")
    if player==computer:
        return "TIE !!!"
    elif player=="rock":
        if computer=="scissors":
            return "Rock Smashes Scissors, You Win !!!"
        else:
            return "Paper covers Rock, You Lose :|"
    elif player=="paper":
        if computer=="rock":
            return "Paper covers Rock, You Win !!!"
        else:
            return "Scissors cuts paper, You Lose :|"
    elif player=="scissors":
        if computer=="rock":
            return "Rock smashes Scissors, You lose :|"
        else:
            return "Scissors cuts paper, You Win !!!"
    
win=check_win(reponse["player"],reponse["computer"] )
print(win)