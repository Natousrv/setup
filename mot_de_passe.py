#import
from tkinter import * #import de la fenetre
import string
from random import randint, choice #import de nombre random
from time import strftime #import du temps
import requests
import subprocess

#import du theme foncer
def create():
    window = Toplevel(root)
    window.title("generateur de mot de passe")
    window.geometry("1280x720")
    window.minsize(1200, 620)
    window.maxsize(4080, 1060)
    window.iconbitmap(bitmap=("icon.ico"))
    window.config(bg='#262626')

    # Create a transparent window
    window.wm_attributes('-transparentcolor', '#add123')

    # crée frame
    frame = Frame(window, bg='#262626', border=0, borderwidth=0)

    # crée un sous boite
    right_frame = Frame(frame, bg='#262626', border=0, borderwidth=0)

    right_frame2 = Frame(frame, bg='#262626')

    def chose():
        button1 = choix1.get()
        button2 = choix2.get()
        button3 = choix3.get()
        if str(button1 and button2 and button3) == '1':
            print(generate_password7() in password_entry)
        if str(button2 and button3) == '1':
            print(generate_password6() in password_entry)
        if str(button1 and button3) == '1':
            print(generate_password5() in password_entry)
        if str(button1 and button2) == '1':
            print(generate_password4() in password_entry)
        if str(button1) == '1':
            print(generate_password1() in password_entry)
        if str(button2) == '1':
            print(generate_password2() in password_entry)
        if str(button3) == '1':
            print(generate_password3() in password_entry)

    def generate_password1():
        password_min = 12
        password_max = 24
        all_chars = string.ascii_letters

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password2():
        password_min = 12
        password_max = 24
        all_chars = string.punctuation

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password3():
        password_min = 12
        password_max = 24
        all_chars = string.digits

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password4():
        password_min = 12
        password_max = 24
        all_chars = string.punctuation + string.ascii_letters

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password5():
        password_min = 12
        password_max = 24
        all_chars = string.ascii_letters + string.digits

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password6():
        password_min = 12
        password_max = 24
        all_chars = string.punctuation + string.digits

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password7():
        password_min = 12
        password_max = 24
        all_chars = string.punctuation + string.digits + string.ascii_letters

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    global choix1
    global choix2
    global choix3
    choix1 = IntVar()
    choix2 = IntVar()
    choix3 = IntVar()
    g = 1
    f = 2
    h = 3
    result = f + g
    result1 = f + g + h

    # crée un sous boite
    right_frame = Frame(frame, bg='#262626')

    right_frame2 = Frame(frame, bg='#262626')
    # crée un titre

    lable_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 35), bg='#262626', fg='white')
    lable_title.pack(expand=YES)

    def destroye():
        password_entry.destroy(string.punctuation)

    def copier():
        window.clipboard_append(password_entry.get())

    copybtn = PhotoImage(file='copy.png')
    bt_copie = Button(window, image=copybtn, text="copier", command=copier, relief=FLAT, bg='#262626', activebackground='#ffffff', borderwidth=0, border=0)
    bt_copie.place(x=1055, y=300)

    # crée un champs
    password_entry = Entry(right_frame, width=30, font=("Helvetica", 35), bg='#262626', fg='white', relief=GROOVE,
                           borderwidth=1, highlightthickness=0)
    password_entry.pack(expand=YES)

    # crée button a cocher
    checkbutton_soleil = Checkbutton(right_frame, text="mot de passe avec des lettre ", font=("Helvetica", 20), selectcolor='black',
                                     bg='#262626', fg='#ffffff', activebackground='white', variable=choix1)
    checkbutton_soleil.pack()
    checkbutton_pluie = Checkbutton(right_frame, text="mot de passe avec des carctere spéciaux", font=("Helvetica", 20), selectcolor='black',
                                    fg='white', bg='#262626', variable=choix2)
    checkbutton_pluie.pack()
    checkbutton_moyen = Checkbutton(right_frame, text="mot de passe avec des chiffres", font=("Helvetica", 20), selectcolor='black',
                                    fg='white', bg='#262626', variable=choix3)
    checkbutton_moyen.pack()
    g = 1
    f = 2
    result = g + f

    # crée un boutton
    generate_password_button = Button(right_frame, text="Générer un mot de passe",
                                      font=("Helvetica", 20), bg='#262626', fg='white', relief=GROOVE, borderwidth=2,
                                      border=2, command=chose)
    generate_password_button.pack(expand=YES)

    # on place la sous boite a droite de la frame principal
    right_frame.grid(row=0, column=1, sticky=W)

    right_frame2.grid(row=1, column=1, sticky=W)
    # afficher frame
    frame.pack(expand=YES)

    def exit():
        window.destroy()


    exitbtn = PhotoImage(file='exit.png')

    button_exit = Button(window, image=exitbtn, bg='#262626', relief=FLAT, activebackground='#ffffff',
                         highlightthickness=0, command=exit)
    button_exit.place(x=1180, y=620)

    button_set = Button(window, text="setting", bg='#262626', relief=FLAT, activebackground='white',
                         highlightthickness=0, command=setting)
    button_set.place(x=0, y=0)


    # afficher la fentre
    window.overrideredirect(2)

    window.wm_attributes('-transparentcolor', '#963963')

    def time():
        string = strftime('%H:%M:%S %p')
        label.config(text=string)
        label.after(1000, time)

    label = Label(window, font=('arial', 50), foreground='red', bg='#262626')
    label.place(x=480, y=0)
    time()

    window.mainloop()


