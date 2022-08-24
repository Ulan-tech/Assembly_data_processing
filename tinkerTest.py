from tkinter import *
import nfr as nfr

nfrRange = nfr.nfrRanges

IMAGE_SIZE = 600

def updateImage(canvasWithItemconfig, imageFilename):
    uniformImage = PhotoImage(file=imageFilename)
    canvasWithItemconfig.itemconfig(canvasWithItemconfig.image_container, image=uniformImage)
    canvasWithItemconfig.image = uniformImage # create reference to prevent deletion.

def printTest():
    nfr1, nfr2, nfr3, info = nfr.infor_con(currentAssembly.get(), currentnfr1.get(), currentnfr2.get(),
                                           currentnfr3.get())
    lbl.config(text=f"Assembly Time:{round(nfr1,4)}\n Displacement Error:{round(nfr2,4)}\n "
                    f"Support Volume:{round(nfr3,4)}\n Information content:{round(info,4)}")
    nfr.uniform_distrb(currentnfr3.get(), currentAssembly.get())
    updateImage(unformCanvas, nfr.UNIFORM_GRAPH_FILENAME)
    nfr.gamma_distrb(currentnfr1.get(), currentAssembly.get())
    updateImage(gamma_Canvas, nfr.GAMMA_GRAPH_FILENAME)
    nfr.lognorm_distrb(currentnfr2.get(), currentAssembly.get())
    updateImage(log_Canvas, nfr.LOG_GRAPH_FILENAME)
    nfr.gamma_distrb(currentnfr3.get(), currentAssembly.get())



window = Tk()

currentnfr1 = StringVar()
currentnfr1.set(nfrRange[0])
currentnfr2 = StringVar()
currentnfr2.set(nfrRange[0])
currentnfr3 = StringVar()
currentnfr3.set(nfrRange[0])

lbl = Label(window, text="Assembly type", fg='black', font=("Helvetica", 16))
lbl.pack()
currentAssembly = StringVar()
currentAssembly.set(nfr.assemblyTypes[0])
assemblyDrop = OptionMenu(window, currentAssembly, *nfr.assemblyTypes)
assemblyDrop.pack()

lbl = Label(window, text="[nFR1]-Assembly time (s)", fg='black', font=("Helvetica", 16))
lbl.pack()
nf1Drop = OptionMenu(window, currentnfr1, *nfrRange)
nf1Drop.pack()

lbl = Label(window, text="[nFR2]-Displacement error (mm)", fg='black', font=("Helvetica", 16))
lbl.pack()
nf1Drop = OptionMenu(window, currentnfr2, *nfrRange)
nf1Drop.pack()

lbl = Label(window, text="[nFR3]-Support Volume (mm3)", fg='black', font=("Helvetica", 16))
lbl.pack()
nf1Drop = OptionMenu(window, currentnfr3, *nfrRange)
nf1Drop.pack()

btn = Button(window, text="Update", fg='blue', command=printTest)
btn.place(x=80, y=100)
lbl = Label(window, text="Results appear here", fg='red', font=("Helvetica", 16))
lbl.pack()

testImage = PhotoImage(file = "11.png")

gamma_Canvas= Canvas(window, width=IMAGE_SIZE, height= IMAGE_SIZE)
gamma_Canvas.place(x=0*IMAGE_SIZE, y=400)
gamma_Canvas.image_container =gamma_Canvas.create_image(0, 0, anchor="nw", image=testImage)

log_Canvas= Canvas(window, width=IMAGE_SIZE, height= IMAGE_SIZE)
log_Canvas.place(x=1*IMAGE_SIZE, y=400)
log_Canvas.image_container =log_Canvas.create_image(0, 0, anchor="nw", image=testImage)

unformCanvas= Canvas(window, width=IMAGE_SIZE, height= IMAGE_SIZE)
unformCanvas.place(x=2*IMAGE_SIZE, y=400)
unformCanvas.image_container =unformCanvas.create_image(0, 0, anchor="nw", image=testImage)


# lbl.place(x=60, y=50)
txtfld = Entry(window, text="This is Entry Widget", bd=5)
txtfld.place(x=80, y=150)
window.title('Hello Python')
window.geometry("1000x600+10+10")
window.mainloop()

