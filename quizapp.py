# Quiz App Program
# Author: [Author Name]
# Date: [Date]
# Description: This program tests users on a specific topic and provides feedback on their performance

import random  # Importing the random module to use for selecting random questions

# Function to ask questions and check answers
def ask_question(question, correct_answer):
    answer = input(f"Your answer: ")  # Have the user input an answer to the question
    if answer.lower() == correct_answer.lower():  # Check if the answer matches the correct answer
        print("You answered correctly!")  # If the answer is correct, print a success message
        return True  # Return True to say the answer was correct
    else:
        print(f"Wrong! The correct answer is: {correct_answer}")  # If the answer is incorrect, print the correct answer
        return False  # Return False to say the answer was incorrect


# Feedback based on incorrect answers
def provide_feedback(incorrect_answers):
    feedback = {  # A dictionary with subject names as keys and feedback messages as values
        "U.S History": "Study the key events and timelines of American history, especially the Civil War and the American Revolution.",
        "Science": "Catch up on basic science concepts like planets, photosynthesis, and the periodic table.",
        "Math": "Review basic arithmetic, geometry, and algebraic concepts, especially slope-intercept form and solving equations.",
        "Films": "Watch the highest-grossing films and study directors' works like Christopher Nolan's.",
        "Music": "Learn about the history of pop and rap music, including artists like Michael Jackson and Lauryn Hill."
    }
   
    for topic in incorrect_answers:  # Loop through each subject in the list of incorrect answers
        print(f"\nFeedback for {topic}: {feedback.get(topic, 'No specific feedback available for this topic.')}")  # Provide feedback for each incorrect answer


# Function for school-related subjects
def school(school_subject):
    subjects = {  # A dictionary of subjects for each subject AND we'll use lists to store questions for each subject since it allows for easy handling and iteration of questions.
        "U.S History": [("Which is the smallest American state by land?", "Rhode Island"),
                        ("When did the Civil War start?", "1861"),
                        ("What is the last state to be added to the United States?", "Hawaii"),
                        ("When did Prohibition in the United States start?", "1920"),
                        ("What year did the American Revolution start?", "1775"),
                        ("Who was the first president of the U.S?", "George Washington"),
                        ("What year did World War I start?", "1914")],
        "Science": [("What planet is known as the Red Planet?", "Mars"),
                    ("What is the chemical symbol for water?", "H2O"),
                    ("What is it called when plants convert sunlight into energy?", "Photosynthesis"),
                    ("Which planet in our solar system has the most moons?", "Saturn"),
                    ("What is the atomic mass of Oxygen on the periodic table?", "16"),
                    ("What is the largest mammal on Earth?", "Blue Whale"),
                    ("Is a tomato a fruit or vegetable?", "Fruit")],
        "Math": [("What is 4*4?", "16"),
                 ("What is slope intercept form?", "y=mx+b"),
                 ("What is 9+10?", "19"),
                 ("What are shapes with 4 sides called?", "Quadrilateral"),
                 ("What is the sum 130+125+191?", "446"),
                 ("20+(90/2) is equal to?", "65")],
    }

    if school_subject in subjects:  # Check if the provided subject is in the dictionary of subjects
        asked_questions = set()  # Track asked questions
        correct_answers = 0  # The number of correct answers
        total_questions = 0  # The total number of questions asked
        incorrect_answers = []  # A list to track incorrect answers
        
        for _ in range(3):  # Loop to ask 3 questions
            question, correct_answer = random.choice(subjects[school_subject])  # Randomly choose a question from the selected subject
            if question in asked_questions:  # Check if the question has already been asked
                continue  # Skip to the next iteration if the question has been asked
            asked_questions.add(question)  # Add the question to the set of asked questions
            print(f"Here is your question from {school_subject}:")  # Display the subject of the question
            print(question)  # Display the question
            if ask_question(question, correct_answer):  # Call the function to ask the question and check the answer
                correct_answers += 1  # The correct answer count if the user answered correctly
            else:
                incorrect_answers.append(school_subject)  # Append the subject to incorrect answers if the user answered incorrectly
            total_questions += 1  # The total questions asked
            
        # Calculate the score
        score_fraction = f"{correct_answers}/{total_questions}"  # Calculate the fraction of correct answers
        score_percentage = (correct_answers / total_questions) * 100  # Calculate the percentage of correct answers
        
        print(f"\nYour performance: {score_fraction} ({score_percentage:.2f}%)")  # Display the user's performance
        
        # Provide feedback if there were any incorrect answers
        if incorrect_answers:
            provide_feedback(incorrect_answers)
    else:
        print("Sorry, we do not have a question for that subject.")  # Inform the user if the subject is not available


