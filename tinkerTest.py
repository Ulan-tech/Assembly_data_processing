import nfr as nfr

nfrRange = nfr.nfrRanges
def printTest():
    print(currentAssembly.get())
    print(currentnfr1.get())
    print(currentnfr2.get())
    print(currentnfr3.get())
    nfr1,nfr2,nfr3, info = nfr.infor_con(currentAssembly.get(), currentnfr1.get(), currentnfr2.get(), currentnfr3.get())
    lbl.config(text= f"Nfr1:{nfr1}\n Nfr2:{nfr2}\n Nfr3:{nfr3}\n info:{info}")





from tkinter import *
window=Tk()


currentnfr1 = StringVar()
currentnfr1.set(nfrRange[0])
currentnfr2 = StringVar()
currentnfr2.set(nfrRange[0])
currentnfr3 = StringVar()
currentnfr3.set(nfrRange[0])



lbl=Label(window, text="Assembly type", fg='red', font=("Helvetica", 16))
lbl.pack()
currentAssembly = StringVar()
currentAssembly.set(nfr.assemblyTypes[0])
assemblyDrop = OptionMenu(window, currentAssembly, *nfr.assemblyTypes)
assemblyDrop.pack()

lbl=Label(window, text="NFR1", fg='red', font=("Helvetica", 16))
lbl.pack()
nf1Drop = OptionMenu(window, currentnfr1, *nfrRange)
nf1Drop.pack()

lbl=Label(window, text="NFR2", fg='red', font=("Helvetica", 16))
lbl.pack()
nf1Drop = OptionMenu(window, currentnfr2, *nfrRange)
nf1Drop.pack()

lbl=Label(window, text="NFR3", fg='red', font=("Helvetica", 16))
lbl.pack()
nf1Drop = OptionMenu(window, currentnfr3, *nfrRange)
nf1Drop.pack()

btn=Button(window, text="Update", fg='blue', command=printTest)
btn.place(x=80, y=100)
lbl=Label(window, text="This is Label widget", fg='red', font=("Helvetica", 16))
lbl.pack()
# lbl.place(x=60, y=50)
txtfld=Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)
window.title('Hello Python')
window.geometry("800x500+10+10")
window.mainloop()

