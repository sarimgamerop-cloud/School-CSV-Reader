# Welcome to the CSV reader made by Special Yt :
# => this version currently contains some main commands:
# .percentage (to calculate out of given students what % passed.)
# .topper (to find out toppers.)
# .passlist (to see passed students and respective marks.)
# => Note:
# to change the marks criteria refer to the documentation or change the line90 as per need.



# Importing the CSV module:
import csv

# Created a List for storing the tuples (data_marks) to a list.
Data_list_marks = []

# Created a loop to iterate over the list:
# (This starts by taking a input , using it as opening a file
# and then extracting the csv rows. then the List Appending comes as discussed.)
while True:
    try:
        file_name = str(input(' • File to Locate (.csv) : '))
        with open(file_name, 'r') as main_file:
            reader = csv.reader(main_file)
            data_students, data_marks = zip(*[(row[0], int(row[1])) for row in reader])
            total_students = len(data_marks)
            for marks in data_marks:
                Data_list_marks.append(int(marks))
        break  
    except FileNotFoundError:
        print('File not Found.')

# a Simple Mathematical Function for calculating Percentage.
# (This calculates from the total number of people how many % passed.)
# Note: Uses a round() function , for precision try removing it ~
def percentage_of_passed(total_no_of_people_passed, total_students):
    percentage = (total_no_of_people_passed/total_students) * 100
    print(f'''
------------------------------------
{round(percentage)}% students passed.
------------------------------------ 
''')
    return percentage

# a Standard function to List all the passed students and locate their marks:
def passlist(data_std, data_mark):
    # Lists for easy data storage:
    data_listcreated = []
    passers_list_marks = []
    index_passers = []
    passed_students = []
    # loop to find every < 50 marks from the data_mark list
    # Change the lines according to your passing criteria.
    i = 0
    for num in data_mark:
        if num >= 50:
            # adds passing marks to a list.
            passers_list_marks.append(num)
            # the i = 0 is variable now used to find index.
            index_passers.append(i)
        i += 1
    
    # converted from a tuple to a list. (data_listcreated)
    for students in data_students:
        data_listcreated.append(students)
    
    # using the index_passers list to determine corresponding students:
    for index_students in index_passers:
        passed_students.append(data_listcreated[index_students])
    
    # handled to a terminal freindly function.
    passlist_decorater(passed_students,index_passers,Data_list_marks)


# Terminal Friendly Function:
# Note : This also does the task to find passed students exact marks
def passlist_decorater(list_passed,passers_index,All_marks):
    print("-" * 30)
    print('=> Passed Students :')
    print("-" * 30)
    # exact marks of passed students.
    for idx , i in zip(passers_index,list_passed):
        print(f"• {i} | Marks: {All_marks[idx]}")
    print("-"*30)


# Also Lists for easy data storage :
total = 0
total_marks = 100
passing_marks = 50
passed_toppers = []
failed_students = []

# Checks for passed students : ( < 50 )
for each_marks in data_marks:
    if each_marks >= passing_marks:
        passed_toppers.append(each_marks)
    # Checks for failed students (make use of it as per usage.)
    if each_marks < passing_marks:
        failed_students.append(each_marks)

# the main loop for taking instructions. breaking the logic can lead unstability.
while True:
    input_task = input(' What task to Perform ? : ')
    # .percentage command to call the percentage_of_passed function :
    if input_task == '.percentage':
        percentage_of_passed(len(passed_toppers) , total_students)
        break
    # .topper command to determine toppers: ( create a seperate function for easy usage and clean code.)
    elif input_task == '.topper':
        highest_topper = max(data_marks)
        print("==========================================================")
        for idx,marks in enumerate(data_marks):
            if marks == highest_topper: 
                topper_name = data_students[idx]     
                print(f'{topper_name} with the score of {marks} is topper')
        print("==========================================================")        
        break
    # .passlist function to call the passlist function.
    elif input_task == '.passlist':
        passlist(data_students,Data_list_marks)
        break
    else:
        print('Invalid Choice')
