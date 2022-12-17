

import sqlite3

import pandas as pd

import bcrypt

import csv




connection = sqlite3.connect('cap_database.db')

db_cursor = connection.cursor()


def create_schema():
    with open('schema.sql', 'rt') as sql_queries:
    
        queries = sql_queries.read()
        db_cursor.execute(queries)
        
        connection.commit()

# create_schema()




def export_to_csv():


    with open('output.csv', 'w') as csv_file:
        csv_reader = csv.reader(csv_file)



        data = pd.read_sql_query('SELECT * FROM Assessment_Results', connection)

    


    if len(data) == 0:

        return

  

    else:

        data.to_csv('output.csv')












def login():



    email = input("Enter your email: \n")
    
    
    password = str(input("input password: ")) 
    

    password = password.encode('utf-8')
    

    hashed = bcrypt.hashpw(password, bcrypt.gensalt(10)) 
    


    check = str(input("check password: ")) 
    

    check = check.encode('utf-8') 
    
    
    db_cursor.execute("SELECT password FROM Users WHERE email =?", (email,)).fetchone()

    
    # db_cursor.execute("INSERT INTO Users WHERE password =?",(password)).fetchone()

    
    connection.commit()
    if bcrypt.checkpw(check, hashed):
        print("login success")
    else:
        print("incorrect password")

   


   

connection = sqlite3.connect('cap_database.db')

db_cursor = connection.cursor()



def add_user():

    print ("Adding User")
    
    first_name = input('Please enter first name: ')

    last = input('Please enter last name: ')

    phone = input ('Please enter phone number: ')

    email = input ('Please enter email: ')
    
    password = input('Please enter password: ')
    
    active = input ('Please Enter 1 -> (Active) 2 -> (Not Active: ')
    
    date_created = input('Please enter date created: ')

    date_hired = input('Please enter date hired: ')

    user_type = input('Please enter User or Manager: ')
    





    USERS = [first_name,last,phone,email,password,active,date_created,date_hired,user_type]

    



    db_cursor.execute('INSERT INTO Users (first_name, last_name, phone,email, password, active, date_created, hire_date, user_type) VALUES (?,?,?,?,?,?,?,?,?)',USERS)



    connection.commit()


def view_all_users(where=None):    
    if where:
        rows = db_cursor.execute("SELECT * FROM Users WHERE user_id LIKE ?", (where)).fetchall()
        
    else:   
        rows = db_cursor.execute("SELECT * FROM Users",)
    
    headers = [
        "user_id",
        "first_name",
        "last_name",
        "phone",
        "email",
        "password",
        "Active",
        "date_created",
        "higher_date",
        "user_type"
        
    ]

    print(
        #  id             firstn           lastn        email           phone         password        address        city          state          Zipcode        active
        f"{headers[0]:10}{headers[1]:12}{headers[2]:12}{headers[3]:14}{headers[4]:34}{headers[5]:15}{headers[6]:15}{headers[7]:17}{headers[8]:17}{headers[9]}")
    print(
        f'{"---------":10}{"---------":12}{"---------":12}{"------------":14}{"-----------------------":34}{"---------":15}{"---------":15}{"---------":17}{"---------":17}{"--------"}'
    )

    for row in rows:
        row = [str (i) for i in row]
        print(
            f"{row[0]:10}{row[1]:12}{row[2]:12}{row[3]:14}{row[4]:34}{row[5]:15}{row[6]:15}{row[7]:17}{row[8]:17}{row[9]}")




def add_competency():

    comp_name = input('Please enter competency Name: ')

    date_created = input('Please enter date created: ')

    competency_scale = input('Please enter competency value 0-4: ')

    

    COMPETENCIES = [comp_name,date_created,competency_scale]



    db_cursor.execute('INSERT INTO Competencies (comp_name, date_created, competency_scale) VALUES (?,?,?)',COMPETENCIES)

   
                

    connection.commit()


def view_all_competencies(where=None):    
    if where:
        rows = db_cursor.execute("SELECT * FROM Competencies WHERE Competency_id LIKE ?", (where)).fetchall()
        
    else:   
        rows = db_cursor.execute("SELECT * FROM Competencies",)
    
    headers = [
        "Competency_id",
        "comp_name",
        "date_created",
        "competency_scale",
        
    ]

    print(
        
        f"{headers[0]:17}{headers[1]:17}{headers[2]:17}{headers[3]}")
    print(
        f'{"---------":17}{"------------":17}{"------------":17}{"--------------"}'
    )

    for row in rows:
        row = [str (i) for i in row]
        print(
            f"{row[0]:17}{row[1]:17}{row[2]:17}{row[3]}")



def edit_Competency():

    db_cursor.execute('UPDATE Competencies SET comp_name = ? WHERE Competency_id = ?',(competency_score, competency_id))



def add_Assessment():

    assessment_name = input('please enter Assessment Name: ')

    date_created = input('Please enter date created: ')

    

    assessment_info = [assessment_name, date_created]



    db_cursor.execute('INSERT INTO Assessments (assessment_name, date_created) VALUES (?,?)', assessment_info)

    

    connection.commit()

