#=====importing libraries===========
'''This is the section where you will import libraries'''
from datetime import datetime                              # source: https://www.digitalocean.com/community/tutorials/python-string-to-datetime-strptime; using library to work with dates; I did not know how to get the  current date

#====Login Section====
'''Here you will write code that will allow a user to login.
    - Your code must read usernames and password from the user.txt file
    - You can use a list or dictionary to store a list of usernames and passwords from the file.
    - Use a while loop to validate your user name and password.
'''
print('-------------Welcome to task manager-------------\n\n')
security = {}                                   #An empty dictionary to store login details from user.txt

'''Opening user.txt to read the file, iterating through the lines in user.txt, 
stripping each line off the \n character, splitting the username and password using the comma and 
space as a delimiter and finally storing each username (item[0]) and password (item[1]) in a dictionary. 
The username is the key :
'''
with open('user.txt','r') as userfile:          
    row = userfile.readlines() 
    for item in row:                            
        item = item.strip()                     
        item = item.split(', ')                 
        security[item[0]] = item[1]             

username = input('Enter a username: ')
password = input('Enter your password: ')
correct_user, correct_pass, correct_combo = False, False, False     # these booleans will be used to validate the password. 
                                                                    # they represent the username, password and the combination of the username and password.

while correct_combo == False:                                       # using a while loop to prompt user to enter login details every time the combination is wrong, i.e False  
    if username in security:                                        
        correct_user = True                                         # the username will be True if it exists in the dictionary.
        if password == security[username]:
            correct_pass = True                                     # the password will be true if it matches the value associated with the key (username) in the dictionary
    correct_combo = correct_user and correct_pass                   # the username and password should both be correct in order for the combination to be correct (True)
    if correct_combo == False:
        print('Invalid login details. Please try again')            # if the combination is incorrect (False), the user is prompted to enter the login details again
        username = input('Enter a username: ')
        password = input('Enter your password: ') 
    else:                                                           # if the combination is correct (True), Access is granted and the user can continue with the program
        print('\nAccess granted\n') 

if username == 'admin':
    admin_stats = 's - view statistics'
else:
    admin_stats = ''

