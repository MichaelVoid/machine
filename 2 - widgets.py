# -*- coding: utf-8 -*-
"""
Created on Tue Jan 30 14:13:38 2018
# how to make a frame
https://www.youtube.com/watch?v=RTM9tiV_HoY&index=2&list=PL6gx4Cwl9DGBwibXFtPtflztSNPGuIB_d
@author: mig
"""

import Tkinter as tk

root = tk.Tk()
topFrame = tk.Frame(root)
topFrame.pack()
bottomFrame = tk.Frame(root)
bottomFrame.pack(side="bottom")

button1 = tk.Button(topFrame,text="Button 1",fg="red")
button2 = tk.Button(topFrame,text="Button 2",fg="blue")
button3 = tk.Button(topFrame,text="Button 3",fg="green")
button4 = tk.Button(bottomFrame,text="Button 4",fg="purple")

button1.pack(side="top")
button2.pack(side="left")
button3.pack(side="right")
button4.pack(side="bottom")


root.mainloop()
