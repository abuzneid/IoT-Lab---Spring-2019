""""
Soumil Nitin Shah

Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

Graduate Teaching/Research Assistant
Python Developer

soushah@my.bridgeport.edu
"""


import sqlite3


def my_database():

    """

    :return: Nothing
    """
    # define the connection
    conn = sqlite3.connect("eg1.db")

    #define the cursor
    cursor = conn.cursor()

    # create Tables
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     temperature  TEXT, 
     humidity TEXT)""")

    # Add data to database
    cursor.execute("""
    INSERT INTO my_table (temperature,humidity) VALUES (4,3)""")

    # perform 3C
    #COMMIT, CLOSE CLOSE
    conn.commit()
    cursor.close()
    conn.close()


if  __name__ == '__main__':
    my_database()
