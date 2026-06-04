import random
from sklearn.tree import DecisionTreeClassifier

# Mapping moves to numbers
move_map = {
    "rock": 0,
    "paper": 1,
    "scissors": 2
}

reverse_map = {
    0: "rock",
    1: "paper",
    2: "scissors"
}

# Training data
X = []
y = []

# Scores
user_score = 0
computer_score = 0

# Machine Learning Model
model = DecisionTreeClassifier()

print("=== AI Rock Paper Scissors Game ===")
print("Type rock, paper, scissors or quit")

previous_move = None

while True:

    user_move = input("\nYour move: ").lower()

    if user_move == "quit":
        print("\nFinal Score")
        print("You:", user_score)
        print("Computer:", computer_score)
        break

    if user_move not in move_map:
        print("Invalid choice!")
        continue

    user_num = move_map[user_move]

    # Train model if enough data exists
    if len(X) > 2:
        model.fit(X, y)

        if previous_move is not None:
            predicted = model.predict([[previous_move]])[0]

            # Computer chooses winning move
            computer_num = (predicted + 1) % 3
        else:
            computer_num = random.randint(0, 2)

    else:
        computer_num = random.randint(0, 2)

    computer_move = reverse_map[computer_num]

    print("Computer chose:", computer_move)

    # Determine winner
    if user_num == computer_num:
        print("It's a Tie!")

    elif (
        (user_num == 0 and computer_num == 2) or
        (user_num == 1 and computer_num == 0) or
        (user_num == 2 and computer_num == 1)
    ):
        print("You Win!")
        user_score += 1

    else:
        print("Computer Wins!")
        computer_score += 1

    print("Score -> You:", user_score,
          "| Computer:", computer_score)

    # Store training data
    if previous_move is not None:
        X.append([previous_move])
        y.append(user_num)

    previous_move = user_num