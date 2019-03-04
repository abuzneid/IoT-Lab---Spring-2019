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

def my_database(my_date,my_date1):

    conn=sqlite3.connect('attendance.db')
    c=conn.cursor()
    c.execute(""" SELECT fname,time,date from my_student WHERE date BETWEEN ? AND ?""",(my_date, my_date1))
    today = c.fetchall()

    print(today)

    conn.commit()
    c.close()
    conn.close()

if  __name__ == '__main__':
    my_database('2018-10-29','2018-10-30')
