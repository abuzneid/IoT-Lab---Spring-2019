import sqlite3

""""
Soumil Nitin Shah

Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

Graduate Teaching/Research Assistant
Python Developer

soushah@my.bridgeport.edu

simple reading values from database

"""


import sqlite3


def my_database():

    # define the connection
    conn = sqlite3.connect("eg3.db")

    #define the cursor
    cursor = conn.cursor()

    m = cursor.execute("""SELECT temperature FROM my_table WHERE temperature > 30 """)

    for x in m:
        print(x)


    conn.commit()
    cursor.close()
    conn.close()


if  __name__ == '__main__':
    my_database()