#import de theme claire

def wind():
    window = Toplevel(root)
    window.title("generateur de mot de passe")
    window.geometry("1280x720")
    window.minsize(1200, 620)
    window.maxsize(4080, 1060)
    window.iconbitmap(bitmap=("icon.ico"))
    window.config(bg='#989898')

    # Create a transparent window
    window.wm_attributes('-transparentcolor', '#add123')

    # crée frame
    frame = Frame(window, bg='#989898', border=0, borderwidth=0)

    # crée un sous boite
    right_frame = Frame(frame, bg='#989898', border=0, borderwidth=0)

    right_frame2 = Frame(frame, bg='#989898')

    def chose():
        button1 = choix1.get()
        button2 = choix2.get()
        button3 = choix3.get()
        if str(button1 and button2 and button3) == '1':
            print(generate_password7() in password_entry)
        if str(button2 and button3) == '1':
            print(generate_password6() in password_entry)
        if str(button1 and button3) == '1':
            print(generate_password5() in password_entry)
        if str(button1 and button2) == '1':
            print(generate_password4() in password_entry)
        if str(button1) == '1':
            print(generate_password1() in password_entry)
        if str(button2) == '1':
            print(generate_password2() in password_entry)
        if str(button3) == '1':
            print(generate_password3() in password_entry)

    def generate_password1():
        password_min = 12
        password_max = 24
        all_chars = string.ascii_letters

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password2():
        password_min = 12
        password_max = 24
        all_chars = string.punctuation

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password3():
        password_min = 12
        password_max = 24
        all_chars = string.digits

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password4():
        password_min = 12
        password_max = 24
        all_chars = string.punctuation + string.ascii_letters

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password5():
        password_min = 12
        password_max = 24
        all_chars = string.ascii_letters + string.digits

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password6():
        password_min = 12
        password_max = 24
        all_chars = string.punctuation + string.digits

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    def generate_password7():
        password_min = 12
        password_max = 24
        all_chars = string.punctuation + string.digits + string.ascii_letters

        password = "".join(choice(all_chars) for x in range(randint(password_min, password_max)))
        password_entry.delete(0, END)
        password_entry.insert(0, password)

    global choix1
    global choix2
    global choix3
    choix1 = IntVar()
    choix2 = IntVar()
    choix3 = IntVar()
    g = 1
    f = 2
    h = 3
    result = f + g
    result1 = f + g + h

    # crée un sous boite
    right_frame = Frame(frame, bg='#989898')

    right_frame2 = Frame(frame, bg='#989898')
    # crée un titre

    lable_title = Label(right_frame, text="Mot de passe", font=("Helvetica", 35), bg='#989898', fg='black')
    lable_title.pack(expand=YES)

    def destroye():
        password_entry.destroy(string.punctuation)

    def copier():
        window.clipboard_append(password_entry.get())

    copybtn = PhotoImage(file='copy.png')
    bt_copie = Button(window, image=copybtn, text="copier", command=copier, relief=FLAT, bg='#989898', activebackground='black', borderwidth=0, border=0)
    bt_copie.place(x=1055, y=300)

    # crée un champs
    password_entry = Entry(right_frame, width=30, font=("Helvetica", 35), bg='#989898', fg='black', relief=GROOVE,
                           borderwidth=1, highlightthickness=0)
    password_entry.pack(expand=YES)

    # crée button a cocher
    checkbutton_soleil = Checkbutton(right_frame, text="mot de passe avec des lettre ", font=("Helvetica", 20), selectcolor='#989898',
                                     bg='#989898', fg='black', variable=choix1)
    checkbutton_soleil.pack()
    checkbutton_pluie = Checkbutton(right_frame, text="mot de passe avec des carctere spéciaux", font=("Helvetica", 20), selectcolor='#989898',
                                    fg='black', bg='#989898', variable=choix2)
    checkbutton_pluie.pack()
    checkbutton_moyen = Checkbutton(right_frame, text="mot de passe avec des chiffres", font=("Helvetica", 20), selectcolor='#989898',
                                    fg='black', bg='#989898', variable=choix3)
    checkbutton_moyen.pack()
    g = 1
    f = 2
    result = g + f

    # crée un boutton
    generate_password_button = Button(right_frame, text="Générer un mot de passe",
                                      font=("Helvetica", 20), bg='#989898', fg='black', relief=GROOVE, borderwidth=2,
                                      border=2, command=chose)
    generate_password_button.pack(expand=YES)

    # on place la sous boite a droite de la frame principal
    right_frame.grid(row=0, column=1, sticky=W)

    right_frame2.grid(row=1, column=1, sticky=W)
    # afficher frame
    frame.pack(expand=YES)

    def exit():
        window.destroy()


    exitbtn = PhotoImage(file='exit.png')

    button_exit = Button(window, image=exitbtn, bg='#989898', relief=FLAT, activebackground='black',
                         highlightthickness=0, command=exit)
    button_exit.place(x=1180, y=620)


    button_set = Button(window, text="setting", bg='#989898', relief=FLAT, activebackground='black', highlightthickness=0, command=setting)
    button_set.place(x=0, y=0)
    if button_set =='1':
        print('coucou')

    # afficher la fentre
    window.overrideredirect(2)

    window.wm_attributes('-transparentcolor', '#963963')

    def time():
        string = strftime('%H:%M:%S %p')
        label.config(text=string)
        label.after(1000, time)

    label = Label(window, font=('arial', 50), foreground='red', bg='#989898')
    label.place(x=480, y=0)
    time()

    window.mainloop()


def setting():
    window = Toplevel(root)
    window.title("generateur de mot de passe")
    window.geometry("1280x720")
    window.minsize(1200, 620)
    window.maxsize(4080, 1060)
    window.iconbitmap(bitmap=("icon.ico"))
    window.config(bg='blue')

    def quiter():
        window.destroy()

    button_quit = Button(window, text="quit", bg='#989898', relief=FLAT, activebackground='black',
                         highlightthickness=0, command=wind and quiter)
    button_quit.place(x=0, y=0)

    window.mainloop()



root = Tk()

root. geometry('200x100')
root.title('menu')
root.maxsize(200, 100)
root.config(bg='#989898')

frame1 = Frame(root, bg='#262626', border=1, borderwidth=1, padx=60, pady=1)

btn = Button(frame1, text="mode sombre", bg='#262626', fg='white', command= create)
btn. pack(pady = 10)

btn = Button(root, text="mode claire", bg='#989898', fg='black', command = wind)
btn. pack(pady = 15)

frame1.pack(side=BOTTOM)



root. mainloop()