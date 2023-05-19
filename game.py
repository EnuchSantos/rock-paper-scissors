import random

def game_run():
    user = input(f"What's your choice? 'r' for ✊ 'p' for 🖐 's' for 🖖\n")
    computer = random.choice(['r', 'p', 's'])
    
    status = rules(user, computer)
    
    if status == 1:
        print(f'You won! Congratulations!\n {user} x {computer}')
    elif status == 2:
        print(f'Draw!!\n {user} x {computer}')
    else:
        print(f'You lost!!\n {user} x {computer}')

def rules(user: str, computer: str) -> int:
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') \
        or (user == 's' and computer == 'p'):
        return 1
    elif (user == 'r' and computer == 'r') or (user == 'p' and computer == 'p') \
        or (user == 's' and computer == 's'):
        return 2
    
    return 3

game_run()