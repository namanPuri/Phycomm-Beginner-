import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import time

class Plotter:

    def __init__(self, fig, ax, gen_func, style = 'b', timeSeconds = 10):
        self.fig = fig
        self.ax = ax
        self.timeSeconds = timeSeconds
        self.style = style
        self.xdata = []
        self.ydata = []
        self.ax.set_xlim((0, self.timeSeconds))
        self.ax.set_ylim((-0.1, 1.1))
        self.gen_func = gen_func
        self.ln, = self.ax.plot(self.xdata, self.ydata, self.style)

    def update(self, data):
        self.xdata.append(data[0])
        self.ydata.append(data[1])
        self.ln.set_data(self.xdata, self.ydata)
        return self.ln,

    def gen(self):
        self.start_time = time.time()
        while time.time() - self.start_time <= self.timeSeconds:
            yield (time.time() - self.start_time, (self.gen_func)())

        
        
