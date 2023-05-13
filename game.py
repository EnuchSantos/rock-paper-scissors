import random

while True:
    user = input(f"What's your choice? 'r' for ✊ 'p' for 🖐 's' for 🖖\n")
    computer = random.choice(['r', 'p', 's'])

    if (user == 'r' and computer == 's') or (user == 'p' and computer == 'r') \
        or (user == 's' and computer == 'p'):
        print(f"You won!\nyou: {user}\ncomputer: {computer}")
        continue

    print(f"You lost!\nyou: {user}\ncomputer: {computer}")
    continue

