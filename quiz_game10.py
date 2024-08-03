print("**************************")
print("Welcome to my quiz game!!")

question_bank=[
{"text":"The ability of one class to acquire methods and attributes of another class is called______.",
"answer":"A"},
{"text":"Which of the following is a type of inheritance?","answer":"C"},
{"text":"what type of inheritance has subclass to a single superclass?","answer":"C"},
{"text":"what is the depth of multilevel inheritance in python?","answer":"C"},
{"text":"What does MRO stands for?","answer":"B"}
]

options=[["A.Inheritance","B.Abstraction","C.polymorphism","D.Object"],
         ["A. Single","B.Double","C.Multiple","D.Both A and C"],
         ["A.Multiple Inheritance","B.Multilevel Inheritance","C.Hierarichal Inheritance","D.None of These"],
         ["A.Two level","B.three level","C.Any level","D.None of these"],
         ["A.Method Recursive Object","B.Method Resolution Order","C.Main Resolution Order","D.Method Resolution Objeect."]
]

score=0
def check_answer(user_guess,correct_answer):
    if user_guess==correct_answer:
        return True
    else:
        return False


for question_num in range (len(question_bank)):# 0 1 2 3 4 index
    print("**********************")
    print(question_bank[question_num]["text"])

    for i in options[question_num]:
        print(i)

    guess=input("Enter Your Answer(A/B/C/D)").upper()
    is_correct=check_answer(guess,question_bank[question_num]["answer"])
    
    if is_correct:
        print("Correct answer")
        score+=1
    else:
        print("Incorrect answer")
        print(f"The correct answer is {question_bank[question_num]['answer']}")

    print(f"Your correct score is {score}/{question_num}")
print(f"Your have given {score} correct answers")

print(f"Your score is {score/len(question_bank)*100}%")







 




































 









































































