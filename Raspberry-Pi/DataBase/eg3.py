""""
Soumil Nitin Shah

Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

Graduate Teaching/Research Assistant
Python Developer

soushah@my.bridgeport.edu
"""


try :
    import random
    import sqlite3
    import numpy as np
except:
    print("Error library not found")



def my_database(x, y):

    """

    :return: Nothing
    """

    # define the connection
    conn = sqlite3.connect("eg3.db")

    #define the cursor
    cursor = conn.cursor()

    # create Tables
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     temperature  TEXT, 
     humidity TEXT)""")

    # Add data to database
    cursor.execute("""
    INSERT INTO my_table (temperature,humidity) VALUES (?, ?)""",(x, y))

    # perform 3C
    #COMMIT, CLOSE CLOSE

    conn.commit()
    cursor.close()
    conn.close()


if  __name__ == '__main__':

    x = np.random.randint(0,40,None)
    y = np.random.randint(0,44,None)

    # pass sensor value to function
    my_database(x, y)
    print("added to database ")