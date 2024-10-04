#Create a Python program that captures and displays a person's to­do list. 
#Continually prompt the user for another item until they enter a blank item. 
#After all the items are entered, display the to­do list back to the user.

#output
#Your ToDo List:
#Buy cat food.
#Mow the lawn.
#Take over the world.

Taskdone=False
AllList=[]
while Taskdone==False:
    TodoList=input("Enter a task for your to­do list.  Press <enter> when done:")
    
    if TodoList=='':
         Taskdone=True
    else:
        AllList.append(TodoList)
        
print()
print("Your ToDo List:")
print("----------------")
for TodoList in AllList:
    print(TodoList)
    
        
    

        
