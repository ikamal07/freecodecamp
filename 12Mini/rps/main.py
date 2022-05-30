import random
def play():
    user=input("'r' for Rock , 'p' for Paper ,'s' for Scissor : ")

#r > s , s > p , p > r
    comp_challenge = random.choice(['r','p','s'])
    print(comp_challenge)
    if user == comp_challenge:
        return 'It is Tie'
    if is_win(user,comp_challenge):
        return 'You Win'
    return 'Computer Win'

def is_win(player,comp):
    if (player == 'r' and comp == 's') or (player == 's' and comp == 'p') or (player == 'p' and comp =='r'):
        return True

print(play())







