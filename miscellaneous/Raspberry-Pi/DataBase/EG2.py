import sqlite3


def my_database():

    """

    :return: Nothing
    """
    # define the connection
    conn = sqlite3.connect("EG2.db")

    #define the cursor
    cursor = conn.cursor()

    # create Tables
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     temperature  TEXT, 
     humidity TEXT)""")

    # Add data to database
    cursor.execute("""
    INSERT INTO my_table (temperature,humidity) VALUES (?, ?)""",(4, 3))

    # perform 3C
    #COMMIT, CLOSE CLOSE
    conn.commit()
    cursor.close()
    conn.close()


if  __name__ == '__main__':
    my_database()
