import psycopg2

connection=None
cur=None





def createTable():
    print("Creating Table")
    script = ''' CREATE TABLE IF NOT EXISTS student (
                    student_id      int PRIMARY KEY AUTO AUTO_INCREMENT,
                    first_name      varchar(255) NOT NULL,
                    last_name       varchar(255) NOT NULL,
                    email           varchar(255) NOT NULL UNIQUE,
                    enrollment_date DATE) '''
    cur.execute(script)
    connection.commit()

def populateTable():
    print("Populating Table")
    pop_s = 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)'
    pop_v = [('John', 'Doe', 'john.doe@example.com', '2023-09-01'), ('Jane', 'Smith', 'jane.smith@example.com', '2023-09-01'), ('Jim', 'Beam', 'jim.beam@example.com', '2023-09-02')]
    cur.execute(pop_s, pop_v)
    connection.commit()

def getAllStudents():
    print('Fetching all students')
    cur.execute('SELECT * FROM students')
    print(cur.fetchall())
    connection.commit()

def addStudent(first_name, last_name, email, enrollment_date):
    print("Adding a student")
    insert_s = 'INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s,%s,%s,%s)'
    insert_v = (first_name, last_name, email, enrollment_date)
    cur.execute(insert_s, insert_v)
    connection.commit()

def updateStudentEmail(student_id, new_email):
    print('Updating student')
    update_s = 'UPDATE students SET email = %s WHERE student_id = %s'
    update_v = (new_email, student_id)
    cur.execute(update_s,update_v)
    connection.commit()

def deleteStudent(student_id):
    print('Deleting student')
    delete_s = 'DELETE FROM students WHERE student_id = %s'
    delete_v = (student_id,)
    cur.execute(delete_s,delete_v)
    connection.commit()


try:
    connection = psycopg2.connect(
        host='localhost',
        dbname='a3p1',
        user='postgres',
        password='123',
        port = 5432
        )

    cur=connection.cursor()
    
    #createTable()

    #populateTable()

    #print('Testing getAllStudents()')    
    #getAllStudents()

    #print('Testing addStudent()')
    #addStudent("New", "Person", "newperson@example.com", '2024-03-18')

    #print("Testing updateStudent()")
    #updateStudentEmail(6, 'newestemail@example.com')

    print("Testing deleteStudent()")
    deleteStudent(6)







except Exception as error:
    print(error)

finally:
    if cur is not None:
        cur.close()
    if connection is not None:
        connection.close()