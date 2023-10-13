from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Register:
    def __init__(self, root):
        self.root = root
        self.root.title("Admin manager")
        self.root.geometry("400x350+820+320")
        self.root.minsize(400, 350)
        self.root.maxsize(400, 350)
        root.iconbitmap(".img\\icon.ico")

        # vars
        self.var_username = StringVar()
        self.var_vpin = StringVar()
        self.var_pkey = StringVar()

        # title
        lbl_title = Label(self.root, text="Administrator manager", font=(
            "times new roman", 20, "bold"), bg="black", fg="silver", anchor="center")
        lbl_title.place(x=0, y=0, width=400, height=60)

        # logo
        img2 = Image.open(".img\\logo.png")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=50, height=50)

        # main frame
        main_frame = Frame(self.root, bd=4, relief=SUNKEN, bg="silver")
        main_frame.place(x=0, y=60, width=400, height=290)

        # label frame
        labelframeleft = LabelFrame(main_frame, bd=2, relief=RIDGE, text="Register new administrator", font=(
            "times new roman", 12, "bold"), padx=2, bg="silver")
        labelframeleft.place(x=0, y=0, width=395, height=280)

        lbl_blank = Label(labelframeleft, padx=2, pady=6, bg="silver")
        lbl_blank.grid(row=0, column=0)

        lbl_admin = Label(labelframeleft, text="Phone:", font=(
            "roboto", 13, "bold"), padx=2, pady=6, bg="silver")
        lbl_admin.grid(row=1, column=0)

        entry_admin1 = ttk.Entry(
            labelframeleft, textvariable=self.var_username, width=20, font=("arial", 13))
        entry_admin1.grid(row=1, column=1, padx=8, pady=8)

        lbl_vpin = Label(labelframeleft, text="Password:", font=(
            "roboto", 13, "bold"), padx=2, pady=6, bg="silver")
        lbl_vpin.grid(row=2, column=0, sticky='W')

        entry_vpin1 = ttk.Entry(
            labelframeleft, textvariable=self.var_vpin, width=20, font=("arial", 13))
        entry_vpin1.grid(row=2, column=1, padx=8, pady=8)

        lbl_pkey = Label(labelframeleft, text="Product key:", font=(
            "roboto", 13, "bold"), padx=2, pady=6, bg="silver")
        lbl_pkey.grid(row=3, column=0, sticky='W')

        entry_pkey1 = ttk.Entry(
            labelframeleft, textvariable=self.var_pkey, width=20, font=("arial", 13))
        entry_pkey1.grid(row=3, column=1, padx=8, pady=8)

        # button
        add_btn = Button(main_frame, text="Add", width=28, command=self.add_data, height=2, font=(
            "times new roman", 10, "bold"), fg="silver", bg="black", bd=3, cursor="hand2", anchor="center", relief=RAISED)
        add_btn.place(x=60, y=200, width=100, height=30)

        delete_btn = Button(main_frame, text="Delete", command=self.delete, width=28, height=2, font=(
            "times new roman", 10, "bold"), fg="silver", bg="black", bd=3, cursor="hand2", anchor="center", relief=RAISED)
        delete_btn.place(x=220, y=200, width=100, height=30)

        back_btn = Button(main_frame, text="Login page", command=self.exit, height=2, font=(
            "times new roman", 10, "bold"), fg="black", bd=3, cursor="hand2", anchor="center")
        back_btn.place(x=140, y=240, width=100, height=30)

    # add

    def add_data(self):
        if self.var_pkey.get() == "VManager01":
            if self.var_username.get() == "" or self.var_vpin.get() == "":
                messagebox.showerror(
                    "Error", "Please fill all the details", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="1234", database="project")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into admin values(%s,%s)", (
                        self.var_username.get(),
                        self.var_vpin.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(
                        "Success", "New administrator has been added", parent=self.root)
                except Exception as es:
                    messagebox.showwarning(
                        "Warning", f"Something went wrong:{str(es)}", parent=self.root)
        else:
            messagebox.showerror(
                "Error", "Incorrect product key", parent=self.root)

    # delete
    def delete(self):
        if self.var_pkey.get() == "VManager01":
            delete = messagebox.askyesno(
                "VManager", "Do you want to removed this administrator?", parent=self.root)
            if delete > 0:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="project")
                my_cursor = conn.cursor()
                querry = "delete from admin where Phone=%s"
                value = (self.var_username.get(),)
                my_cursor.execute(querry, value)
            else:
                if not delete:
                    return
            conn.commit()
            conn.close()
        else:
            messagebox.showerror(
                "Error", "Incorrect product key", parent=self.root)

    # exit
    def exit(self):
        self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Register(root)
    root.mainloop()
