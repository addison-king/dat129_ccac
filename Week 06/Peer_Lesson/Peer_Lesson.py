"""
Brandyn Gilbert
    Tue Mar 10 12:49:54 2020
    Python 2 - DAT-129 - Spring 2020
    Homework #####
    TITLE OF HOMEWORK
"""
#PLAN
import pandas as pd
import sqlite3
import os


def main():
    '''
    Example on how to take a .csv file and store it into a database using
        sqlite3. We use pandas to extract all of the csv data. Then we use
        pandas to store it all into the database.
    Once our database is created and filled, we use a cursor to navigate the
        database and extract data from it. Then we print it.
    Do NOT forget to close the connection to the database. If you open a
        connection to a databse and your code fails with the connection open,
        then it stays open. You have to then close your editor to terminate
        the connection.

    Returns
    -------
    None.

    '''
  # if the database exists, delete the file...we do this only for testing
    if os.path.exists("Peer_Lesson_Jail.db"):
        os.remove("Peer_Lesson_Jail.db")
  # use pandas to read the csv into a dataframe
    df = pd.read_csv('jail.csv')
  # strip the dataframe of white space
    df.columns = df.columns.str.strip()
  # create a connection to the database..creates it if it doesn't exist
    connection = sqlite3.connect('Peer_Lesson_Jail.db')
  # use pandas to send the dataframe to the database, into the table 'Jail'
    df.to_sql('Jail', connection)

    ####################### PRINTING #######################

  # create a cursor to navigate the database
    cursor_obj = connection.cursor()

  # 1st example :: use 'execute' to select headers, from our table
  # the SELECT order is important. it is the order in which it will print
    cursor_obj.execute('SELECT race, gender, COUNT(*), date \
                       FROM Jail \
                       WHERE race= "W" AND gender= "M" \
                       GROUP BY date')
  # store the info in our cursor to a variable
    data = cursor_obj.fetchall()
  # iterate through the data and print it
    for i in data:
        print(i)

    print('----------------------------------------------------------------')
  # 2nd example :: use 'execute' to select headers, from our table
  # the SELECT order is important. it is the order in which it will print
    cursor_obj.execute('SELECT date, race, gender, COUNT(race) \
                        FROM Jail \
                        WHERE Age_Current < 20 and race= "B" \
                        GROUP BY date \
                        ORDER BY date DESC')
  # store the info in our cursor to a variable
    data = cursor_obj.fetchall()
  # iterate through the data and print it
    for i in data:
        print(i)

  # close the connection :: VERY IMPORTANT
    connection.close()

if __name__ == "__main__":
    main()
