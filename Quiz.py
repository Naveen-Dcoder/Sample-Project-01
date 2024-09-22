print("Welcome to the Quiz")

player = input('Do you want to play : ')

if player.lower() != "yes":
    quit()
    
print ('ok lets play')
score=0


question = input(" Who invented python? ")
if question.lower() == "Gudio van Rossum":
    print("correct")
    score+=1  
else:
    print("incorrect")
    
question = input("When did python inveted?")  
if question.lower() == "February 20,1991":
    print("correct")
    score+=1
else:
    print("incorrect")
    
question = input("What type of language is python?")
if question.lower() == "Interpreted language":
    print("correct")
    score+=1
else:
    print("incorrect")
    
question = input("Where did the name python came from?")
if question.lower() == "BBC TV show , Monty pythons Flying Circus":
    print("correct")
    score+=1
else:
    print("incorrect")
    
questuion = input("What type typing is used in pyhton?")
if question.lower() == "Dynamic typing":
    print("correct")
    score+=1
else:
    print("incorrect")
    
question = input("Do you like my project")    
if question.lower() == "yes":
    print("correct")
    score+=2
else:
    print("incorrect")
    
print("Your Score"+ str(score))
