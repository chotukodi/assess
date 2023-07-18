exam_questions = {
    1: {
        'question': 'What is the capital of France?',
        'answer': 'Paris'
    },
    2: {
        'question': 'What is the largest planet in our solar system?',
        'answer': 'Jupiter'
    },
    3: {
        'question': 'What programming language is known as the "language of the web"?',
        'answer': 'JavaScript'
    }
}

# Accessing and displaying a question
question_number = 2
question = exam_questions[question_number]['question']
print(f"Question {question_number}: {question}")

# Accepting user input and checking the answer
user_answer = input("Your answer: ")
correct_answer = exam_questions[question_number]['answer']

if user_answer.lower() == correct_answer.lower():
    print("Correct answer!")
else:
    print(f"Wrong answer. The correct answer is: {correct_answer}")