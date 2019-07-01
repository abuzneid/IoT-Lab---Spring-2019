import RPi.GPIO as GPIO
import time
import datetime

#GPIO Mode (BOARD / BCM)
GPIO.setmode(GPIO.BCM)

#set GPIO Pins
GPIO_TRIGGER = 17
GPIO_ECHO = 27

#set GPIO direction (IN / OUT)
GPIO.setup(GPIO_TRIGGER, GPIO.OUT)
GPIO.setup(GPIO_ECHO, GPIO.IN)

def get_time():
    t = datetime.datetime.now()
    my_time ='{}:{}:{}'.format(t.hour,t.minute,t.second)
    return my_time


def distance():
    # set Trigger to HIGH
    GPIO.output(GPIO_TRIGGER, True)

    # set Trigger after 0.01ms to LOW
    time.sleep(0.00001)
    GPIO.output(GPIO_TRIGGER, False)

    StartTime = time.time()
    StopTime = time.time()

    # save StartTime
    while GPIO.input(GPIO_ECHO) == 0:
        StartTime = time.time()

    # save time of arrival
    while GPIO.input(GPIO_ECHO) == 1:
        StopTime = time.time()

    # time difference between start and arrival
    TimeElapsed = StopTime - StartTime
    # multiply with the sonic speed (34300 cm/s)
    # and divide by 2, because there and back
    distance = (TimeElapsed * 34300) / 2

    my_time = get_time()
    my_database(distance, my_time)

    return distance

def my_database(distance,my_time):

    """

    :return: Nothing
    """
    # define the connection
    conn = sqlite3.connect("distance.db")

    #define the cursor
    cursor = conn.cursor()

    # create Tables
    cursor.execute("""
     CREATE TABLE IF NOT EXISTS my_table (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
     distance  TEXT, 
     my_time TEXT)""")

    # Add data to database
    cursor.execute("""
    INSERT INTO my_table (distance,my_time) VALUES (?, ?)""",(distance, my_time))

    # perform 3C
    #COMMIT, CLOSE CLOSE
    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)

        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()