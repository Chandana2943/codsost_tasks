import random
import time
questions = { 1 : ["What is the capital of France?", "A. Berlin,B. Madrid,C. Paris,D. Rome"],
              2 : ["Which planet is known as the \"Red Planet\"?" , "A. Mercury,B. Venus,C. Mars,D. Jupiter"],
              3 : ["Who painted the Mona Lisa?", "A. Vincent van Gogh,B. Leonardo da Vinci,C. Pablo Picasso,D. Michelangelo"],
              4 : ["Which programming language is known for its use in web development and is often associated with frameworks like Django and Flask?","A. Java, B. Python, C. C++, D. Ruby"],
              5 : ["What does HTML stand for?","A. Hyper Transfer Markup Language, B. Hypertext Markup Language, C. Hyperlink and Text Markup Language, D. High-level Text Manipulation Language"],
              6 : ["Which programming concept allows a function to call itself?","A. Inheritance, B. Polymorphism, C. Recursion, D. Abstraction"],
              7 : ["Which scientist formulated the laws of motion and universal gravitation?","A.  Albert Einstein, B.  Isaac Newton, C.  Galileo Galilei, D.  Nikola Tesla"],
              8 : ["What does the acronym 'CPU' stand for?", "A.  Central Processing Unit, B.  Computer Processing Unit, C.  Central Processor Unit, D.  Core Processing Unit"],
              9 : ["Which data structure follows the 'First-In-First-Out' (FIFO.  principle?","A.  Stack, B.  Queue, C.  Array, D.  Linked List"],
              10 : ["What is the largest mammal on Earth?","A.  African Elephant, B.  Blue Whale, C.  Giraffe, D.  Polar Bear"],
              11 : ["Which programming language is often used for statistical analysis and data visualization?","A. Java, B. Python, C. C#, D. Ruby"],
              12 : ["which gas do plants absorb from the atmosphere during photosynthesis?","A. Nitrogen, B. Oxygen, C. Carbon Dioxide, D. Hydrogen"],
              13 : ["In which year did World War II end?","A. 1945, B. 1918, C. 1939, D. 1955"],
              14 : ["Which programming language uses curly braces '{}' to define code blocks?","A. Python, B. Java, C. Ruby, D. PHP"],
              15 : ["What is the chemical symbol for gold?","A. Go, B. Au, C. Ag, D. Gd"],
              16 : ["Which programming language is used for building Android applications?","A. Java, B. Python, C. C#, D. Ruby"],
              17 : ["What is the world's largest ocean?","A. Atlantic Ocean, B. Indian Ocean, C. Arctic Ocean, D. Pacific Ocean"],
              18 : ["Which programming language was created by Guido van Rossum?","A. Java, B. Python, C. C++, D. Ruby"],
              19 : ["What is the chemical symbol for water?","A. H2O, B. CO2, C. O2, D. N2"],
              20 : ["In which year did the United States declare its independence?","A. 1776, B. 1789, C. 1812, D. 1856"]}
answers = {1: "C", 2: "B", 3: "B", 4: "B", 5: "B", 6:"C", 7: "B", 8: "A", 9: "B", 10: "B", 11: "B", 12: "C", 13: "A", 14: "B", 15: "B", 16: "A", 17: "D", 18: "B", 19: "A", 20:"A"}
user = {}
def quiz(q):
  print(questions[q][0])
  for a in questions[q][1].split(","):
    print(a)
  user[q] = input("Enter your option: ").upper()
  if user[q] not in ["A" , "B" , "C" , "D"]:
    print("\033[31m"+"\033[1m"+"Please enter the A or B or C or D option only!"+ "\033[0m")
    quiz(q)
def firststep():
  setofquestions = []
  selected = []
  for i in questions.keys():
    setofquestions.append(i)
  for _ in range(5):
    question = random.choice(setofquestions)
    selected.append(question)
    setofquestions.remove(question)
  return selected
def game():
  setofquestions = firststep()
  for q in setofquestions:
    quiz(q)
    score = 0
  for q in user.keys():
    if user[q] == answers[q]:
      score += 100
    else:
      score -= 10
  print("Your score is:",score)
  play = input("Do you want to play again? (y/n): ")
  if play == "y":
    game()
def timeset(t):
  for i in range(t + 1):
    print(f"\rTime left: {t - i}", end="")
    time.sleep(1)
  print("\n")
print("Welcome to quiz")
print("rules: \nEnter options only from A,B,C,D\nyou will get 5 questions\nyou will get 100 points for each correct answer\nyou will get 10 points for each wrong answer")
timeset(5)
game()
