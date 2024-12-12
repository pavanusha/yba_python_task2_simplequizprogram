def run_quiz():
    
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee",
        "What is the largest planet in our Solar System?": "Jupiter",
        "What is the boiling point of water in Celsius?": "100",
    }

    print("Welcome to the Quiz!\n")

    score = 0  

    
    for question, answer in questions.items():
        print(question)
        user_answer = input("Your answer: ").strip()

        if user_answer.lower() == answer.lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {answer}.\n")

    
    print(f"Quiz complete! Your final score is {score}/{len(questions)}.")

def main():
    run_quiz()

if __name__ == "__main__":
    main()
