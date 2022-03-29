import tkinter as tk
from tkinter import *
import tkinter.messagebox
import math
import sympy as sy
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


root = tk.Tk()
root.wm_title("Pharet")
root.geometry("700x450")

size=80

def resize(e):
	# Grab the app width and height
	size = (root.winfo_width()+root.winfo_height())/100
	# Change our text size
	buttonsi.config(font=("Helvetica", int(size)))
	buttondmnd.config(font=("Helvetica", int(size)))
	buttongr.config(font=("Helvetica", int(size)))
	buttonpr.config(font=("Helvetica", int(size)))
	labelh.config(font=("Helvetica", int(size)))
	entryh.config(font=("Helvetica", int(size)))
	labelk.config(font=("Helvetica", int(size)))
	entryk.config(font=("Helvetica", int(size)))	
	labell.config(font=("Helvetica", int(size)))
	entryl.config(font=("Helvetica", int(size)))
	labelt.config(font=("Helvetica", int(size)))
	entryt.config(font=("Helvetica", int(size)))
	labeleV.config(font=("Helvetica", int(size)))
	entryeV.config(font=("Helvetica", int(size)))
	labelres.config(font=("Helvetica", int(size)))
	labelres1.config(font=("Helvetica", int(size)))
	labelang.config(font=("Helvetica", int(size)))
	labelresang.config(font=("Helvetica", int(size)))
	labeloff.config(font=("Helvetica", int(size)))
	labelresoff.config(font=("Helvetica", int(size)))

root.bind('<Configure>',resize)

tbdeg=tk.IntVar()
dtdeg=tk.IntVar()
lensType=tk.StringVar()

canvas = tk.Canvas(root, bg='#b49e83') 	#sets up the window size and color
canvas.place(relwidth=1, relheight=1, relx=0, rely=0)

frame1 = tk.Frame(root, bd=0.1)
frame1.place(relwidth=0.3, relheight=0.12, relx=0.05, rely=0.075)	#places a frame for other elements within the window

buttonsi = tk.Button(frame1, bg='#848482', text='Silicon')	#Creates the silicone button
buttonsi.place(relwidth=0.5, relheight=1)

buttondmnd = tk.Button(frame1, bg='#848482', text='Diamond')	#creates the diamond button(ADD MORE ENTRYS FOR t AND eV)
buttondmnd.place(relwidth=0.5, relheight=1, relx=0.5)

framegrpr = tk.Frame(root, bd=0.1)
framegrpr.place(relwidth=0.4, relheight=0.12, relx=0.5, rely=0.555)

buttongr = tk.Button(framegrpr, bg='#696969', text='Graph')	#Creates the silicone button
buttongr.place(relwidth=0.5, relheight=1)

buttonpr = tk.Button(framegrpr, bg='#696969', text='Print')	#creates the diamond button(ADD MORE ENTRYS FOR t AND eV)
buttonpr.place(relwidth=0.5, relheight=1, relx=0.5)


frameentry = tk.Frame(root, bd=0.1)
frameentry.place(relheight=0.6, relwidth=0.3, relx=0.05, rely=0.25)		#creates another frame for entrys

labelh = tk.Label(frameentry, bd=0.1, bg='#4f7171', text='h:')	#label for variable 1
labelh.place(relheight=0.2, relwidth=0.4, anchor='nw')

entryh = tk.Entry(frameentry, bd=0.1, bg='#759696')	 	#entry for variable 1
entryh.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0)

labelk = tk.Label(frameentry, bd=0.1, bg='#696969', text='k:') #label for variable 2
labelk.place(relheight=0.2, relwidth=0.4, rely=0.2, relx=0)

entryk = tk.Entry(frameentry, bd=0.1, bg='#848482')
entryk.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0.2)		#entry for variable 2

labell = tk.Label(frameentry, bd=0.1, bg='#4f7171', text='l:') 	#label for variable 3
labell.place(relheight=0.2, relwidth=0.4, rely=0.4, relx=0)

entryl = tk.Entry(frameentry, bd=0.1, bg='#759696')
entryl.place(relheight=0.2, relwidth=0.6, relx=0.4, rely=0.4) 	#entry for variable 3

labelt = tk.Label(frameentry, bd=0.1, bg='#696969', text='thickness(μm):') 	
labelt.place(relheight=0.2, relwidth=0.5, rely=0.6, relx=0)

entryt = tk.Entry(frameentry, bd=0.1, bg='#848482')
entryt.place(relheight=0.2, relwidth=0.5, relx=0.5, rely=0.6) 

labeleV = tk.Label(frameentry, bd=0.1, bg='#4f7171', text='energy(eV):') 	
labeleV.place(relheight=0.2, relwidth=0.5, rely=0.8, relx=0)

