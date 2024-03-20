# a3p1
Simple Python - Postgres application

DEMO LINK: https://youtu.be/Zv5gdEhDw24

Setup instructions
Ensure Postgres and pgAdmin4 are installed,
Ensure Python 3  and pip are installed,
Run pip install psycopg2-binary in the terminal

Open pgAdmin4, create a new database and name it something like a3p1. Open the query tool on this database.
Take note of the host(likley localhost), the name of the database you entered in the previous step, the password you entered when setting up Postgres, and the port the database exists on(likley 5432)

Scroll to the try block in the application, around line 57, and enter the information above in the appropriate fields.

To create the table with the given schema run the createTable() function in the application.
To populate the table with the default data run the populateTable() function in the application
Alternativly, you run these queries using the query tool on the newly created database.

The rest of the functions provided work as described.

Test by un-commenting the functions as desired, starts at line 68.