while True:
    #presenting the menu to the user and 
    # making sure that the user input is coneverted to lower case.
    menu = input(f'''Select one of the following Options below:
{admin_stats}
r - Registering a user
a - Adding a task
va - View all tasks
vm - view my task
e - Exit
: \n''').lower()


    if menu == 'r':
        pass
        '''In this block you will write code to add a new user to the user.txt file
        - You can follow the following steps:
            - Request input of a new username
            - Request input of a new password
            - Request input of password confirmation.
            - Check if the new password and confirmed password are the same.
            - If they are the same, add them to the user.txt file,
            - Otherwise you present a relevant message.'''
        if username == 'admin':                                             #If the user is admin they can add a new user
            new_user = input('Enter the new username: ')                    # prompting the admin to enter the new login details
            new_password = input("Enter the user's new password: ")
            confirm_password = input("Confirm new password: ")

            while new_password != confirm_password:                         # using while loop to ensure that the password confirmation matches the password entered.
                print('The passwords do not match. Please try again.')
                new_password = input("Enter the user's new password: ")
                confirm_password = input("Confirm new password: ")

            with open('user.txt','a') as userfile:                          
                userfile.write('\n' + new_user + ', ' + new_password)       # on a new line, the user's login details will be added
            
            security[new_user] = new_password                               # adding new user details to the users dictionary (security)
        else:
            print('\nYou are not authorized to add a new user. Only the Admin user can add a new user\n') 

    elif menu == 'a':
        pass
        '''In this block you will put code that will allow a user to add a new task to task.txt file
        - You can follow these steps:
            - Prompt a user for the following: 
                - A username of the person whom the task is assigned to,
                - A title of a task,
                - A description of the task and 
                - the due date of the task.
            - Then get the current date.
            - Add the data to the file task.txt and
            - You must remember to include the 'No' to indicate if the task is complete.'''
        task_user = input('Username of the person whom the task is assigned to: ')  # prompting user to enter details
        while task_user not in security:                                            # validity test. checks if user exists 
            print('User not found.')
            task_user = input('Username of the person whom the task is assigned to: ')  # prompting user to enter details
        task_title = input('Title of the task: ')
        task_description = input('Task description: ')
        due_date = input('Task due date [dd/mm/yyyy]: ')
        task_due = datetime.strptime(due_date,'%d/%m/%Y').date()      # converting the due_date into a date format. Source: Digital Ocean
        current_date = datetime.today().date()
        task_completed = 'No'
        task_due = task_due.strftime('%d %b %Y')                                    # changing task due date into correct string formatting (Eg: 11 Oct 2021). Source Digital Ocean                         
        current_date = current_date.strftime('%d %b %Y')                            # changing current date into correct string formatting (Eg: 11 Oct 2021). Source Digital Ocean


        with open('tasks.txt','a') as taskfile:                                      # opening tasks.txt file to append new task details
            taskfile.write(f'\n{task_user}, {task_title}, {task_description}, {task_due}, {current_date}, {task_completed}' )

        

    elif menu == 'va':
        pass
        '''In this block you will put code so that the program will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file.
            - Split that line where there is comma and space.
            - Then print the results in the format shown in the Output 2 
            - It is much easier to read a file using a for loop.'''
        mydata = []                                      #Used to store data from user.txt
        with open('tasks.txt','r') as userfile:         
            row = userfile.readlines() 
            for item in row:                             #iterating through the lines in tasks.txt
                item = item.strip()                     
                item = item.split(', ')                  
                mydata.append(item)                      #appending each item of the task into mydata (list)
            

        description = ['User\t','Title\t','Description','Date assigned','Due date','Task complete'] #Descriptions of tasks
        for Row in range(len(mydata)):                   # Row = the index of each line read from tasks.txt stored in mydata
            print(f"Task {Row+1}:")
            for Col in range(len(mydata[Row])):          # Col = the index of each task description stored in mydata
                print(f"\t\t {description[Col]}\t\t {mydata[Row][Col]}")
            print('\n')

    elif menu == 'vm':
        pass
        '''In this block you will put code the that will read the task from task.txt file and
         print to the console in the format of Output 2 in the task PDF(i.e. include spacing and labelling)
         You can do it in this way:
            - Read a line from the file
            - Split the line where there is comma and space.
            - Check if the username of the person logged in is the same as the username you have
            read from the file.
            - If they are the same print it in the format of Output 2 in the task PDF'''
        mydata = []                                   
        with open('tasks.txt','r') as userfile:         
            row = userfile.readlines() 
            for item in row:                             #iterating through the lines in tasks.txt
                item = item.strip()                      
                item = item.split(', ')                  
                mydata.append(item)                      #appending each item of the task into mydata (list)

        description = ['User\t','Title\t','Description','Date assigned','Due date','Task complete'] #Descriptions of tasks
        print("My tasks")
        
        #Using the code from 'va' section to view tasks if username is the same as the user in mydata
        for Row in range(len(mydata)):
            if username == mydata[Row][0]:               #comparing the username to the user stored in mydata. If they match the task details will be printed
                for Col in range(len(mydata[Row])):
                    print(f"\t\t {description[Col]}\t\t {mydata[Row][Col]}")
                print('\n') 
    
    if menu == 's' and username == 'admin':             #statistics menu. the number of lines in the userfile is the number of users. same applies to tasks
        pass
        ufile = open('user.txt', 'r')
        tfile = open('tasks.txt','r')
        print('\n----------------------STATISTICS------------------------\nTotal number of tasks:', len(tfile.readlines()),"\t\t Total users:", len(ufile.readlines()),'\n\n')

    elif menu == 'e':
        print('Goodbye!!!')
        exit()

    else:
        print("You have made a wrong choice, Please Try again")