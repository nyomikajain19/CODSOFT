import random
print("\n Rock-Paper-Scissors - Game On!")
options = ["rock", "paper", "scissors"]
user_score = comp_score = 0
while True:
  user = input("\nChoose rock / paper / scissors (or exit): ").lower()
  if user == "exit":
    break
  if user not in options:
    print(" Invalid choice!")
    continue
  comp = random.choice(options)
  print(f"Computer chose: {comp}")
  if user == comp:
    print(" It's a tie!")
  elif (user == "rock" and comp == "scissors") or \
       (user == "paper" and comp == "rock") or \
       (user == "scissors" and comp == "paper"):
      print(" You Win!")
      user_score += 1
  else:
    print(" Computer Wins!")
    comp_score += 1
  print(f" Score -> You: {user_score} | Computer: {comp_score}")
print(" Thanks for playing!")
