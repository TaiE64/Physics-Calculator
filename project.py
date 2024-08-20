from tkinter import *
import re



#record number of clicks
clickNum=[]

cal = Tk()

# project heading
cal.title("Calculator")

# heading "calculator"
Label(cal, text="Physics Formula", height=3, font=('Helvetica', '25', 'bold')).place(x=580, y=10)

text_input = StringVar()
text_input.set("")
#for display 2
fomula_note=StringVar()
fomula_note.set("Calculator")
# display of calculator setting and position   2 is for formula (on the top)
def main():
    display = Entry(cal,highlightcolor='blue',relief=FLAT,highlightthickness=3, font=('Helvetica', '26', 'bold'),bd=5,textvariable=text_input)
    display2 = Message(cal,highlightcolor='blue',relief=FLAT,highlightthickness=3, font=('Helvetica', '15', 'bold'),bd=5,bg="lemon chiffon",textvariable=fomula_note,width=400)
    display.place(x=0, y=165,height=90,width=400)
    display2.place(x=0, y=10,height=150,width=400)


# screen size
cal.geometry("400x700")

#####################################################################################################################
# button setting
b7 = Button(cal, text=7, width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b8 = Button(cal, text=8, width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b9 = Button(cal, text=9, width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b4 = Button(cal, text=4, width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b5 = Button(cal, text=5, width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b6 = Button(cal, text=6, width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b1 = Button(cal, text=1, width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b2 = Button(cal, text=2, width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b3 = Button(cal, text=3, width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b_eq=Button(cal, text="=", width=7,font=("arial", 30,),bd=3,bg="DarkSeaGreen4",relief=FLAT)
b_clear=Button(cal, text="C", width=3, font=("arial", 30,),bd=3,bg="yellow green",relief=FLAT)
b_add=Button(cal, text="+", width=3, font=("arial", 30,),bd=3,bg="DarkSeaGreen4",relief=FLAT)
b_min=Button(cal, text="-", width=3, font=("arial", 30,),bd=3,bg="DarkSeaGreen4",relief=FLAT)
b_times=Button(cal, text="x", width=3, font=("arial", 30,),bd=3,bg="DarkSeaGreen4",relief=FLAT)
b_divide=Button(cal, text="÷", width=3, font=("arial", 30,),bd=3,bg="DarkSeaGreen4",relief=FLAT)
b_0=Button(cal, text="0", width=3, font=("arial", 30,),bd=3,bg="gainsboro",relief=FLAT)
b_dot=Button(cal, text=".", width=3, font=("arial", 30,),bd=3,bg="DarkSeaGreen4",relief=FLAT)
b_function=Button(cal, text="Phy", width=6, font=("arial", 30,),bd=3,bg="lemon chiffon",relief=FLAT)

#button for fomula
Emc2=Button(cal, text="E = mc²", width=7,font=("arial", 30,),bd=3,bg="lemon chiffon",relief=FLAT)
weight=Button(cal, text="W = mg", width=7,font=("arial", 30,),bd=3,bg="lemon chiffon",relief=FLAT)
r_force=Button(cal, text="F = ma", width=7,font=("arial", 30,),bd=3,bg="lemon chiffon",relief=FLAT)
density=Button(cal, text="P = m/v", width=7,font=("arial", 30,),bd=3,bg="lemon chiffon",relief=FLAT)
mgh=Button(cal, text="ΔE=mgΔh", width=7,font=("arial", 28,),bd=3,bg="lemon chiffon",relief=FLAT)
work=Button(cal, text="ΔW=FΔS", width=7,font=("arial", 30,),bd=3,bg="lemon chiffon",relief=FLAT)
power=Button(cal, text="P = W/t", width=7,font=("arial", 30,),bd=3,bg="lemon chiffon",relief=FLAT)
wave_v=Button(cal, text="V = fλ", width=7,font=("arial", 30,),bd=3,bg="lemon chiffon",relief=FLAT)



# position of buttons
b7.place(x=40, y=260)
b8.place(x=120, y=260)
b9.place(x=200, y=260)
b4.place(x=40, y=345)
b5.place(x=120, y=345)
b6.place(x=200, y=345)
b1.place(x=40, y=430)
b2.place(x=120, y=430)
b3.place(x=200, y=430)

b_eq.place(x=190,y=600)
b_clear.place(x=280,y=260)
b_add.place(x=280,y=345)
b_times.place(x=120,y=515)
b_divide.place(x=200,y=515)
b_min.place(x=280,y=430)
b_0.place(x=40,y=515)
b_dot.place(x=280,y=515)
b_function.place(x=40,y=600)

Emc2.place(x=550,y=150)
weight.place(x=550,y=250)
r_force.place(x=550,y=350)
density.place(x=550,y=450)
mgh.place(x=750,y=150)
work.place(x=750,y=250)
power.place(x=750,y=350)
wave_v.place(x=750,y=450)
#event for each button
##################################################################################################################

#get value and store it by get()
def inputNum(i):
    text_input.set(text_input.get()+i)
    return i

#for formula
def emc():
    note="E = mc²(Joules)\nc = 3x10^8 ms^-1\nInput a value for mass in kilogram(kg):"
    fomula_note.set(note)
    text_input.set('300000000**2')
    return note
def w():
    note="W = mg(Newton)\ng = 9.81 ms^-2\nInput a value for mass in kilogram(kg):"
    fomula_note.set(note)
    text_input.set('9.81*')
    return note
def F():
    note="F = ma(Newton)\na = Acceleration (ms^-2)\nm = mass (kg)\nInput values for mass in kilogram(kg) and acceleration in (ms^-2):"
    fomula_note.set(note)
    text_input.set("")
    return note
def P():
    note="P = m/v (kgm^-3)\nm = mass (kg)\nv = volume (m^3) \nInput values for mass in kilogram(kg) and volume in cubic metre(m^3):"
    fomula_note.set(note)
    text_input.set("")
    return note
def Eh():
    note="E = mgh(Joules)\ng = 9.81 ms^-2\nInput value for mass in kilogram(kg) and height in meters(m):"
    fomula_note.set(note)
    text_input.set('9.81*')
    return note
def wk():
    note="ΔW = FΔS(Joules)\nF = Force (ms^-2)\nΔS =Δdistance (m)\nInput values for foce in Newton(kgms^-2) and distance in meters(m):"
    fomula_note.set(note)
    text_input.set("")
    return note
def pw():
    note="P = W/t (Watt)\nW = work done (Joules)\nt = time (s)\nInput values for work done in Joules(J) and time in second(s):"
    fomula_note.set(note)
    text_input.set("")
    return note
def wv():
    note="V = fλ (speed)\nf = frequency (Hertz)\nλ = wavelength (m)\nInput values for fequency in Hertz(Hz) and wavelength in meters(m):"
    fomula_note.set("V = fλ (speed)\nf = frequency (Hertz)\nλ = wavelength (m)\nInput values for fequency in Hertz(Hz) and wavelength in meters(m):")
    text_input.set("")
    return note




#calculate value
def equal():
    any=text_input.get()
    if i:=re.findall("/0",any):
        text_input.set("Math Error")
    if len(any) != 0:
        num=eval(any)
        text_input.set(num)
    return any




#C
def clear():
    text_input.set('')
    fomula_note.set('Calculator')
    return ""
#use property of number(odd/even) to open or close extra phy window
def phy():
    total=sum(clickNum)
    if (total % 2)!=0:
        cal.geometry("1000x700")
    if (total % 2) == 0:
        cal.geometry("400x700")
    return total
def click():
    clickNum.append(1)
    phy()
    return "1"

b_0.config(command=lambda:inputNum("0"))
b7.config(command=lambda:inputNum("7"))
b8.config(command=lambda:inputNum("8"))
b9.config(command=lambda:inputNum("9"))
b4.config(command=lambda:inputNum("4"))
b5.config(command=lambda:inputNum("5"))
b6.config(command=lambda:inputNum("6"))
b1.config(command=lambda:inputNum("1"))
b2.config(command=lambda:inputNum("2"))
b3.config(command=lambda:inputNum("3"))
b_add.config(command=lambda:inputNum("+"))
b_times.config(command=lambda:inputNum("*"))
b_divide.config(command=lambda:inputNum("/"))
b_min.config(command=lambda:inputNum("-"))
b_dot.config(command=lambda:inputNum("."))


b_function.config(command=click)
Emc2.config(command=emc)
weight.config(command=w)
r_force.config(command=F)
density.config(command=P)
mgh.config(command=Eh)
work.config(command=wk)
power.config(command=pw)
wave_v.config(command=wv)


b_eq.config(command=equal)
b_clear.config(command=clear)

main()
cal.mainloop()
