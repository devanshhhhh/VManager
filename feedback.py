from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Feedback:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer feedback")
        self.root.geometry("1095x450+400+320")
        self.root.minsize(1095, 450)
        self.root.maxsize(1095, 450)
        root.iconbitmap(".img\\icon.ico")

        # vars
        self.var_feedbackgood = StringVar()
        self.var_feedbackbad = StringVar()
        self.var_feedbackrec = StringVar()
        self.var_feedbackoverall = StringVar()
        self.var_contact = StringVar()

        # title
        lbl_title = Label(self.root, text="Customer feedback", font=(
            "times new roman", 30, "bold"), bg="black", fg="silver", anchor="center")
        lbl_title.place(x=0, y=0, width=1095, height=50)

        # logo
        img2 = Image.open(".img\\logo.png")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=50, height=50)

        # customer contact
        lbl_cust_contact = Label(self.root, text="Contact:", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_cust_contact.place(x=655, y=90, width=80, height=30)

        entry_contact = ttk.Entry(
            self.root, textvariable=self.var_contact, width=18, font=("arial", 10))
        entry_contact.place(x=735, y=95, width=250, height=20)

        # fetch buttom
        btnFetchData = Button(self.root, command=self.fetch_contact, text="Fetch data", font=(
            "arial", 8, "bold"), bg="black", fg="silver", width=8, padx=2, pady=2, relief=RAISED)
        btnFetchData.place(x=990, y=95, width=80, height=20)

        # label frame
        labelframeleft = LabelFrame(
            self.root, bd=2, relief=RIDGE, text="Feedback:-", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=650, height=490)

        label_good = Label(labelframeleft, text="What you liked?", font=(
            "times new  roman", 12, "bold"), padx=2, pady=6)
        label_good.grid(row=0, column=0, sticky=W, padx=4, pady=4)
        text_good = ttk.Entry(
            labelframeleft, textvariable=self.var_feedbackgood, font=("arial", 10), width=90)
        text_good.grid(row=1, column=0, sticky=W, padx=4, pady=4)

        label_bad = Label(labelframeleft, text="Where can we improve?", font=(
            "times new  roman", 12, "bold"), padx=2, pady=6)
        label_bad.grid(row=2, column=0, sticky=W, padx=4, pady=4)
        text_bad = ttk.Entry(
            labelframeleft, textvariable=self.var_feedbackbad, font=("arial", 10), width=90)
        text_bad.grid(row=3, column=0, sticky=W, padx=4, pady=4)

        label_overall = Label(labelframeleft, text="Rate your overall experience", font=(
            "times new  roman", 12, "bold"), padx=2, pady=6)
        label_overall.grid(row=4, column=0, sticky=W, padx=4, pady=4)
        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_feedbackoverall, width=88, font=(
            "arial", 10), state="readonly")
        combo_gender["value"] = ("Excellent", "Good", "Considerable", "Bad")
        combo_gender.current()
        combo_gender.grid(row=5, column=0)

        label_rec = Label(labelframeleft, text="Will you be recommeding our establishment to your friends and family?", font=(
            "times new  roman", 12, "bold"), padx=2, pady=6)
        label_rec.grid(row=6, column=0, sticky=W, padx=4, pady=4)
        combo_rec = ttk.Combobox(labelframeleft, textvariable=self.var_feedbackrec, width=88, font=(
            "arial", 10), state="readonly")
        combo_rec["value"] = ("Yes", "No", "Not sure")
        combo_rec.current()
        combo_rec.grid(row=7, column=0)

        lbl_title = Label(labelframeleft, text="(Max=240 characters)", font=(
            "adabi", 8), fg="black", anchor="center")
        lbl_title.place(x=220, y=340, width=200, height=20)

        # save button
        btnSave = Button(labelframeleft, text="Save", command=self.save, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9, relief=RAISED, bd=3)
        btnSave.place(x=526, y=320, width=100, height=40)

        # reset button
        btnReset = Button(labelframeleft, text="Reset", command=self.reset, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9, relief=RAISED, bd=3)
        btnReset.place(x=8, y=320, width=100, height=40)

    # save
    def save(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="project")
        my_cursor = conn.cursor()
        querry = ("select name from customer where Contact=%s")
        value = (self.var_contact.get(),)
        my_cursor.execute(querry, value)
        name = my_cursor.fetchone()

        if name == None:
            messagebox.showerror(
                "Error", "Customer not found\n \nPlease check if the customer is added", parent=self.root)
        else:
            if self.var_contact.get() == "" or self.var_feedbackgood.get() == "" or self.var_feedbackbad.get() == "" or self.var_feedbackoverall.get() == "" or self.var_feedbackrec.get() == "":
                messagebox.showerror(
                    "Error", "Please fill the feedback form and contact info", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="1234", database="project")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into feedback values(%s,%s,%s,%s,%s)", (
                        self.var_contact.get(),
                        self.var_feedbackgood.get(),
                        self.var_feedbackbad.get(),
                        self.var_feedbackoverall.get(),
                        self.var_feedbackrec.get()
                    ))
                    conn.commit()
                    conn.close()
                    messagebox.showinfo(
                        "Success", "Feedback stored", parent=self.root)
                except Exception as es:
                    messagebox.showwarning(
                        "Warning", f"Something went wrong:{str(es)}", parent=self.root)
    # reset

    def reset(self):
        self.var_contact.set(""),
        self.var_feedbackoverall.set(""),
        self.var_feedbackbad.set(""),
        self.var_feedbackgood.set(""),
        self.var_feedbackrec.set("")

    # fetch data for contact
    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter contact info", parent=self.root)
        else:
            # name
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="project")
            my_cursor = conn.cursor()
            querry = ("select name from customer where Contact=%s")
            value = (self.var_contact.get(),)
            my_cursor.execute(querry, value)
            row = my_cursor.fetchone()

            if row == None:
                messagebox.showerror(
                    "Error", "Invalid contact info", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame = LabelFrame(self.root, bd=4, relief=RIDGE, padx=2,
                                           text="Customer details:-", font=("times new roman", 12, "bold"))
                showDataFrame.place(x=700, y=130, width=320, height=290)

                lblName = Label(showDataFrame, text="Name:",
                                font=("arial", 12, "bold"))
                lblName.place(x=0, y=0)

                lbl1 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl1.place(x=90, y=0)

                # gender
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="project")
                my_cursor = conn.cursor()
                querry = ("select gender from customer where Contact=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblGender = Label(showDataFrame, text="Gender:",
                                  font=("arial", 12, "bold"))
                lblGender.place(x=0, y=30)

                lbl2 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl2.place(x=90, y=30)

                # email
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="project")
                my_cursor = conn.cursor()
                querry = ("select email from customer where Contact=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblEmail = Label(showDataFrame, text="Email:",
                                 font=("arial", 12, "bold"))
                lblEmail.place(x=0, y=60)

                lbl3 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl3.place(x=90, y=60)

                # nationality
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="project")
                my_cursor = conn.cursor()
                querry = ("select nationality from customer where Contact=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblNationality = Label(
                    showDataFrame, text="Nationality:", font=("arial", 12, "bold"))
                lblNationality.place(x=0, y=90)

                lbl2 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl2.place(x=90, y=90)

                # address
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="project")
                my_cursor = conn.cursor()
                querry = ("select address from customer where Contact=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblAddress = Label(
                    showDataFrame, text="Address:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=120)

                lbl3 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl3.place(x=90, y=120)

                # checkin
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="project")
                my_cursor = conn.cursor()
                querry = ("select checkin from customer where Contact=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblAddress = Label(
                    showDataFrame, text="Check-in:", font=("arial", 12, "bold"))
                lblAddress.place(x=0, y=150)

                lbl4 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl4.place(x=90, y=150)

                # room no.
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="project")
                my_cursor = conn.cursor()
                querry = ("select Room from room where Phone=%s")
                value = (self.var_contact.get(),)
                my_cursor.execute(querry, value)
                row = my_cursor.fetchone()

                lblroomno = Label(showDataFrame, text="Room no.:",
                                  font=("arial", 12, "bold"))
                lblroomno.place(x=0, y=180)

                lbl4 = Label(showDataFrame, text=row, font=("arial", 12))
                lbl4.place(x=90, y=180)


if __name__ == "__main__":
    root = Tk()
    obj = Feedback(root)
    root.mainloop()