entryeV = tk.Entry(frameentry, bd=0.1, bg='#759696')
entryeV.place(relheight=0.2, relwidth=0.5, relx=0.5, rely=0.8) 



frameres = tk.Frame(root, bd=0.1)
frameres.place(relheight= 0.4, relwidth=0.4, relx=0.5, rely=0.1)	#frame for results

labelres1 = tk.Label(frameres, bd=0.1, bg='#696969', text='Results for Crystal Type:') 	#title for results
labelres1.place(relheight=0.15, relwidth=1)

labelres = tk.Label(frameres, bd=0.1, bg='#696969', textvariable=lensType) 	#title for results
labelres.place(relheight=0.15, relwidth=1, rely=0.15)

labelang = tk.Label(frameres, bd=0.1, bg='#4f7171', text='Bragg Angle') 	#label for angle
labelang.place(relheight=0.35, relwidth=0.5, rely=0.3)

labelresang = tk.Label(frameres, bd=0.1, bg='#759696', textvariable=tbdeg) 		#angle text box
labelresang.place(relheight=0.35, relwidth=0.5, rely=0.3, relx=0.5)

labeloff = tk.Label(frameres, bd=0.1, bg='#696969', text='Offset (Pc=1)') 	#label for offset
labeloff.place(relheight=0.35, relwidth=0.5, rely=0.65)

labelresoff = tk.Label(frameres, bd=0.1, bg='#848482', textvariable=dtdeg) 	#offset text box
labelresoff.place(relheight=0.35, relwidth=0.5, rely=0.65, relx=0.5)

ident=0

deltathetadeg=0
thetabdiamdeg=0
thetabsildeg=0

h=0
k=0
l=0
t=0
eV=0
#coordinate arrays
arrx=[]
arry=[]
arrsin=[]

#diamond and silicone specific variable arrays
xarr = [0.1250, 0.8750, 0.6250, 0.3750, 0.1250, 0.8750, 0.6250, 0.3750]
yarr = [0.1250, 0.8750, 0.6250, 0.3750, 0.6250, 0.3750, 0.1250, 0.8750]
zarr = [0.1250, 0.8750, 0.1250, 0.8750, 0.6250, 0.3750, 0.6250, 0.3750]

def truncate(number, decimals):
    """
    Returns a value truncated to a specific number of decimal places.
    """
    factor = 10.0 ** decimals
    return math.trunc(number * factor) / factor


def calcdiam():

	try:
		buttondmnd.configure(bg="#759696")
		buttonsi.configure(bg="#848482")

		lensType.set('Diamond')

		global ident
		ident=1

		h=int(entryh.get())
		k=int(entryk.get())
		l=int(entryl.get())
		t=int(entryt.get())
		eV=int(entryeV.get())
		tm=t*10**4
		Re=2.81794*10**-5
		wavel=12398.506/eV

		ddiam=3.567/(math.sqrt(h**2+k**2+l**2))
		Vdiam=3.567**3
		thetabdiam=math.asin(wavel/(2*ddiam))
		changethetadiam=0

		#fh summation
		pi = 3.141592653589793
		e = 2.7182818284590452
		s = 1/(2*ddiam)
		a = complex(0, 1)

		f0carbon=((2.31*e**(-20.844*s**2))+(1.02*e**(-10.208*s**2))+(1.589*e**(-0.569*s**2))+(0.865*e**(-51.651*s**2))+0.216)

		FminH = 0
		FplusH = 0

		for i in range(8):
			FminH += f0carbon*e**(-2*pi*a*(h*xarr[i]+k*yarr[i]+l*zarr[i]))
			FplusH += f0carbon*e**(2*pi*a*(h*xarr[i]+k*yarr[i]+l*zarr[i]))


		FinFH = np.real(FminH*FplusH)

		deltatheta = (tm*math.sin(2*thetabdiam)*(pi/2)*(((Re*wavel**2)/(pi*Vdiam))**2)*FinFH)/((pi/2)*math.sin(thetabdiam)*wavel)

		global deltathetadeg
		global thetabdiamdeg

		deltathetadeg = (deltatheta/(2*pi))*360

		dtdeg.set(truncate(deltathetadeg,6))

		thetabdiamdeg = (thetabdiam/(2*pi))*360

		tbdeg.set(truncate(thetabdiamdeg,6))

	
		global arrx
		global arry
		global arrsin
		arrx=[]
		arry=[]
		arrsin=[]
		g=1
		whiletemp=0
		while(g<=200):
			arrx.append(whiletemp*(180/pi))
			whiletemp=g*5*10**-6
			arry.append(FinFH*((Re*wavel**2)/(pi*Vdiam))**2*((tm*math.sin(2*thetabdiam))/(wavel*math.sin(thetabdiam)*whiletemp)))
			arrsin.append(math.sin((pi/2)*arry[g-1]))
			g=g+1
	except Exception:
		tkinter.messagebox.showinfo('Error','You have entered an invalid value')


