from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
from tkinter import messagebox


class Extras:
    def __init__(self, root):
        self.root = root
        self.root.title("Extras")
        self.root.geometry("1095x450+400+320")
        self.root.minsize(1095, 450)
        self.root.maxsize(1095, 450)
        root.iconbitmap(".img\\icon.ico")

        # variables
        self.var_contact = IntVar()

        self.var_extra1 = StringVar()
        self.var_extra2 = StringVar()
        self.var_extra3 = StringVar()
        self.var_extra4 = StringVar()
        self.var_extra5 = StringVar()
        self.var_extra_cost1 = IntVar()
        self.var_extra_cost2 = IntVar()
        self.var_extra_cost3 = IntVar()
        self.var_extra_cost4 = IntVar()
        self.var_extra_cost5 = IntVar()
        self.var_extra_quan1 = IntVar()
        self.var_extra_quan2 = IntVar()
        self.var_extra_quan3 = IntVar()
        self.var_extra_quan4 = IntVar()
        self.var_extra_quan5 = IntVar()
        self.var_extra_total1 = StringVar()
        self.var_extra_total2 = StringVar()
        self.var_extra_total3 = StringVar()
        self.var_extra_total4 = StringVar()
        self.var_extra_total5 = StringVar()

        self.var_subtotal = StringVar()
        self.var_extax = StringVar()
        self.var_finaltotal = StringVar()

        # final bill vars
        self.var_alltax = StringVar()
        self.var_alltotal = StringVar()

        # title
        lbl_title = Label(self.root, text="Value added services", font=(
            "times new roman", 30, "bold"), bg="black", fg="silver", anchor="center")
        lbl_title.place(x=0, y=0, width=1095, height=50)

        # logo
        img2 = Image.open(".img\\logo.png")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=50, height=50)

        # label frame
        labelframeleft = LabelFrame(
            self.root, bd=2, relief=RIDGE, text="Extras:-", font=("times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=650, height=490)

        # customer contact
        lbl_cust_contact = Label(labelframeleft, text="Contact:", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(
            labelframeleft, textvariable=self.var_contact, width=18, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        btnTotal = Button(labelframeleft, text="Validate", command=self.validate, font=(
            "times new roman", 7, "bold"), bg="silver", fg="black", width=7, padx=2, pady=6)
        btnTotal.grid(row=0, column=2, sticky=W, padx=8, pady=8)

        #########labels and enteries
        lbl_0_0 = Label(labelframeleft, text="Name", font=(
            "times new roman", 15, "bold"), padx=2, pady=6, fg="black", width=7)
        lbl_0_0.grid(row=1, column=1, sticky=W)
        lbl_0_1 = Label(labelframeleft, text="Cost", font=(
            "times new roman", 15, "bold"), padx=2, pady=6, fg="black", width=7)
        lbl_0_1.grid(row=1, column=2, sticky=W, padx=8)
        lbl_0_1 = Label(labelframeleft, text="Quantity", font=(
            "times new roman", 15, "bold"), padx=2, pady=6, fg="black", width=7)
        lbl_0_1.grid(row=1, column=3, sticky=W, padx=8)

        btnTotal = Button(labelframeleft, text="Total", command=self.total, font=(
            "times new roman", 13, "bold"), bg="silver", fg="black", width=7, padx=2, pady=6, relief=RAISED)
        btnTotal.grid(row=1, column=4, sticky=W, padx=8)

        # extra1
        lbl_1 = Label(labelframeleft, text="(1)", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_1.grid(row=2, column=0, sticky=W)

        entry_1 = ttk.Entry(
            labelframeleft, textvariable=self.var_extra1, width=18, font=("arial", 13, "bold"))
        entry_1.grid(row=2, column=1, sticky=W)

        entry_1_1 = ttk.Entry(
            labelframeleft, textvariable=self.var_extra_cost1, width=12, font=("arial", 10, "bold"))
        entry_1_1.grid(row=2, column=2, sticky=W, padx=8)

        entry_1_2 = ttk.Entry(
            labelframeleft, width=12, textvariable=self.var_extra_quan1, font=("arial", 10, "bold"))
        entry_1_2.grid(row=2, column=3, sticky=W, padx=8)

        entry_1_3 = ttk.Entry(labelframeleft, width=14, textvariable=self.var_extra_total1, font=(
            "arial", 10, "bold"), state="readonly")
        entry_1_3.grid(row=2, column=4, sticky=W, padx=8)

        # extra2
        lbl_2 = Label(labelframeleft, text="(2)", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_2.grid(row=3, column=0, sticky=W)

        entry_2 = ttk.Entry(
            labelframeleft, textvariable=self.var_extra2, width=18, font=("arial", 13, "bold"))
        entry_2.grid(row=3, column=1, sticky=W)

        entry_2_1 = ttk.Entry(
            labelframeleft, width=12, textvariable=self.var_extra_cost2, font=("arial", 10, "bold"))
        entry_2_1.grid(row=3, column=2, sticky=W, padx=8)

        entry_2_2 = ttk.Entry(
            labelframeleft, width=12, textvariable=self.var_extra_quan2, font=("arial", 10, "bold"))
        entry_2_2.grid(row=3, column=3, sticky=W, padx=8)

        entry_2_3 = ttk.Entry(labelframeleft, width=14, textvariable=self.var_extra_total2, font=(
            "arial", 10, "bold"), state="readonly")
        entry_2_3.grid(row=3, column=4, sticky=W, padx=8)

        # extra3
        lbl_3 = Label(labelframeleft, text="(1)", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_3.grid(row=4, column=0, sticky=W)

        entry_3 = ttk.Entry(labelframeleft, width=18,
                            textvariable=self.var_extra3, font=("arial", 13, "bold"))
        entry_3.grid(row=4, column=1, sticky=W)

        entry_3_1 = ttk.Entry(
            labelframeleft, width=12, textvariable=self.var_extra_cost3, font=("arial", 10, "bold"))
        entry_3_1.grid(row=4, column=2, sticky=W, padx=8)

        entry_3_2 = ttk.Entry(
            labelframeleft, width=12, textvariable=self.var_extra_quan3, font=("arial", 10, "bold"))
        entry_3_2.grid(row=4, column=3, sticky=W, padx=8)

        entry_3_2 = ttk.Entry(labelframeleft, width=14, textvariable=self.var_extra_total3, font=(
            "arial", 10, "bold"), state="readonly")
        entry_3_2.grid(row=4, column=4, sticky=W, padx=8)

        # extra4
        lbl_4 = Label(labelframeleft, text="(4)", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_4.grid(row=5, column=0, sticky=W)

        entry_4 = ttk.Entry(labelframeleft, width=18,
                            textvariable=self.var_extra4, font=("arial", 13, "bold"))
        entry_4.grid(row=5, column=1, sticky=W)

        entry_4_1 = ttk.Entry(
            labelframeleft, width=12, textvariable=self.var_extra_cost4, font=("arial", 10, "bold"))
        entry_4_1.grid(row=5, column=2, sticky=W, padx=8)

        entry_4_2 = ttk.Entry(
            labelframeleft, width=12, textvariable=self.var_extra_quan4, font=("arial", 10, "bold"))
        entry_4_2.grid(row=5, column=3, sticky=W, padx=8)

        entry_4_2 = ttk.Entry(labelframeleft, width=14, textvariable=self.var_extra_total4, font=(
            "arial", 10, "bold"), state="readonly")
        entry_4_2.grid(row=5, column=4, sticky=W, padx=8)

        # extra5
        lbl_5 = Label(labelframeleft, text="(5)", font=(
            "arial", 10, "bold"), padx=2, pady=6)
        lbl_5.grid(row=6, column=0, sticky=W)

        entry_5 = ttk.Entry(labelframeleft, width=18,
                            textvariable=self.var_extra5, font=("arial", 13, "bold"))
        entry_5.grid(row=6, column=1, sticky=W)

        entry_5_1 = ttk.Entry(
            labelframeleft, width=12, textvariable=self.var_extra_cost5, font=("arial", 10, "bold"))
        entry_5_1.grid(row=6, column=2, sticky=W, padx=8)

        entry_5_2 = ttk.Entry(
            labelframeleft, width=12, textvariable=self.var_extra_quan5, font=("arial", 10, "bold"))
        entry_5_2.grid(row=6, column=3, sticky=W, padx=8)

        entry_5_2 = ttk.Entry(labelframeleft, width=14, textvariable=self.var_extra_total5, font=(
            "arial", 10, "bold"), state="readonly")
        entry_5_2.grid(row=6, column=4, sticky=W, padx=8)

        # buttons
        btn_frame = Frame(labelframeleft, bd=2)
        btn_frame.place(x=130, y=320, width=380, height=60)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9, relief=RAISED, bd=8)
        btnAdd.grid(row=0, column=0, padx=8)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9, relief=RAISED, bd=8)
        btnDelete.grid(row=0, column=1, padx=8)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9, relief=RAISED, bd=8)
        btnReset.grid(row=0, column=2, padx=8)

        # table frame(search system)
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details", font=(
            "times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=675, y=140, width=400, height=290)

        # data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=5, y=10, width=380, height=255)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.details_table = ttk.Treeview(details_table, column=(
            "Contactno", "subtotal", "extax", "finaltotal"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        self.details_table.heading("Contactno", text="Contact")
        self.details_table.heading("subtotal", text="Sub total")
        self.details_table.heading("extax", text="Tax")
        self.details_table.heading("finaltotal", text="Final total")

        self.details_table["show"] = "headings"
        self.details_table.column("Contactno", width=100)
        self.details_table.column("subtotal", width=100)
        self.details_table.column("extax", width=100)
        self.details_table.column("finaltotal", width=100)
        self.details_table.pack(fill=BOTH, expand=1)
        self.details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # valdiation
    def validate(self):
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

                showDataFrame = LabelFrame(
                    self.root, bd=4, relief=RIDGE, padx=2)
                showDataFrame.place(x=675, y=60, width=280, height=60)

                lblName = Label(showDataFrame, text="""Customer validation successful
Please continue""", font=("times new roman", 13, "bold"))
                lblName.place(x=0, y=0)
    # add and display data
    # add

    def add_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="project")
        my_cursor = conn.cursor()
        querry = ("select name from customer where Contact=%s")
        value = (self.var_contact.get(),)
        my_cursor.execute(querry, value)
        row = my_cursor.fetchone()

        if row == None:
            messagebox.showerror(
                "Error", "Customer not found\n \nPlease check if the customer is added", parent=self.root)
        else:
            if self.var_contact.get() == "":
                messagebox.showerror(
                    "Error", "Please fill all the details", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="1234", database="project")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into extras values(%s,%s,%s,%s)", (
                        self.var_contact.get(),
                        self.var_subtotal.get(),
                        self.var_extax.get(),
                        self.var_finaltotal.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo(
                        "Success", "Extra services added", parent=self.root)
                except Exception as es:
                    messagebox.showwarning(
                        "Warning", f"Something went wrong:{str(es)}", parent=self.root)

    # fetch
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from extras")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.details_table.delete(*self.details_table.get_children())
            for i in rows:
                self.details_table.insert("", END, values=i)
        conn.commit()
        conn.close()

    # get cursor
    def get_cursor(self, event=""):
        cursor_row = self.details_table.focus()
        content = self.details_table.item(cursor_row)
        row = content["values"]

        self.var_contact.set(row[0]),
        self.var_subtotal.set(row[1]),
        self.var_extax.set(row[2]),
        self.var_finaltotal.set(row[3])

    # delete
    def delete(self):
        delete = messagebox.askyesno(
            "VManager", "Do you want to delete this entry?", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="project")
            my_cursor = conn.cursor()
            querry = "delete from extras where Contactno=%d"
            value = (self.var_contact.get(),)
            my_cursor.execute(querry, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    # reset
    def reset(self):

        self.var_contact.set(""),
        self.var_extra1.set(""),
        self.var_extra2.set(""),
        self.var_extra3.set(""),
        self.var_extra4.set(""),
        self.var_extra5.set(""),
        self.var_extra_cost1.set(""),
        self.var_extra_cost2.set(""),
        self.var_extra_cost3.set(""),
        self.var_extra_cost4.set(""),
        self.var_extra_cost5.set(""),
        self.var_extra_quan1.set(""),
        self.var_extra_quan2.set(""),
        self.var_extra_quan3.set(""),
        self.var_extra_quan4.set(""),
        self.var_extra_quan5.set(""),
        self.var_extra_total1.set(""),
        self.var_extra_total2.set(""),
        self.var_extra_total3.set(""),
        self.var_extra_total4.set(""),
        self.var_extra_total5.set(""),
        self.var_subtotal.set(""),
        self.var_extax.set(""),
        self.var_finaltotal.set("")

    # fetch data for contact
    def total(self):
        if(self.var_extra1.get() != "" or self.var_extra2.get() != "" or self.var_extra3.get() != "" or self.var_extra4.get() != "" or self.var_extra5.get() != ""):
            c1 = float(self.var_extra_cost1.get())
            c2 = float(self.var_extra_cost2.get())
            c3 = float(self.var_extra_cost3.get())
            c4 = float(self.var_extra_cost4.get())
            c5 = float(self.var_extra_cost5.get())

            q1 = float(self.var_extra_quan1.get())
            q2 = float(self.var_extra_quan2.get())
            q3 = float(self.var_extra_quan3.get())
            q4 = float(self.var_extra_quan4.get())
            q5 = float(self.var_extra_quan5.get())

            t1 = c1*q1
            t2 = c2*q2
            t3 = c3*q3
            t4 = c4*q4
            t5 = c5*q5

            self.var_extra_total1.set(str(t1))
            self.var_extra_total2.set(str(t2))
            self.var_extra_total3.set(str(t3))
            self.var_extra_total4.set(str(t4))
            self.var_extra_total5.set(str(t5))

        else:
            x = 0.0
            self.var_extra_total1.set(str(x))
            self.var_extra_total2.set(str(x))
            self.var_extra_total3.set(str(x))
            self.var_extra_total4.set(str(x))
            self.var_extra_total5.set(str(x))

        st1 = float(self.var_extra_total1.get())
        st2 = float(self.var_extra_total2.get())
        st3 = float(self.var_extra_total3.get())
        st4 = float(self.var_extra_total4.get())
        st5 = float(self.var_extra_total5.get())

        ST = (st1+st2+st3+st4+st5)
        TAX = (ST*(18/100.0))
        FT = (TAX+ST)

        self.var_subtotal.set(str(ST))
        self.var_extax.set(str(TAX))
        self.var_finaltotal.set(str(FT))


if __name__ == "__main__":
    root = Tk()
    obj = Extras(root)
    root.mainloop()
