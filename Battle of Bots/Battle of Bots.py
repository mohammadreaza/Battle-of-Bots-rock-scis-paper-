import random
import time
options = ["rock", "paper", "scis"]
round=0
computer1_score = 0
computer2_score = 0
count=int(input("Enter:"))
time.sleep(3)
print(count)
while count>0:  
    computer1 = random.choice(options)
    computer2 = random.choice(options)
    round+=1
    print(f"Round {round} - Computer1 chose: {computer1} - computer2:{computer2}")
    time.sleep(0)
    if computer1 == computer2:
        print("Tie!")
    elif (computer1 == "rock" and computer2 == "scis") or (computer1 == "paper" and computer2 == "rock")or (computer1 == "scis" and computer2 == "paper"):
        print("computer1 wins this round!")
        computer1_score += 1
    elif (computer2=="rock" and computer1=="scis")or(computer2 =="paper" and computer1=="rock")or (computer2=="scis" and computer1=="peper"):
        print("Computer2 wins this round!")
        computer2_score += 1
    count-=1
    print(count)
    

print("\nFinal Results:")
print(f"computer1 Score: {computer1_score}")
print(f"Computer2 Score: {computer2_score}")

if computer1_score > computer2_score:
    print("	\U0001F3AE computer1 is the overall winner!\U0001F3AE")
elif computer2_score > computer1_score:
    print("	\U0001F3AE Computer2 is the overall winner!	\U0001F3AE")
else:
    print(" \U0001F643It's an overall tie!\U0001F643")