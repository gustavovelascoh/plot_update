'''
Created on Jan 29, 2017
@author: gustavo
'''
import tkinter as tk
import sys
from numpy import arange, sin, pi, random


sys.path.append("..")

from viewer import Viewer

class Multiplot(tk.Frame):
    def __init__(self, master):
        tk.Frame.__init__(self, master)
        button_frame = tk.Frame(self)
        button_bg = tk.Button(button_frame, text="Save as BG",
                           command=self.save_as_bg)
        button_bg.pack(side="left")
        button_a = tk.Button(button_frame, text="Plot A",
                           command=self.plot_a)
        button_a.pack(side="left")
        button_b = tk.Button(button_frame, text="Plot B",
                           command=self.plot_b)
        button_b.pack(side="left")
        button_c = tk.Button(button_frame, text="Plot C",
                           command=self.plot_c)
        button_c.pack(side="left")
        button_d = tk.Button(button_frame, text="Plot d",
                           command=self.plot_d)
        button_d.pack(side="left")
        button_clr = tk.Button(button_frame, text="Clear all",
                           command=self.clear_all)
        button_clr.pack(side="left")
        button_frame.pack(side="top")



        self.viewer = Viewer(self)
        self.viewer.pack()

        roi={"ymin":-2,"ymax":2,"xmin":-10,"xmax":10}
        self.viewer.set_roi(roi)
        self.viewer.canvas.draw()
        self.viewer.update()


    def plot_d(self):
        t1 = arange(-3*random.rand(), 3*random.rand(), 0.01)
        t2 = arange(-3*random.rand(), 3*random.rand(), 0.01)
        self.viewer.plot(t1,t1,color='red')
        self.viewer.plot(t2,-t2,color='red')
        self.viewer.update()

#        self.viewer.canvas.draw()
 #       self.viewer.save_background()

    def plot_a(self):
        t = arange(0.0, 3.0, 0.01)
        s = sin(2*pi*t)

        self.viewer.plot(t,s,color='black')
        self.viewer.update()



    def plot_b(self):
        t1 = arange(0.0, 3.0, 0.01)
        s1 = sin(pi*t1)-1
        t2 = arange(-1.0, 1.0, 0.01)
        s2 = sin(4*pi*t2) + 1

        self.viewer.plot(t1,s1,color='purple')
        self.viewer.plot(t2,s2,color='green')
        self.viewer.update()

    def plot_c(self):
        x = 5*random.rand(1,20)-1.5
        y = 2*random.rand(1,20)-1

        self.viewer.plot(x,y,color='blue', linestyle=" ", marker='o')

        self.viewer.update()

        pass

    def save_as_bg(self):
        self.viewer.canvas.draw()
        self.viewer.save_background()

    def clear_all(self):
        self.viewer.clear_all()


if __name__ == '__main__':
    main = tk.Tk()
    main.wm_title("Viewer example")
    m =Multiplot(main)
    m.pack(side="top", fill="both", expand="True")

    tk.mainloop()
