import json
import math

# Get the JSON data of the quiz
def return_quiz(filename):
  file = open(filename)
  return json.load(file)

def is_ai_correct(ai_guess, correct_answers):
  # Check for each item in the correct answer array
  if(not isinstance(correct_answers, list)):
    correct_answers = [correct_answers]
  for answer in correct_answers:
    if answer.lower() in ai_guess.lower():
      return True
  return False
def get_ai_guess(prompt):
  # Call your AI here and return the string you get (Do NOT include the prompt in the output)
  guess = "Paris"
  return guess

def form_ai_question_prompt(question):
  # You may want to fiddle with the prompt, it will likely affect the AI's preformance.
  return "Q: What is the largest city in Australia?\nA: Sydney\nQ: " + question + "\nA:"

def ask_ai_question(question_for_ai, correct_answer):
  prompt = form_ai_question_prompt(question_for_ai)
  guess = get_ai_guess(prompt)
  return is_ai_correct(guess, correct_answer)

def main():
  class score:
    def __init__ (self, correct_answers, quiz_length):
      self.percent = (correct_answers / quiz_length) * 100
      self.interval = math.sqrt((1 - (self.percent / 100)) * (self.percent / 100) / quiz_length) * 164.5
      self.lower_interval = self.percent - self.interval
      self.upper_interval = self.percent + self.interval
  
  quiz = return_quiz("quiz.json")
  quiz_type = "memorizing" # At this moment, only the memorizing quiz is availible, if you are looking at this in the future, the reasoning quiz will probably be available.
  quiz_lvl = "lvl1" # In the future, there will be a lvl 1, 2, 3, and 4, which each one being more difficult than the last
  quiz_length = len(quiz["quiz"][quiz_type][quiz_lvl]["questions"])
  correct_answers = 0
  print("This part of the quiz is", quiz_length, "questions")
  for current_question in quiz["quiz"][quiz_type][quiz_lvl]["questions"]:
    # print(current_question)
    correct_answers += ask_ai_question(current_question["question"], current_question["answer"])
  print("The AI got", correct_answers, "correct answer(s) out of", quiz_length, "questions.", "The AI got a percentage of", (correct_answers / quiz_length) * 100, "%")
  score = score(correct_answers, quiz_length)
  print("With a 90% confidence, the grade is between:", score.lower_interval, "% -", score.upper_interval, "%")
main()
