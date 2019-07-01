import sqlite3

""""
Soumil Nitin Shah

Bachelor in Electronic Engineering
Master in Electrical Engineering
Master in Computer Engineering

Graduate Teaching/Research Assistant
Python Developer

soushah@my.bridgeport.edu

"""

"""
CONVERTING DATABASE DATA TO LIST 
"""


import sqlite3

t = []

def my_database():

    # define the connection
    conn = sqlite3.connect("eg3.db")

    #define the cursor
    cursor = conn.cursor()

    m = cursor.execute("""SELECT * FROM my_table""")

    for x in m:
        print(x[0])
        t.append(x[0])



    conn.commit()
    cursor.close()
    conn.close()
    print(t)


if  __name__ == '__main__':
    my_database()
