from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox
from register import Register
from hotel import ManagementSystem


class Login:
    def __init__(self, root):
        self.root = root
        self.root.title("VManager")
        self.root.geometry("300x350+820+320")
        self.root.minsize(300, 350)
        self.root.maxsize(300, 350)
        root.iconbitmap(".img\\icon.ico")

        # vars
        self.var_username = StringVar()
        self.var_vpin = StringVar()

        # title
        lbl_title = Label(self.root, text="WELCOME", font=(
            "times new roman", 20, "bold"), bg="black", fg="silver", anchor="center")
        lbl_title.place(x=0, y=0, width=300, height=60)

        # logo
        img2 = Image.open(".img\\logo.png")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=50, height=50)

        # main frame
        main_frame = Frame(self.root, bd=4, relief=SUNKEN, bg="silver")
        main_frame.place(x=0, y=60, width=300, height=290)

        # label frame
        labelframeleft = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Log in or Register", font=(
            "times new roman", 12, "bold"), padx=2, bg="silver")
        labelframeleft.place(x=0, y=0, width=290, height=280)

        lbl_blank = Label(labelframeleft, padx=2, pady=6, bg="silver")
        lbl_blank.grid(row=0, column=0)

        lbl_admin = Label(labelframeleft, text="Phone:", font=(
            "roboto", 13, "bold"), padx=2, pady=6, bg="silver")
        lbl_admin.grid(row=1, column=0)

        entry_admin = ttk.Entry(
            labelframeleft, textvariable=self.var_username, width=20, font=("arial", 13))
        entry_admin.grid(row=1, column=1, padx=8, pady=8)

        lbl_admin = Label(labelframeleft, text="Password:", font=(
            "roboto", 13, "bold"), padx=2, pady=6, bg="silver")
        lbl_admin.grid(row=2, column=0, sticky='W')

        entry_admin = ttk.Entry(
            labelframeleft, textvariable=self.var_vpin, width=20, font=("arial", 13))
        entry_admin.grid(row=2, column=1, padx=8, pady=8)

        # button
        log_btn = Button(main_frame, text="LOGIN", command=self.login, width=28, height=2, font=(
            "times new roman", 10, "bold"), fg="silver", bg="black", bd=3, cursor="hand2", anchor="center", relief=RAISED)
        log_btn.place(x=30, y=160, width=80, height=30)

        reg_btn = Button(main_frame, text="REGISTER", command=self.register, width=28, height=2, font=(
            "times new roman", 10, "bold"), fg="silver", bg="black", bd=3, cursor="hand2", anchor="center", relief=RAISED)
        reg_btn.place(x=190, y=160, width=80, height=30)

        back_btn = Button(main_frame, text="Exit", command=self.exit, height=2, font=(
            "times new roman", 10, "bold"), fg="black", bd=3, cursor="hand2", anchor="center")
        back_btn.place(x=120, y=200, width=60, height=20)

        # developer
        lbl_trb = Label(labelframeleft, text="Having trouble?\nEmail us at devanshmuj@gmail.com",
                        font=("roboto", 10, "bold"), padx=2, pady=6, bg="sky blue")
        lbl_trb.place(x=0, y=215, width=280, height=40)

    def login(self):
        if self.var_username.get() == "" or self.var_vpin.get() == "":
            messagebox.showerror(
                "Error", "Phone and Password required", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="project")
            my_cursor = conn.cursor()
            querry = ("select Phone from admin where password=%s")
            value = (self.var_vpin.get(),)
            my_cursor.execute(querry, value)
            username = my_cursor.fetchone()

            if (username == None):
                messagebox.showerror(
                    "Error", "Incorrect Phone or password", parent=self.root)
            else:
                conn.commit()
                conn.close()
                self.mainf()

    def register(self):
        self.new_window = Toplevel(self.root)
        self.app = Register(self.new_window)

    def mainf(self):
        self.new_window = Toplevel(self.root)
        self.app = ManagementSystem(self.new_window)

    def exit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Login(root)
    root.mainloop()
