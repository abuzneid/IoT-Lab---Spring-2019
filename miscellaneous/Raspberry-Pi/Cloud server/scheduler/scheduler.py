import schedule
import time

def do_nothing():
    print("soumil shah")

schedule.every(10).seconds.do(do_nothing)

while 1:
    schedule.run_pending()
    time.sleep(1)