def calcsi():

	try:
		buttondmnd.configure(bg="#848482")
		buttonsi.configure(bg="#759696")

		lensType.set('Silicon')

		global ident
		ident=2

		h=int(entryh.get())
		k=int(entryk.get())
		l=int(entryl.get())
		t=int(entryt.get())
		eV=int(entryeV.get())
		tm=t*10**4
		Re=2.81794*10**-5
		wavel=12398.506/eV

		dsil=5.43/(math.sqrt(h**2+k**2+l**2))
		Vsil=5.43**3
		thetabsil=math.asin(wavel/(2*dsil))

		#fh summation
		pi = 3.141592653589793
		e = 2.7182818284590452
		s = 1/(2*dsil)
		a = complex(0, 1)

		f0silicon=((6.292*e**(-2.439*s**2))+(3.035*e**(-32.334*s**2))+(1.989*e**(-0.678*s**2))+(1.541*e**(-81.694*s**2))+1.141)

		FminH = 0
		FplusH = 0

		for i in range(8):
			FminH += f0silicon*e**(-2*pi*a*(h*xarr[i]+k*yarr[i]+l*zarr[i]))
			FplusH += f0silicon*e**(2*pi*a*(h*xarr[i]+k*yarr[i]+l*zarr[i]))

		FinFH = np.real(FminH*FplusH)

		deltatheta = (tm*math.sin(2*thetabsil)*(pi/2)*(((Re*wavel**2)/(pi*Vsil))**2)*FinFH)/((pi/2)*math.sin(thetabsil)*wavel)

		global deltathetadeg
		global thetabsildeg

		deltathetadeg = (deltatheta/(2*pi))*360

		dtdeg.set(truncate(deltathetadeg,6))

		thetabsildeg = (thetabsil/(2*pi))*360

		tbdeg.set(truncate(thetabsildeg,6))

		#while loop creates arrays of x and y coords of graph
		global arrx
		global arry
		global arrsin
		arrx=[]
		arry=[]
		arrsin=[]
		g=1
		whiletemp=0
		while(g<=200):
			arrx.append(whiletemp*(180/pi))
			whiletemp=g*5*10**-6
			arry.append(FinFH*((Re*wavel**2)/(pi*Vsil))**2*((tm*math.sin(2*thetabsil))/(wavel*math.sin(thetabsil)*whiletemp)))
			arrsin.append(math.sin((pi/2)*arry[g-1]))
			g=g+1
	except Exception:
		tkinter.messagebox.showinfo('Error','You have entered an invalid value')


def genGraph():

	fig , ax = plt.subplots(nrows = 2, ncols = 1, figsize=(8,6))
 
	#Plotting on the 1st axes
	ax[0].set_ylim([0,2])
	ax[0].set_xlabel('Offset(degrees)')
	ax[0].set_ylabel('Phase(pi/2)')
	ax[0].plot(arrx,arry, color = 'blue')
 
	#Plotting on the last axes
	ax[1].set_xlabel('Offset(degrees)')
	ax[1].set_ylabel('Sin(phase)')
	ax[1].plot(arrx,arrsin , color = 'orange')
	plt.show()

forcount=0
def genTXT():

	tkinter.messagebox.showinfo('Print Alert','Your results have been printed to the file PHAREToutput.txt in the same directory as the program. Move or change the name of the file if you do not want it to be overwritten by the next print.')

	global forcount
	forcount=0
	bang=0
	if(ident==1):
		bang=thetabdiamdeg

	if(ident==2):
		bang=thetabsildeg

	with open("PHAREToutput.txt","w") as f:
		f.write("#Output for h="+str(h)+" k="+str(k)+" l="+str(l)+" t(microns)="+str(t)+" eV="+str(eV)+'\n')
		if(ident==1):
			f.write("#Crystal Type: Diamond"+'\n')
		if(ident==2):
			f.write("#Crystal Type: Silicon"+'\n')
		f.write("#Bragg Angle(degrees)="+str(truncate(bang,6))+'\n')
		f.write("#Offset(degrees)="+str(truncate(deltathetadeg,6))+'\n')
		f.write("#Offset(degrees)   Phase(pi/2) 	 Sin(phase)"+'\n')
		for x in arrx:
			f.write(str(truncate(x,6))+"     "+str(truncate(arry[forcount],6))+"      "+str(truncate(arrsin[forcount],6))+'\n')
			forcount=forcount+1
		f.write('\n')
		f.write("#Credits to Lucas Ancieta and Dr.Daniel Haskel")



buttonpr.config(command=genTXT)
buttongr.config(command=genGraph)
buttonsi.config(command=calcsi)
buttondmnd.config(command=calcdiam)




	




root.mainloop()

#Credits to Lucas Ancieta and Dr.Daniel Haskell