# Function for pop culture questions
def social(pop_culture):  # Parameter to specify the pop culture topic
    culture = {  # A dictionary of pop culture topics for each topic AND we'll use lists to store questions for each subject since it allows for easy handling and iteration of questions.
        "Films": [("What is the highest-grossing film of all time?", "Avatar"),
                  ("What film was released in 2021 and directed by Denis Villeneuve?", "Dune"),
                  ("What movie franchise parodies horror films?", "Scary Movie"),
                  ("What year was the movie Gone With The Wind released?", "1939"),
                  ("Who is the director of Oppenheimer?", "Christopher Nolan"),
                  ("What are the names of the two main characters in La La Land?", "Mia and Sebastian")],
        "Music": [("Who is known as the king of Pop?", "Michael Jackson"),
                  ("Which classic rap group included Ice Cube, Eazy-E, and Dr. Dre?", "N.W.A"),
                  ("Who is the most grammy awarded female rapper?", "Lauryn Hill"),
                  ("Who is Kendrick Lamar's 'Not Like Us' about?", "Drake"),
                  ("Who has won the most Grammys?", "Beyonce"),
                  ("Who has the most number one hits?", "The Beatles"),
                  ("Which city is often referred to as the birthplace of jazz?", "New Orleans")]
    }

    if pop_culture in culture:  # Check if the provided pop culture topic is in the dictionary
        asked_questions = set()  # Track asked questions
        correct_answers = 0  # The number of correct answers
        total_questions = 0  # The total number of questions asked
        incorrect_answers = []  # A list to track incorrect answers
        for _ in range(3):  # Loop to ask 3 questions
            question, correct_answer = random.choice(culture[pop_culture])  # Randomly choose a question from the selected pop culture topic
            if question in asked_questions:  # Check if the question has already been asked
                continue  # Skip to the next iteration if the question has been asked
            asked_questions.add(question)  # Add the question to the set of asked questions
            print(f"Here is your pop culture question about {pop_culture}:")  # Display the pop culture topic
            print(question)  # Display the question
            if ask_question(question, correct_answer):  # Call the function to ask the question and check the answer
                correct_answers += 1  # The correct answer count if the user answered correctly
            else:
                incorrect_answers.append(pop_culture)  # Append the topic to incorrect answers if the user answered incorrectly
            total_questions += 1  # The total questions asked
            
        # Calculate the score
        score_fraction = f"{correct_answers}/{total_questions}"  # Calculate the fraction of correct answers
        score_percentage = (correct_answers / total_questions) * 100  # Calculate the percentage of correct answers
        
        print(f"\nYour performance: {score_fraction} ({score_percentage:.2f}%)")  # Display the user's performance
        
        # Provide feedback if there were any incorrect answers
        if incorrect_answers:
            provide_feedback(incorrect_answers) # Calling the funtion
    else:
        print("Sorry, we do not have questions on this pop culture topic.")  # Inform the user if the topic is not available


# Main function to drive the app
def start_schools():
    while True:  # Loop to allow the user to continue answering questions until they decide to stop
        category = input("Do you want a question on 'school subjects' or 'pop culture'? (or type 'exit' to stop): ").lower()  # Have the user choose a category
        if category == "exit":  # Check if the user wants to exit the quiz
            quit_confirmation = input("Are you sure you want to exit? (yes/no): ").lower()  # Confirm the user's decision to exit
            if quit_confirmation == "yes":  # If the user confirms, exit the loop
                print("Thank you for playing!")  # Thank the user for playing
                break
        elif category == "school subjects":  # If the user chooses school subjects
            subject = input("Which school subject? (U.S History, Science, Math): ").title()  # Ask for a specific subject
            school(subject)  # Call the function to ask questions for the selected subject
        elif category == "pop culture":  # If the user chooses pop culture
            topic = input("Which pop culture topic? (Films, Music): ").title()  # Ask for a specific pop culture topic
            social(topic)  # Call the function to ask questions for the selected topic
        else:
            print("Sorry, we don't have questions for that category.")  # Tell the user if the category is not valid

# Call the function to start the quiz
start_schools()  # Start the quiz game