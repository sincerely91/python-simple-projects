import time

true = ["T", "t", "True", "true"]
false = ["F", "f", "False", "false"]
correct = 0 #Storing the correct answers

name = input ("What's your name?") #Storing the user's name

print ("\nOK, " +  name +", let's get started. Remember, the following answers are only True or False (you can answer true as 't' and false as 'f')")
time.sleep(2)

print ("\nPython good for making commplex gmaes ")
choice = input(">>> ")
if choice in false:
  correct += 1 #If correct, the user gets one point
else:
  correct += 0
  
print ("\nEngland is not an island.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0  

print ("\nNorthern Ireland is part of Great Britian.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0 
  
print ("\nMicrosoft originated in the UK")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0  
  
print ("\nIran use to be part of the Perisan Empire.")
choice = input(">>> ")
if choice in true:
  correct += 1
else:
  correct += 0
  
print ("\nWasikstan is a real contry")
choice = input(">>> ")
if choice in false:
  correct += 1
else:
  correct += 0

print ("\nBONUS POINTS!: When adding a favicon to a website, the following HTML code would work: '<link rel=icon href=#'")
choice = input(">>> ")
if choice in false:
  correct += 2
else:
  correct += 0

time.sleep(1)
if correct <4:
    print ("\nOh no you got less than 4 right")
time.sleep(2)
print ("\nYou're finished, " + name +". You got", correct, "out of 8 possible points (7 questions, the last question was worth 2 points).")
