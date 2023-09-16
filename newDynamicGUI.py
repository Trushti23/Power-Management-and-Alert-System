from tkinter import *
from time import sleep
from PIL import ImageTk, Image
import socket


HOST = '192.168.79.126'
PORT = 5000


def blockSelect():
    global Avar, Bvar, Cvar, Dvar, Evar, Nvar

    def closeWin():
        global A_circle1, A_circle2, B_circle1, B_circle2, C_circle1, C_circle2, D_circle1, D_circle2, E_circle1, E_circle2, N_circle1, N_circle2

        blockSelectWin.destroy()
        if Avar.get() == 1:
            A_label_A1 = Label(Aframe, text="UPS:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            A_label_A1.grid(row=0, column=0)

            A_label_A2 = Label(Aframe, text="A Main:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            A_label_A2.grid(row=1, column=0)

            A_canvas1 = Canvas(Aframe, height=20, width=20, bg='black')
            A_canvas1.grid(row=0, column=1, sticky='W')
            A_circle1 = A_canvas1.create_oval(0, 0, 20, 20, fill='blue')

            A_canvas2 = Canvas(Aframe, height=20, width=20, bg='black')
            A_canvas2.grid(row=1, column=1, sticky='W')
            A_circle2 = A_canvas2.create_oval(0, 0, 20, 20, fill='blue')
        elif Avar.get() == 0:
            for widgets in Aframe.winfo_children():
                widgets.grid_forget()

        if Bvar.get() == 1:
            B_label_A1 = Label(Bframe, text="UPS:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            B_label_A1.grid(row=0, column=0)

            B_label_A2 = Label(Bframe, text="B Main:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            B_label_A2.grid(row=1, column=0)

            B_canvas1 = Canvas(Bframe, height=20, width=20, bg='black')
            B_canvas1.grid(row=0, column=1, sticky='W')
            B_circle1 = B_canvas1.create_oval(0, 0, 20, 20, fill='blue')

            B_canvas2 = Canvas(Bframe, height=20, width=20, bg='black')
            B_canvas2.grid(row=1, column=1, sticky='W')
            B_circle2 = B_canvas2.create_oval(0, 0, 20, 20, fill='blue')
        else:
            for widgets in Bframe.winfo_children():
                widgets.grid_forget()

        if Cvar.get() == 1:
            C_label_A1 = Label(Cframe, text="UPS:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            C_label_A1.grid(row=0, column=0)

            C_label_A2 = Label(Cframe, text="B Main:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            C_label_A2.grid(row=1, column=0)

            C_canvas1 = Canvas(Cframe, height=20, width=20, bg='black')
            C_canvas1.grid(row=0, column=1, sticky='W')
            C_circle1 = C_canvas1.create_oval(0, 0, 20, 20, fill='blue')

            C_canvas2 = Canvas(Cframe, height=20, width=20, bg='black')
            C_canvas2.grid(row=1, column=1, sticky='W')
            C_circle2 = C_canvas2.create_oval(0, 0, 20, 20, fill='blue')
        else:
            for widgets in Cframe.winfo_children():
                widgets.grid_forget()

        if Dvar.get() == 1:

            D_label_A1 = Label(Dframe, text="UPS:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            D_label_A1.grid(row=0, column=0)

            D_label_A2 = Label(Dframe, text="D Main:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            D_label_A2.grid(row=1, column=0)

            D_canvas1 = Canvas(Dframe, height=20, width=20, bg='black')
            D_canvas1.grid(row=0, column=1, sticky='W')
            D_circle1 = D_canvas1.create_oval(0, 0, 20, 20, fill='blue')

            D_canvas2 = Canvas(Dframe, height=20, width=20, bg='black')
            D_canvas2.grid(row=1, column=1, sticky='W')
            D_circle2 = D_canvas2.create_oval(0, 0, 20, 20, fill='blue')
        else:
            for widgets in Dframe.winfo_children():
                widgets.grid_forget()

        if Evar.get() == 1:

            E_label_A1 = Label(Eframe, text="UPS:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            E_label_A1.grid(row=0, column=0)

            E_label_A2 = Label(Eframe, text="E Main:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            E_label_A2.grid(row=1, column=0)

            E_canvas1 = Canvas(Eframe, height=20, width=20, bg='black')
            E_canvas1.grid(row=0, column=1, sticky='W')
            E_circle1 = E_canvas1.create_oval(0, 0, 20, 20, fill='blue')

            E_canvas2 = Canvas(Eframe, height=20, width=20, bg='black')
            E_canvas2.grid(row=1, column=1, sticky='W')
            E_circle2 = E_canvas2.create_oval(0, 0, 20, 20, fill='blue')
        else:
            for widgets in Eframe.winfo_children():
                widgets.grid_forget()

        if Nvar.get() == 1:

            N_label_A1 = Label(Nframe, text="UPS:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            N_label_A1.grid(row=0, column=0)

            N_label_A2 = Label(Nframe, text="N Main:",
                               font=("Montserrat", 10), padx=0, pady=0, fg="white", bg="black")
            N_label_A2.grid(row=1, column=0)

            N_canvas1 = Canvas(Nframe, height=20, width=20, bg='black')
            N_canvas1.grid(row=0, column=1, sticky='W')
            N_circle1 = N_canvas1.create_oval(0, 0, 20, 20, fill='blue')

            N_canvas2 = Canvas(Nframe, height=20, width=20, bg='black')
            N_canvas2.grid(row=1, column=1, sticky='W')
            N_circle2 = N_canvas2.create_oval(0, 0, 20, 20, fill='blue')
        else:
            for widgets in Nframe.winfo_children():
                widgets.grid_forget()

    blockSelectWin = Toplevel(root)
    blockSelectWin.title("Block Select")
    blockSelectWin.geometry("200x200")

    frame1 = LabelFrame(blockSelectWin)
    frame1.grid(row=0, column=0, padx=5, pady=5)

    aButton = Checkbutton(frame1, text="A Block", variable=Avar)
    bButton = Checkbutton(frame1, text="B Block", variable=Bvar)
    cButton = Checkbutton(frame1, text="C Block", variable=Cvar)
    dButton = Checkbutton(frame1, text="D Block", variable=Dvar)
    eButton = Checkbutton(frame1, text="E Block", variable=Evar)
    nButton = Checkbutton(frame1, text="N Block", variable=Nvar)

    aButton.grid(row=0, column=0)
    bButton.grid(row=1, column=0)
    cButton.grid(row=2, column=0)
    dButton.grid(row=3, column=0)
    eButton.grid(row=4, column=0)
    nButton.grid(row=5, column=0)

    lockButton = Button(frame1, text="Confirm", padx=5, pady=5,
                        command=lambda: closeWin(), bg="#3FC1C9", fg="#F5F5F5")
    lockButton.grid(row=6, column=0)


root = Tk()
root.title("Embedded System Special Assignment")
root.geometry("700x750")

ButtonFrame = LabelFrame(root)
MapFrame = LabelFrame(root)

ButtonFrame.grid(row=0, column=0, sticky=W, padx=5, pady=5)
MapFrame.grid(row=1, column=0, padx=5, pady=5, sticky=N)

Avar = IntVar()
Bvar = IntVar()
Cvar = IntVar()
Dvar = IntVar()
Evar = IntVar()
Nvar = IntVar()

Avar.set(1)
Bvar.set(1)
Cvar.set(1)
Dvar.set(1)
Evar.set(1)
Nvar.set(1)


A_circle1, A_circle2, B_circle1, B_circle2, C_circle1, C_circle2, D_circle1, D_circle2, E_circle1, E_circle2, N_circle1, N_circle2 = None, None, None, None, None, None, None, None, None, None, None, None

bgimage = Image.open("map.jpg")
bgimage = bgimage.resize((700, 700))
bgimage = ImageTk.PhotoImage(bgimage)
imagelabel = Label(root, image=bgimage)
imagelabel.place(x=5, y=50)

# Adding Frames
Aframe = LabelFrame(root)
Aframe.place(x=123+5, y=218+50)
Bframe = LabelFrame(root)
Bframe.place(x=240+5, y=218+50)
Cframe = LabelFrame(root)
Cframe.place(x=123+5, y=350+50)
Dframe = LabelFrame(root)
Dframe.place(x=240+5, y=350+50)
Eframe = LabelFrame(root)
Eframe.place(x=413+5, y=220+50)
Nframe = LabelFrame(root)
Nframe.place(x=353+5, y=302+50)


with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print('Connected by', addr)
        data = conn.recv(1024).decode('utf-8')
        if data is not None:
            print(data)


blockButton = Button(ButtonFrame, text="Edit Blocks", padx=20, pady=2,
                     command=lambda: blockSelect(), bg="#3FC1C9", fg="#F5F5F5")
blockButton.grid(row=1, column=0, sticky=NW)

root.mainloop()
