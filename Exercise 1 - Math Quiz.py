import random

def DisplayChoices(): # Displays difificulty choices and returns the selected level.
    print("DIFFICULTY LEVEL")
    print("1. Easy")
    print("2. Moderate")
    print("3. Advanced")
    while True:
        try:
            choice = int(input("Choose difficulty (1-3): "))
            if choice in [1, 2, 3]:
                return choice
            else:
                print("Please enter 1, 2, or 3.")
        except:
            print("Invalid input, please enter a number.")

def randomInt(level): # Generates a random integer based on the difficulty level.
    if level == 1:
        return random.randint(1, 9)
    elif level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(1000, 9999)

def decideOperation(): # Randomly decides between addition and subtraction.
    op = random.choice(['+', '-'])
    return op

def displayProblem(num1, num2, op): # Displays the problem and gets user input.
    print()
    print(f"{num1} {op} {num2} = ", end="")
    while True:
        try:
            answer = int(input())
            return answer
        except:
            print("Please enter a number.")
            print(f"{num1} {op} {num2} = ", end="")

def isCorrect(userAns, correctAns, attempt): # Checks if the answer is correct and returns score.
    if userAns == correctAns:
        if attempt == 1:
            print("Correct! +10 points")
            return 10
        else:
            print("Correct on second try! +5 points")
            return 5
    else:
        if attempt == 1:
            print("Incorrect. Try again.")
        else:
            print(f"Wrong again! The correct answer was {correctAns}.")
        return 0

def displayResults(score): # Displays the final score and grade.
    print("\nQUIZ COMPLETE!") 
    print(f"Your final score is {score}/100")
    if score >= 90:
        grade = "A+"
    elif score >= 80:
        grade = "A"
    elif score >= 70:
        grade = "B"
    elif score >= 60:
        grade = "C"
    elif score >= 50:
        grade = "D"
    else:
        grade = "F"
    print("Your grade:", grade)
    print()

def playQuiz(): # Main function to play the quiz.
    level = DisplayChoices()
    totalScore = 0
    for i in range(1, 11):
        num1 = randomInt(level)
        num2 = randomInt(level)
        op = decideOperation()

        # prevent negative results for easy mode (optional)
        if op == '-' and num1 < num2:
            num1, num2 = num2, num1

        if op == '+':
            correctAns = num1 + num2
        else:
            correctAns = num1 - num2

        print(f"\nQuestion {i}:") # Displays question number.
        attempt = 1
        userAns = displayProblem(num1, num2, op)
        score = isCorrect(userAns, correctAns, attempt)
        if score == 0 and userAns != correctAns:
            attempt = 2
            userAns = displayProblem(num1, num2, op)
            score = isCorrect(userAns, correctAns, attempt)
        totalScore += score

    displayResults(totalScore) # Displays final results.

def main(): # Main loop to run the quiz and asks the user for a replay.
    print("Welcome to the MQG (Math Quiz Generator!)")
    while True:
        playQuiz()
        again = input("Do you want to play again or nah? (y/n): ").lower()
        if again != 'y':
            print("Thanks for playing!")
            break
main() # Start the program.