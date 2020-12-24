import tkinter as tk
import math
import sympy as sy
import numpy as np
import matplotlib
from matplotlib import style
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure



HEIGHT = 700
WIDTH = 1000


root = tk.Tk()
root.wm_title("Pharet")

tbdeg=tk.IntVar()
dtdeg=tk.IntVar()

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg='gray') 	#sets up the window size and color
canvas.pack()

frame1 = tk.Frame(root, bd=0.1)
frame1.place(relwidth=0.3, relheight=0.075, relx=0.05, rely=0.05)	#places a frame for other elements within the window

buttonsi = tk.Button(frame1, bg='#666666', text='Silicone', font=80)	#Creates the silicone button
buttonsi.place(relwidth=0.5, relheight=1)

buttondmnd = tk.Button(frame1, bg='#666666', text='Diamond', font=80)	#creates the diamond button(ADD MORE ENTRYS FOR t AND eV)
buttondmnd.place(relwidth=0.5, relheight=1, relx=0.5)



frameentry = tk.Frame(root, bd=0.1)
frameentry.place(relheight=0.4, relwidth=0.3, relx=0.05, rely=0.15)		#creates another frame for entrys

labelh = tk.Label(frameentry, bd=0.1, bg='#666666', text='h', font=80)	#label for variable 1
labelh.place(relheight=0.2, relwidth=0.4, anchor='nw')

entryh = tk.Entry(frameentry, bd=0.1, bg='#8c8c8c', font=80)	 	#entry for variable 1
entryh.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0)

labelk = tk.Label(frameentry, bd=0.1, bg='#666666', text='k', font=80) #label for variable 2
labelk.place(relheight=0.2, relwidth=0.4, rely=0.2, relx=0)

entryk = tk.Entry(frameentry, bd=0.1, bg='#8c8c8c', font=80)
entryk.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0.2)		#entry for variable 2

labell = tk.Label(frameentry, bd=0.1, bg='#666666', text='l', font=80) 	#label for variable 3
labell.place(relheight=0.2, relwidth=0.4, rely=0.4, relx=0)

entryl = tk.Entry(frameentry, bd=0.1, bg='#8c8c8c', font=80)
entryl.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0.4) 	#entry for variable 3

labelt = tk.Label(frameentry, bd=0.1, bg='#666666', text='t', font=80) 	
labelt.place(relheight=0.2, relwidth=0.4, rely=0.6, relx=0)

entryt = tk.Entry(frameentry, bd=0.1, bg='#8c8c8c', font=80)
entryt.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0.6) 

labeleV = tk.Label(frameentry, bd=0.1, bg='#666666', text='eV', font=80) 	
labeleV.place(relheight=0.2, relwidth=0.4, rely=0.8, relx=0)

entryeV = tk.Entry(frameentry, bd=0.1, bg='#8c8c8c', font=80)
entryeV.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0.8) 



frameres = tk.Frame(root, bd=0.1)
frameres.place(relheight= 0.37, relwidth=0.3, relx=0.05, rely=0.6)	#frame for results

labelres = tk.Label(frameres, bd=0.1, bg='#666666', text='Results', font=200) 	#title for results
labelres.place(relheight=0.2, relwidth=1)

labelang = tk.Label(frameres, bd=0.1, bg='#666666', text='Angle', font=200) 	#label for angle
labelang.place(relheight=0.33, relwidth=0.3, rely=0.2)

labelresang = tk.Label(frameres, bd=0.1, bg='#8c8c8c', textvariable=tbdeg, font=200) 		#angle text box
labelresang.place(relheight=0.33, relwidth=0.7, rely=0.2, relx=0.3)

labeloff = tk.Label(frameres, bd=0.1, bg='#666666', text='Offset', font=200) 	#label for offset
labeloff.place(relheight=0.34, relwidth=0.3, rely=0.45)

labelresoff = tk.Label(frameres, bd=0.1, bg='#8c8c8c', textvariable=dtdeg, font=200) 	#offset text box
labelresoff.place(relheight=0.34, relwidth=0.7, rely=0.45, relx=0.3)

labelp = tk.Label(frameres, bd=0.1, bg='#666666', text='Phase', font=200) 	#label for angle+offset
labelp.place(relheight=0.33, relwidth=0.3, rely=0.7)

labelresp = tk.Label(frameres, bd=0.1, bg='#8c8c8c', text="unset", font=200) 	#angle+offset text box
labelresp.place(relheight=0.33, relwidth=0.7, rely=0.7, relx=0.3)



framegraph1 = tk.Frame(root, bd=0.1)
framegraph1.place(relheight=0.4, relwidth=0.55, relx=0.41, rely=0.1) #example graph 2




framegraph2 = tk.Frame(root, bd=0.1)
framegraph2.place(relheight=0.4, relwidth=0.55, relx=0.41, rely=0.55) #example graph 1

fig = Figure(figsize=(5, 4), dpi=100)
t = np.arange(0, 3, .01)
fig.add_subplot(111).plot(t, 2 * np.sin(2 * np.pi * t))

