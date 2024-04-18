import random

def play():
    user = input("whats your choice? 'r' for rock , 'p' for paper ,'s' for scissors\n")
    user = user.lower()

    computer = random.choice(['r', 'p', 's'])

    if user == computer:
        return "you and the computer have both chosen {}. it's a tie".format(computer)

        # r > s, s > p , p > r
        if is_win (user,computer):
            return "you have chosen {} and the computer has chosen {}. you won!".format(user,computer)

            return "you have chosen {} and the computer has chosen {}.you lost:(".format(user, computer)

def is_win(player, oponent):
    # return true is the player beats opponent
    # wining conditions: r > s, s > p, p > r
    if (player == 'r' and opponent == 's') or (player == 's' and opponent == 'p') or ( player == 'p' and opponent =='r'):
        return  True
    return False

if __name__=='__main__':
    print(play())
