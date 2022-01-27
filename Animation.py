# plot_web_api_realtime.py
"""
A live auto-updating plot of random numbers pulled from a web API
"""

import time
import datetime as dt
import requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation

url = "https://qrng.anu.edu.au/API/jsonI.php?length=1&type=uint8"


# function to pull out a float from the requests response object
def pull_float(response):
    jsonr = response.json()
    strr = jsonr["data"][0]
    if strr:
        fltr = round(float(strr), 2)
        return fltr
    else:
        return None


# Create figure for plotting
fig, ax = plt.subplots()
xs = []
ys = []


def animate(i, xs: list, ys: list):
    # grab the data from thingspeak.com
    response = requests.get(url)
    flt = pull_float(response)

    # Add x and y to lists
    xs.append(dt.datetime.now().strftime('%H:%M:%S'))  # Time
    ys.append(flt)  # Random number

    # Limit x and y lists to 10 items
    xs = xs[-10:]
    ys = ys[-10:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    ax.set_ylim([0, 255])


# Set up plot to call animate() function every 1000 milliseconds
ani = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)

plt.show()
