from tkinter import *




w = Tk()
w.geometry("300x100")
w.title('coucou')


labem = Label(w, text='veuillez entrer un nom', fg='black')
labem.pack(expand=YES)

nout = Entry(w)
nout.pack()
btn1 = 2

def prin():
    labem.configure(text=nout.get())
    btn.destroy()
    nout.destroy()
    btnback = Button(w, text='back', command=back)
    btnback.pack()
    btn2 = btn1 - 1
    print(btn2)
def destroy():
    w.destroy()
    nout.insert()



def back():
    label= Label(w, text='veuillez entrer un nom')
    label.place(x= 90, y=0)

    nat = Entry(w)
    nat.place(x= 90, y=20)
    btnback.destroy()

if btn1 ==1:
    btnback = Button(w, text='back', command=back)
    btnback.pack()
    print('ok')

btn_exit = Button(w, text='exit', command=destroy)
btn_exit.pack(expand=YES)
btn = Button(w, text='print', command=prin)
btn.pack(expand=YES)



w.mainloop()