import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.backends.backend_tkagg import FigureCanvasAgg, NavigationToolbar2Tk
import numpy as np
from matplotlib import style
style.use('ggplot')


x  = []
y1 = []
y2 = []

fig = plt.figure()
ax1 = fig.add_subplot(111)

global counter
counter = 0

def sensor_random_value():

    x = np.random.randint(0, 20, None)              # create random value which resenble to sensor data Live
    y = np.random.randint(0, 20, None)              # create a another random variable to store Data Sensor 2

    my_sensor = "{},{}".format(x, y)                # create a Fake Data which represent the hardware data

    return my_sensor


def plot_data(i):                                    # plot the Graph
    global counter
    counter += 1
    x.append(counter)

    y1_data, y2_data = sensor_random_value().split(',')
    ax1.clear()

    y1.append(y1_data)
    y2.append(y2_data)

    ax1.plot(x, y1)


if __name__ == "__main__":                                               # run the code
    ani = animation.FuncAnimation(fig, plot_data, interval = 2000)
    plt.show()
