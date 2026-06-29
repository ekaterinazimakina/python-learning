A simple command-line number guessing game written in Python.
The player tries to guess a randomly generated number within a chosen range and limited number of attempts based on difficulty level.
Created as a Python learning project to practice:
- loops
- functions
- input validation
- control flow
- basic game logic

Features
User-defined number range
Three difficulty levels:
- Easy (more attempts)
- Medium (balanced)
- Hard (optimal number of attempts)
Input validation (only positive integers allowed)
Feedback after each guess:
- “too high”
- “too low”
- “out of range”
Tracks number of attempts used
Option to replay the game

How the game works
The player enters a numeric range (start and end).
The program randomly selects a number within that range.
The player selects a difficulty level:
Easy → more attempts
Medium → moderate attempts
Hard → minimal attempts (based on logarithmic formula)
The player tries to guess the number.
After each guess, the game gives hints.
The game ends when:
The number is guessed correctly, OR Attempts run out
The player can choose to play again.
