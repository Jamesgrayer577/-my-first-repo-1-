#Author: James Grayer
#Program: Mod_11 - Dictionaries
#Date: November, 5, 2026

import random

# Create a dictionary of U.S. states and capitals
state_capitals = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "St. Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

# Initialize counters
correct_count = 0
incorrect_count = 0

# Convert dictionary keys into a list for random selection
states_list = list(state_capitals.keys())

print("Welcome to the U.S. State Capital Quiz!")
print("Type 'quit' anytime to stop the quiz.\n")

while True:
  # Randomly pick a state
  state = random.choice(states_list)
  correct_capital = state_capitals[state]

  # Ask the user for the capital
  user_answer = input(f"What is the capital of {state}? ").strip()

  # Check if the user wants to quit
  if user_answer.lower() == "quit":
    break

  # Compare answers (case-insensitive)
  if user_answer.lower() == correct_capital.lower():
    print("Correct!")
    correct_count += 1
  else:
    print(f"Incorrect. The capital of {state} is {correct_capital}.")
    incorrect_count += 1

  print(
      f"Current Score -> Correct: {correct_count} | Incorrect:"
      f" {incorrect_count}\n"
  )

# Display final results
print("\n--- Quiz Finished ---")
print(f"Total Correct: {correct_count}")
print(f"Total Incorrect: {incorrect_count}")
PS G:\Users\James\AppData\Local\Programs\Microsoft VS Code> & C:\Users\James\AppData\Local\Python\pythoncore-3.14-64\python.exe "c:/Users/James/OneDrive - Laramie County Community College/COSC 1010/python/.py"
Welcome to the U.S. State Capital Quiz!
Type 'quit' anytime to stop the quiz.

What is the capital of South Carolina? Columbia
Correct!
Current Score -> Correct: 1 | Incorrect: 0

What is the capital of Indiana? Indianapolis
Correct!
Current Score -> Correct: 2 | Incorrect: 0

What is the capital of Wyoming? Cheyenne
Correct!
Current Score -> Correct: 3 | Incorrect: 0

What is the capital of New Jersey? Trenton
Correct!
Current Score -> Correct: 4 | Incorrect: 0

What is the capital of South Dakota? Bismarck
Incorrect. The capital of South Dakota is Pierre.
Current Score -> Correct: 4 | Incorrect: 1

What is the capital of Minnesota? St. Paul
Correct!
Current Score -> Correct: 5 | Incorrect: 1

What is the capital of South Carolina? quit

--- Quiz Finished ---
Total Correct: 5
Total Incorrect: 1
PS G:\Users\James\AppData\Local\Programs\Microsoft VS Code> 
