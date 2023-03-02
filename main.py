#I imported these for the needed code.
import time
import random
print("welcome to the Magic 8-ball game")
#the list of potential answers the 8-ball can give
answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "signs point to yes", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful", "Reply hazy try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again"]
#this is the list of seconds that the prgram can take to pause and think.
pause = [1, 2, 3, 4, 5]

randomanswer = random.choice(answers)
random_pause = random.choice(pause)

while True: 
  question = input("8 ball will give you your fortune: ")
#this is the while loop that loops the entire program
  if question != "stop": 
    time.sleep(random_pause)
    print(randomanswer)
  elif question == "stop":
    break