# this is a question and answer program with pasword for accessability and it shows the performance of each # QUESTION:
def Questions(): # questions
    myscore=[]
    print ('chose the appropiate answer\nyour answer should be in either a,b,or c')
    print("what is the capital of Nigeria (a) Abuja (b) Lagos (c) Kano")
    Question1 = input()
    if Question1 == "a":
        myscore.insert(0,5)
    else:
        myscore.insert(0,0)
    print("what is the capital of Ghana (a) Abuja (b) Accra (c) Kano")
    Question2 = input()
    if Question2 == "b":
        myscore.insert(1,5)
    else:
        myscore.insert(1,0)
    print("what is the capital of anambara state (a) Abuja (b) Accra (c) Awka")
    Question3 = input()
    if Question3 == "c":
        myscore.insert(2,5)
    else:
        myscore.insert(2,0)
    print('who is the president of Nigeria \t(a)Buhari (b)TRUMP (c)obansanjo\n')
    Question4 = input()
    if Question4 == "a":
        myscore.insert(3,5)
    else:
        myscore.insert(3,0)
    print('who is the life leader of China \t(a)li keqiang (b)TRUMP (c)xi ping\n')
    Question5 = input()
    if Question5 == "c":
        myscore.insert(4,5)
    else:
        myscore.insert(4,0)
    print('who is the president of USA \t(a)Buhari (b)TRUMP (c)Goodluck\n')
    Question6 = input()
    if Question6 == "b":
        myscore.insert(5,5)
    else:
        myscore.insert(5,0)
    score =sum (myscore)
    print('your score is \n',score)
    if(score > 20):
	    print('you did great')
    if(score == 20):
	    print('your score is fairly ok')
    if(score==0):
	    print('your score is pathetic and a disgrace')
    if(score < 15):
	    print('you tried but you have to do better')
    if(score==5):
	    print('you are no trying')
    print("your question and their repective score is listed below")
    my_questions = ["Question_1","Question_2","Question_3","Question_4","Question_5","Question_6"]
    for question,score in zip(my_questions,myscore):
        print(question,score)
    I = myscore
    filename="result2.txt"
    with open(filename,'w') as file:
        for result in I:
            file.write(result+"\n")


# the candidate registering his bio detail and pasword
firstname = input ('first name\n')
secondname = input ('second name\n')
age = input ('your age\n')
reg_password = input ('register your password\n')
for password in reg_password:
    password = input("please enter your password\n")
    if reg_password == password:
        print("you are logged in")
        input("press enter to continue")
        print ('your first name\n',firstname,'\nyour second name\n',secondname,'\n your age\n',age)
        Questions()
        break
    else:
        print("wrong password try again")
