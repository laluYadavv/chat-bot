questions_answers = {
    "where is the canteen?": "The canteen is located near the main building.",
    "who is the head of the CS department?": "Dr. XYZ is the head of the CS department."
}

user_input = input("Ask me something about the college: ").lower()
response = questions_answers.get(user_input, "Sorry, I don't know the answer to that.")
print(response)
