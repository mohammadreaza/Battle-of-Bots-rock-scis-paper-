import random
options = ["rock", "paper", "scis"]
round=0
user_score = 0
computer_score = 0
count=int(input("Enter:"))
print(count)
while count>0:  
    user = input("Choose: ")
    if user == "q":
        break
    computer = random.choice(options)
    round+=1
    print(f"Round {round} - Computer chose: {computer}")
    if user == computer:
        print("Tie!")
    elif (user == "rock" and computer == "scis") or (user == "paper" and computer == "rock")or (user == "scis" and computer == "paper"):
        print("You win this round!")
        user_score += 1
    elif (computer=="rock" and user=="scis")or(computer =="paper" and user=="rock")or (computer=="scis" and user=="peper"):
        print("Computer wins this round!")
        computer_score += 1
    count-=1
    print(count)
    

print("\nFinal Results:")
print(f"User Score: {user_score}")
print(f"Computer Score: {computer_score}")

if user_score > computer_score:
    print(" \U0001F60E You are the overall winner!\U0001F60E")
elif computer_score > user_score:
    print(" \U0001F3AE Computer is the overall winner!	\U0001F3AE")
else:
    print(" \U0001F643 It's an overall tie!\U0001F643")

