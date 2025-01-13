#sadie levitt
#01/13


import time

import random

x=int(input("How many questions do you want?"))
start_time = time.time()
score=0
count=0
while (x>0):
    m1=random.randint(1,10)

    m2=random.randint(1,10)

    ans=int(input("what is "+str(m1)+" times "+str(m2)))
    right=m1*m2
    if ans==right:
        print("correct")
        x-=1
        score+=1
        count+=1
    else:
        print("wrong")
        x-=1
        count+=1
end_time = time.time()
elapsed_time = end_time - start_time
print("your score: "+str(score)+"/"+str(count))
print("You completed the test in " +str(elapsed_time) + " seconds")
