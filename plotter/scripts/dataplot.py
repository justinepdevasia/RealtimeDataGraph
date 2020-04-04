import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random
import socket


# Initialize communication with magnetometer sensor
def get_data1():
    return random.random()
def get_data2():
    # sock=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    # sock.bind(("",3410))
    # while True:
    #     data,addr=sock.recvfrom(1024)

    return random.random()*2


# This function is called periodically from FuncAnimation


def setSubPlot(ax, xs, ys, title, xlab, ylab, fontsize=12,secondData=[]):
    ax.clear()
    ax.plot(xs,ys,color='b')
    if len(secondData)>0:
        ax.plot(secondData[0],secondData[1], color='r')
    
    ax.set_xlabel(xlab, fontsize=8)
    ax.set_ylabel(ylab, fontsize=10)
    ax.set_title(title, fontsize=10)
    ax.set_xticklabels(labels=xs, rotation=45 )
    


def animate(i, xs1, ys1, xs2, ys2):

    # Read temperature (Celsius) from TMP102
    temp_c1 = get_data1()
    temp_c2 = get_data2()

    # Add x and y to lists
    xs1.append(dt.datetime.now().strftime('%S.%f'))
    ys1.append(temp_c1)

    xs2.append(dt.datetime.now().strftime('%S.%f'))
    ys2.append(temp_c2)

    # Limit x and y lists to 50 items
    xs1 = xs1[-50:]
    ys1 = ys1[-50:]

    xs2 = xs2[-50:]
    ys2 = ys2[-50:]
    
    plt.subplots_adjust(bottom=0.30)
    setSubPlot(ax1, xs1, ys1,'Magnetometer data over time','sensor readings','angle measure', fontsize=10,secondData=[xs1,ys2])
    setSubPlot(ax2, xs2, ys2,'GPS data over time','sensor readings','angle measure', fontsize=10,secondData=[])

if __name__=="__main__":
    # Create figure for plotting
    fig,(ax1,ax2) = plt.subplots(nrows=2, ncols=1)
    fig.tight_layout(pad=5.0)
    #ax1 = fig.add_subplot(2, 2, 1)
    xs1 = []
    ys1 = []

    #ax2 = fig.add_subplot(2, 2, 2)
    xs2 = []
    ys2 = []


    # Set up plot to call animate() function periodically
    ani = animation.FuncAnimation(fig, animate, fargs=(xs1, ys1, xs2, ys2), interval=1500)
    plt.show()
