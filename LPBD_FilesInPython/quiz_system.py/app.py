# The quiz system to load data from txt file "questions.txt".
# Questions are stored in the questions.txt as a question per line.
# For Each Q&As prompt the user with the question and wait for the user to answer before moving to next question
# Keep track of the answers, once all questions are answered grade need to be stored into a file result.txt
# Format of the grade should be Your final score is {n}/{m}

questions = open("questions.txt", "r")
questions_list = [question.strip() for question in questions.readlines()]
questions.close()

quiz_questions = []
quiz_answers = []
correct_answers_counter = 0

for question in questions_list:
    splitter = question.find("=")
    quiz_questions.append(question[0:splitter+1])
    quiz_answers.append(question[splitter+1:])

for i, question in enumerate(quiz_questions):
    user_answer = input(f"{question}")
    if user_answer == quiz_answers[i]:
        correct_answers_counter += 1

result = f"Your final score is {correct_answers_counter}/{len(quiz_questions)}."

results = open("result.txt", "w")
results.write(result)

results.close()