import threading

def donothing():
    threading.Timer(3,donothing).start()
    print('hello')

print("ahshaha")
print("asac")


donothing()


