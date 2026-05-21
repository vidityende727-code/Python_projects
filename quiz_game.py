questions = [ 
    { 
       "question": "What is the capital of France?", 
       "options": ["A. London","B.Paris","C. Rome","D. Berlin"], 
       "answer": "B" 
    }, 
    { 
        "question": "Which planet is closest to the sun?", 
        "options": ["A.Venus","B. Earth", "C.Mercury", "D. Mars"], 
        "answer": "C"

    }, 
    { 
        "question": "What is  15 x 15?", 
        "options": ["A. 200", "B. 215", "C. 225", "D. 250"],
        "answer": "C"  

    }, 
    { 
        "question": "Who invented the telephone?", 
        "options": ["A. Edison", "B. Tesla", "C. Bell", "D. Newton"], 
        "answer": "C"
    }, 
    { 
        "question": "What is the largest ocean?", 
        "options": ["A. Atlantic", "B. Indian", "C. Arctic", "D. Pacific"], 
        "answer": "D"
    }
] 
score = 0 
print("--- Welcome to Quiz Game ---\n") 
for i, q in enumerate(questions): 
    print(f"Questions {i + 1}: {q['question']}") 
    for option in q["options"]: 
        print(option) 
    answer = input("Your answer (A/B/B/D):").upper() 
    if answer == q["answer"]: 
        print("Correct!✅\n") 
        score += 1 
    else: 
        print(f"Wrong! Answer was {q['answer']} ❌\n") 
print(f"--- Quiz Completed! ---") 
print(f"Your score: {score}/{len(questions)}") 
if score == len(questions): 
    print("Perfect score! Amazing!") 
elif score >= 3: 
    print("Good job!") 
else: 
    print("Keep practicing!") 
    