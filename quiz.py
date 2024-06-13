
print('Hii :) this is a quiz about how well do you know me')
answer=input(' Are you ready to take it? (yes/no) :')
score=0
total_questions=3
 
if answer.lower()=='yes':
    answer=input('Question 1: What is my Favourite Flower?')
    if answer.lower()=='sunflower':
        score += 1
        print('Right :)')
    else:
        print('Wrong :(')
 
 
    answer=input('Question 2: Do I like reading? ')
    if answer.lower()=='no':
        score += 1
        print('Correct, I do not like reading')
    else:
        print('Wrong :(')
 
    answer=input('Question 3: What is my favourite movie? Hint: It is a hindi movie ;)')
    if answer.lower()=='Kal Ho Nah Ho':
        score += 1
        print('absolutely!! I love SRK')
    else:
        print('You do not know me too well :(')
 
print('Thank you for taking this quiz',"you answered", score,"questions correctly!")
mark=(score/total_questions)*100
print('Marks obtained:',mark)
print('Bye bye')