def view_all_assessments(where=None):    
    if where:
        rows = db_cursor.execute("SELECT * FROM Assessments WHERE assessment_id LIKE ?", (where)).fetchall()
        
    else:   
        rows = db_cursor.execute("SELECT * FROM Assessments",)
    
    headers = [
        "assessment_id",
        "date_created",
        "assessment_name",
        
        
    ]

    print(
        
        f"{headers[0]:17}{headers[1]:17}{headers[2]}")
    print(
        f'{"---------":17}{"------------":17}{"------------"}'
    )

    for row in rows:
        row = [str (i) for i in row]
        print(
            f"{row[0]:17}{row[1]:17}{row[2]:17}")


def edit_Assessment():

    db_cursor.execute('UPDATE Assessments SET assessment_name = ? WHERE assessment_id =?',(assessment_id, assess_value)) # I need help I keep getting errors on all of my editing ones.
    



def add_assessment_result():

    

    user = input('please enter user: ')

    assessment_result_name = input(' Please name your assessment result: ')

    assessment = input('please enter assessment: ')

    assessment_result_id ('Please Enter The Result ID')
    
    score = input('Please enter the score: ')

    date_taken = input('Please enter the date taken: ')

    manager = input('please enter manager: ')





    ASSESSMENT_RESULTS = [user, assessment_result_name, assessment, assessment_result_id, score,date_taken, manager]

    

    db_cursor.execute('INSERT INTO Assessment_Results (user_id, assessment_result_name, assessment_id, score, date_taken, manager) VALUES (?,?,?,?,?,?)', ASSESSMENT_RESULTS)

    connection.commit()

def view_all_assessments_results(where=None):    
    if where:
        rows = db_cursor.execute("SELECT * FROM Assessments_Results WHERE assessment_result_id LIKE ?", (where)).fetchall()
        
    else:   
        rows = db_cursor.execute("SELECT * FROM Assessments",)
    
    headers = [
        
        "user_id"
        "assessment_result_name"
        "assessment_id",
        "assessment_result_id"
        "score",
        "date_taken",
        "manager"
        
        
    ]

    print(
        
        f"{headers[0]:17}{headers[1]:17}{headers[2]:17}{headers[3]:17}{headers[4]:17}{headers[5]:17}{headers[6]}")
    print(
        f'{"---------":17}{"------------":17}{"------------":17}{"---------":17}{"------------":17}{"------------":17}{"------------"}'
    )

    for row in rows:
        row = [str (i) for i in row]
        print(
            f"{row[0]:17}{row[1]:17}{row[2]:17}{row[3]:17}{row[4]:17}{row[5]:17}{row[6]:17}")

def edit_Assessment_Result():

    db_cursor.execute('UPDATE Assessment_Results SET assessment_results_name = ? WHERE assessment_result_id =?',(assess_value,assessment_result_id))




login()
while True:
    
    
    main_inquiry = input('''
    Welcome!
    Main Menu
    ----------
    
    1. User
    2. Manager
    3. Quit
    
    
    
   
    ''')
    
    
    if main_inquiry == '1':
        while True:
            user_choice = input ('''
            Welcome User
            1. Add User
            2. Go Back
            3. Exit
            
            
            ''')
            if user_choice == '1':
                add_user()
            
            elif user_choice == '2':
                break
            
            elif user_choice == '3':
                quit()
        
    
    elif main_inquiry == '2':
        while True:
            manager_choice = input ('''
            Welcome Manager
            1. Edit User

            2. Add Competency

            3. Edit Competency

            4. Add Assessment

            5. Edit Assessment

            6. Add Assessment Result

            7. Edit Assessment Result

            8. Export to CSV

            9. Go Back
            
            10. Exit
            
            
            ''')
    
            if manager_choice == '1':
                view_all_users()    
                user_id = input ('What user would you like to input: ')
                
                value = input ('Please provide a new value for this user: ')
                edit_query = "UPDATE Users SET first_name = ? WHERE user_id = ?;"
                result = db_cursor.execute(value, (user_id,)).fetchone()

                connection.commit()
               
    
            elif manager_choice == '2':
                add_competency()
            
            elif manager_choice == '3':
                view_all_competencies()
                competency_id = input('Which Competency?:')

                competency_score = input('Please provide a new value for this Competency:')

                edit_Competency(competency_score,competency_id)

        

                
                
            elif manager_choice == '4':
                
                add_Assessment()
                
            elif manager_choice == '5':
                view_all_assessments()
                assessment_id = input('Which Assessment?:')

                assess_value = input('Please provide a new value for this Assessment:')

                edit_Assessment(assessment_id,assess_value)
                
            elif manager_choice == '6':
                view_all_users()
                add_assessment_result()
                
            elif manager_choice == '7':
                view_all_assessments_results
                assessment_result_id = input('Which Assessment Results?:')

                asr_value = input('Please provide a new value for this Assessment Result:')

                edit_Assessment_Result(asr_value,assessment_result_id)

        
            
            elif manager_choice == '8':
                export_to_csv()
                
            elif manager_choice == '9':
                break
            
            elif manager_choice == '10':
                print("Thank you for coming!")
                quit()
                
            else:
                print ('Not a valid option! Try again.')
    
    
    elif main_inquiry == '3':
        print("Thank you for coming!")
        quit()    
    
    
    
    
        
        
  
        
        
