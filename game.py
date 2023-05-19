import random

def game_run():
    user_points = 0
    computer_points = 0
    for hit in range(3):
        user = input(f"What's your choice? 'r' for ✊ 'p' for 🖐 's' for 🖖\n")
        computer = random.choice(['r', 'p', 's'])
        
        status = rules(user, computer)
        
        if status == 1:
            user_points += 1
        elif status == 2:   
            computer_points += 1 
        print(f'user:{user_points} computer: {computer_points}\n{user} x {computer}') 
    
    if user_points > computer_points:
        print(f'You won! Congratulations!')
    elif computer_points > user_points:
        print(f'You lost!!')
    else:
        print(f'Draw!!') 
                   

def rules(user: str, computer: str) -> int:
    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') \
        or (user == 's' and computer == 'p'):
        return 1
    elif (user == 's' and computer == 'r') or (user == 'r' and computer == 'p') \
        or (user == 'p' and computer == 's'):
        return 2
    
    return 3
    
    
game_run()