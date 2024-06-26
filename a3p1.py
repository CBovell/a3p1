import psycopg2

connection=None
cur=None




#This function creates a table based on the provided schema
def createTable():
    print("Creating Table")
    script = ''' CREATE TABLE IF NOT EXISTS students (
                    student_id      SERIAL PRIMARY KEY,
                    first_name      varchar(255) NOT NULL,
                    last_name       varchar(255) NOT NULL,
                    email           varchar(255) NOT NULL UNIQUE,
                    enrollment_date DATE) '''
    cur.execute(script)
    connection.commit()

#This function populates the students table with the default, provided data
def populateTable():
    print("Populating Table")
    pop_s = 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)'
    pop_v = [('John', 'Doe', 'john.doe@example.com', '2023-09-01'), ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')]
    for entry in pop_v:
        cur.execute(pop_s,entry)
    connection.commit()

#This function fetches all of the students currently in the database
def getAllStudents():
    print('Fetching all students')
    cur.execute('SELECT * FROM students')
    print(cur.fetchall())
    connection.commit()

#This function takes in paramaters firstname, lastname, email, and enrollmentdate and creates a new entry in the database based on this provided information
def addStudent(first_name, last_name, email, enrollment_date):
    print("Adding a student")
    insert_s = 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s)'
    insert_v = (first_name, last_name, email, enrollment_date)
    cur.execute(insert_s, insert_v)
    connection.commit()

#This function takes in a unique studentID and a new email and updates the correct entry in the database with the new information
def updateStudentEmail(student_id, new_email):
    print('Updating student')
    update_s = 'UPDATE students SET email = %s WHERE student_id = %s'
    update_v = (new_email, student_id)
    cur.execute(update_s,update_v)
    connection.commit()

#This function deletes a student in the database in based on their unique studentID
def deleteStudent(student_id):
    print('Deleting student')
    delete_s = 'DELETE FROM students WHERE student_id = %s'
    delete_v = (student_id,)
    cur.execute(delete_s,delete_v)
    connection.commit()


try:
    #Needed for connetion, replace with own data
    connection = psycopg2.connect(
        host='localhost',
        dbname='a3p1',
        user='postgres',
        password='123',
        port = 5432
        )

    cur=connection.cursor()

    #Testing starts here, un-comment the desired function to run

    #createTable()

    #populateTable()

    #print('Testing getAllStudents()')    
    #getAllStudents()

    #print('Testing addStudent()')
    #addStudent("New", "Person", "newperson@example.com", '2024-03-18')

    #print("Testing updateStudent()")
    #updateStudentEmail(4, 'newestemail@example.com')

    #print("Testing deleteStudent()")
    #deleteStudent(4)






#Incase of an error
except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if connection is not None:
        connection.close()
