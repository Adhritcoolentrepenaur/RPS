questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "answer": 2
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Saturn"],
        "answer": 1
    },
    {
        "question": "What is 5 + 7?",
        "options": ["10", "11", "12", "13"],
        "answer": 2
    },
    {
        "question": "Which gas do plants absorb from the atmosphere?",
        "options": ["Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen"],
        "answer": 2
    },
    {
        "question": "Who wrote the play 'Romeo and Juliet'?",
        "options": ["Charles Dickens", "William Shakespeare", "Jane Austen", "Mark Twain"],
        "answer": 1
    },
    {
        "question": "What is the largest mammal in the world?",
        "options": ["Elephant", "Blue Whale", "Giraffe", "Hippopotamus"],
        "answer": 1
    },
    {
        "question": "Which element has the chemical symbol 'O'?",
        "options": ["Osmium", "Oxygen", "Gold", "Iron"],
        "answer": 1
    },
    {
        "question": "What is the square root of 144?",
        "options": ["10", "11", "12", "13"],
        "answer": 2
    },
    {
        "question": "Which continent is the Sahara Desert located in?",
        "options": ["Asia", "Africa", "Australia", "South America"],
        "answer": 1
    },
    {
        "question": "What is the boiling point of water in Celsius?",
        "options": ["90°C", "95°C", "100°C", "105°C"],
        "answer": 2
    },
    {
        "question": "Which organ pumps blood throughout the human body?",
        "options": ["Lungs", "Brain", "Heart", "Liver"],
        "answer": 2
    },
    {
        "question": "What is the currency of Japan?",
        "options": ["Yuan", "Won", "Yen", "Ringgit"],
        "answer": 2
    },
    {
        "question": "Which planet is closest to the Sun?",
        "options": ["Venus", "Earth", "Mercury", "Mars"],
        "answer": 2
    }
]



score = 0

for i, q in enumerate(questions):
    print(f"\nQuestion {i+1}: {q['question']}")
    for idx, option in enumerate(q['options']):
        print(f"{idx + 1}. {option}")
    
    try:
        user_answer = int(input("Enter your answer (1-4): ")) - 1
        if user_answer == q['answer']:
            print("✅ Correct!")
            score += 1
        else:
            print(f"❌ Wrong! The correct answer was: {q['options'][q['answer']]}")
    except ValueError:
        print("⚠️ Invalid input. Please enter a number between 1 and 4.")

print(f"\n🎉 Your final score is: {score}/{len(questions)}")
