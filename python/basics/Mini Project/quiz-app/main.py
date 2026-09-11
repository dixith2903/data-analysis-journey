def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "options": ["A) Berlin", "B) Madrid", "C) Paris", "D) Rome"],
            "answer": "C) Paris"
        },
        {
            "question": "What is the largest planet in our solar system?",
            "options": ["A) Earth", "B) Jupiter", "C) Mars", "D) Saturn"],
            "answer": "B) Jupiter"
        },
        {
            "question": "Who wrote 'To Kill a Mockingbird'?",
            "options": ["A) Harper Lee", "B) Mark Twain", "C) J.K. Rowling", "D) Ernest Hemingway"],
            "answer": "A) Harper Lee"
        }
    ]

    score = 0

    for index, question in enumerate(questions):
        print(f"Question {index + 1}: {question['question']}")
        for option in question['options']:
            print(option)
        
        user_answer = input("Your answer: ")
        
        if user_answer.strip().upper() == question['answer'][0]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {question['answer']}")
        
        print()
        print(f"Your current score is: {score}/{index + 1}")
        print("-" * 30)
run_quiz()