canvasgraph2 = FigureCanvasTkAgg(fig, master=framegraph2)  # A tk.DrawingArea.
canvasgraph2.draw()
canvasgraph2.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)


def calculate():
	h=int(entryh.get())
	k=int(entryk.get())
	l=int(entryl.get())
	t=int(entryt.get())
	eV=int(entryeV.get())
	tm=t*10**4
	Re=2.81794*10**-5
	wavel=12398.506/eV

	#diamond specific variables
	x1=0.1250
	y1=0.1250
	z1=0.1250

	x2=0.8750
	y2=0.8750
	z2=0.8750

	x3=0.6250
	y3=0.6250
	z3=0.1250

	x4=0.3750
	y4=0.3750
	z4=0.8750

	x5=0.1250
	y5=0.6250
	z5=0.6250

	x6=0.8750
	y6=0.3750
	z6=0.3750

	x7=0.6250
	y7=0.1250
	z7=0.6250

	x8=0.3750
	y8=0.8750
	z8=0.3750

	adaim=3.567
	ddiam=3.567/(math.sqrt(h**2+k**2+l**2))
	Vdiam=3.567**3
	thetabdiam=math.asin(wavel/(2*ddiam))
	changethetadiam=0

	#fh summation
	pi = 3.141592653589793
	e = 2.7182818284590452
	s = 1/(2*ddiam)
	a = complex(0, 1)

	#Prt1 = (math.pi/2)*(((Re*(wavel)**2)/(math.pi*Vdiam))**2)
	#Prt2 = (tm*(math.sin(2*thetabdiam)))/(wavel*(math.sin(thetabdiam)*changethetadiam)) #change theta division by 0




	f0carbon=((2.31*e**(-20.844*s**2))+(1.02*e**(-10.208*s**2))+(1.589*e**(-0.569*s**2))+(0.865*e**(-51.651*s**2))+0.216)
	f0silicon=((6.292*e**(-2.439*s**2))+(3.035*e**(-32.334*s**2))+(1.989*e**(-0.678*s**2))+(1.541*e**(-81.694*s**2))+1.141)

	#print(f0silicon)
	#print(f0carbon)

	FminH = (f0carbon*e**(-2*pi*a*(h*x1+k*y1+l*z1)))+(f0carbon*e**(-2*pi*a*(h*x2+k*y2+l*z2)))+(f0carbon*e**(-2*pi*a*(h*x3+k*y3+l*z3)))+(f0carbon*e**(-2*pi*a*(h*x4+k*y4+l*z4)))+(f0carbon*e**(-2*pi*a*(h*x5+k*y5+l*z5)))+(f0carbon*e**(-2*pi*a*(h*x6+k*y6+l*z6)))+(f0carbon*e**(-2*pi*a*(h*x7+k*y7+l*z7)))+(f0carbon*e**(-2*pi*a*(h*x8+k*y8+l*z8)))
	FplusH = (f0carbon*e**(2*pi*a*(h*x1+k*y1+l*z1)))+(f0carbon*e**(2*pi*a*(h*x2+k*y2+l*z2)))+(f0carbon*e**(2*pi*a*(h*x3+k*y3+l*z3)))+(f0carbon*e**(2*pi*a*(h*x4+k*y4+l*z4)))+(f0carbon*e**(2*pi*a*(h*x5+k*y5+l*z5)))+(f0carbon*e**(2*pi*a*(h*x6+k*y6+l*z6)))+(f0carbon*e**(2*pi*a*(h*x7+k*y7+l*z7)))+(f0carbon*e**(2*pi*a*(h*x8+k*y8+l*z8)))

	FinFH = np.real(FminH*FplusH)

	#print(FinFH)
	#print(Prt1)
	#print(Prt2)

	#print(FinFH*Prt1)

	deltatheta = (tm*math.sin(2*thetabdiam)*(pi/2)*(((Re*wavel**2)/(pi*Vdiam))**2)*FinFH)/((pi/2)*math.sin(thetabdiam)*wavel)

	#print(deltatheta)

	deltathetadeg = (deltatheta/(2*pi))*360

	dtdeg.set(deltathetadeg)

	thetabdiamdeg = (thetabdiam/(2*pi))*360

	tbdeg.set(thetabdiamdeg)

	fig = Figure(figsize=(5, 4), dpi=100)
	xgraph = np.arange(5*10**-6, 1000*10**-6, .0001)
	fig.add_subplot(111).plot(xgraph, FinFH*(math.pi/2)*((Re*wavel**2)/(math.pi*Vdiam))**2*((tm*math.sin(2*thetabdiam))/(math.sin(thetabdiam))*t)) #should calculate the equation for all values of xgraph

	canvasgraph1 = FigureCanvasTkAgg(fig, master=framegraph1)  # A tk.DrawingArea.
	canvasgraph1.draw()
	canvasgraph1.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)



buttondmnd.config(command=calculate)

root.mainloop()