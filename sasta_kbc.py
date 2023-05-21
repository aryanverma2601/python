print("APKA SWAGAT HAI KON BANEGA SASTA KARODPATI MAI\n")
print("And your next question is for 200k rupees\n")
ll="You have only one lifeline which is 50:50\n"
ques="Who was the founder of Sisodiya dynasty?"
options=["A:Rana Hammir","B:Maharana Pratap","C:Bapa Rawal","D:Udai Singh","E:Use lifeline"]
right="A"
print(ques,"\n",ll)

for i in range(0,5):
    print(options[i])
ans=input("Enter your option:\n")
if(ans=="E"):
    print("you have use your last lifeline 50:50\n")
    print(options[0],options[3])    
    ans=input("Enter your option: \n")
    if(right==ans):
        print("you have won 200k rupees\n")
    else:
        print("you choosed the wrong option and loosed 200k rupees\n")
elif(right==ans):
    print("You are absolutely right","You have won 200k rupees\n")
elif(right!=ans and ans!="E"):
    print("you have choosed the wrong option\n")
