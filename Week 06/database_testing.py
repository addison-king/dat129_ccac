"""
Brandyn Gilbert
    Fri Mar  6 09:06:00 2020
    Python 2 - DAT-129 - Spring 2020
    Homework 6
    Databases
"""
#PLAN

import sqlite3
from sqlite3 import Error

def _sql_connection():

    try:
        connection = sqlite3.connect('week06_test.db')
        return connection

    except Error:
        print(Error)

def _create_sql_table(connection):
    cursor_object = connection.cursor()
    cursor_object.execute('CREATE TABLE IF NOT EXISTS \
        employees(id integer PRIMARY KEY, name text, salary real, \
                  department text, position text, hireDate text)')
    connection.commit()
    input('1')


def _insert_into_table(connection):
    entity1 = (2, 'Andrew', 850, 'IT', 'Tech', '2018-02-06')
    entity2 = (4, 'Bob', 1000, 'Lab', 'Tech', '2018-03-06')
    entity3 = (5, 'Sarah', 750, 'IT', 'Tech', '2018-05-16')
    entity4 = (6, 'Ron', 500, 'IT', 'Intern', '2018-08-01')

    entities = [entity1, entity2, entity3, entity4]

    cursor_object = connection.cursor()
    cursor_object.execute("INSERT INTO employees VALUES(1, 'John', \
                          700, 'HR', 'Manager', '2017-01-04')")
    cursor_object.execute("INSERT INTO employees VALUES(3, 'Mike', \
                          900, 'Lab', 'Tech', '2019-12-14')")


    for i in entities:
        cursor_object.execute("INSERT INTO employees (id, name, salary, \
                          department, position, hireDate) \
                          VALUES(?, ?, ?, ?, ?, ?)", i)
    connection.commit()
    input('2')


def _update_sql_table(connection):
    cursor_object = connection.cursor()
    cursor_object.execute('UPDATE employees SET name = "Rogers" where id = 2')
    connection.commit()
    input('3')

def _print_sql_table(connection):
    cursor_object = connection.cursor()
    cursor_object.execute('DELETE FROM employees WHERE salary > 950')
    # cursor_object.execute('SELECT * FROM employees')
    cursor_object.execute('SELECT id, name, salary FROM employees WHERE salary > 800')

    rows = cursor_object.fetchall()
    for i in rows:
        print((i))

def main():

    connection = _sql_connection()
    _create_sql_table(connection)
    # _insert_into_table(connection)
    # _update_sql_table(connection)
    _print_sql_table(connection)
    connection.close()

if __name__ == "__main__":
    main()
