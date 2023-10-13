from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
from datetime import datetime
import mysql.connector
from tkinter import messagebox


class Roombooking:
    def __init__(self, root):
        self.root = root
        self.root.title("Room details")
        self.root.geometry("1295x550+400+320")
        self.root.minsize(1295, 550)
        self.root.maxsize(1295, 550)
        root.iconbitmap(".img\\icon.ico")

        # variables
        self.var_contact = StringVar()
        self.var_checkin = StringVar()
        self.var_checkout = StringVar()
        self.var_roomtype = StringVar()
        self.var_floor = StringVar()
        self.var_roomavailable = StringVar()
        self.var_noOfdays = StringVar()
        self.var_paidtax = StringVar()
        self.var_actualtotal = StringVar()
        self.var_total = StringVar()

        # title
        lbl_title = Label(self.root, text="Room booking", font=(
            "times new roman", 30, "bold"), bg="black", fg="silver", anchor="center")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        img2 = Image.open(".img\\logo.png")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=50, height=50)
        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Room details", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        #########labels and enteries
        # customer contact
        lbl_cust_contact = Label(labelframeleft, text="Phone:", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_cust_contact.grid(row=0, column=0, sticky=W)

        entry_contact = ttk.Entry(
            labelframeleft, textvariable=self.var_contact, width=18, font=("arial", 13, "bold"))
        entry_contact.grid(row=0, column=1, sticky=W)

        # fetch buttom
        btnFetchData = Button(labelframeleft, command=self.fetch_contact, text="Fetch data", font=(
            "arial", 8, "bold"), bg="black", fg="silver", width=8, padx=2, pady=2)
        btnFetchData.place(x=347, y=4)

        # checkin date
        check_in_date = Label(labelframeleft, text="Check-in date:",
                              font=("arial", 13, "bold"), padx=2, pady=6)
        check_in_date.grid(row=1, column=0, sticky=W)

        txtcheck_in = ttk.Entry(
            labelframeleft, textvariable=self.var_checkin, width=25, font=("arial", 13, "bold"))
        txtcheck_in.grid(row=1, column=1)

        # checkout date
        check_out_date = Label(
            labelframeleft, text="Check-out date:", font=("arial", 13, "bold"), padx=2, pady=6)
        check_out_date.grid(row=2, column=0, sticky=W)

        txtcheck_out = ttk.Entry(
            labelframeleft, textvariable=self.var_checkout, width=25, font=("arial", 13, "bold"))
        txtcheck_out.grid(row=2, column=1)

        # room type combobox
        label_RoomType = Label(labelframeleft, text="Room type:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        label_RoomType.grid(row=3, column=0, sticky=W)

        combo_RoomType = ttk.Combobox(labelframeleft, textvariable=self.var_roomtype, width=23, font=(
            "arial", 13, "bold"), state="readonly")
        combo_RoomType["value"] = ("Single", "Double", "Luxury")
        combo_RoomType.current()
        combo_RoomType.grid(row=3, column=1)

        # floor
        lblfloor = Label(labelframeleft, text="Floor:",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lblfloor.grid(row=4, column=0, sticky=W)

        combo_floor = ttk.Combobox(labelframeleft, textvariable=self.var_floor, width=23, font=(
            "arial", 13, "bold"), state="readonly")
        combo_floor["value"] = (
            "Ground", "First", "Second", "Third", "Fourth", "Fifth", "Sixth", "Seventh")
        combo_floor.current()
        combo_floor.grid(row=4, column=1)

        # room
        lblRoomAvailable = Label(labelframeleft, text="Room available:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblRoomAvailable.grid(row=5, column=0, sticky=W)

        entry_room = ttk.Entry(
            labelframeleft, textvariable=self.var_roomavailable, width=25, font=("arial", 13, "bold"))
        entry_room.grid(row=5, column=1)

        # no. of days
        lblNoOfDays = Label(labelframeleft, text="No. of days:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblNoOfDays.grid(row=6, column=0, sticky=W)

        txtNoOfDays = ttk.Entry(
            labelframeleft, textvariable=self.var_noOfdays, width=25, font=("arial", 13, "bold"))
        txtNoOfDays.grid(row=6, column=1)

        # tax
        lblTax = Label(labelframeleft, text="Tax:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblTax.grid(row=7, column=0, sticky=W)

        txtTax = ttk.Entry(labelframeleft, textvariable=self.var_paidtax,
                           width=25, font=("arial", 13, "bold"))
        txtTax.grid(row=7, column=1)

        # subtotal
        lblSubTotal = Label(labelframeleft, text="Sub total:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblSubTotal.grid(row=8, column=0, sticky=W)

        txtSubTotal = ttk.Entry(
            labelframeleft, textvariable=self.var_actualtotal, width=25, font=("arial", 13, "bold"))
        txtSubTotal.grid(row=8, column=1)

        # total
        lblTotal = Label(labelframeleft, text="Total amount payable:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblTotal.grid(row=9, column=0, sticky=W)

        txtTotal = ttk.Entry(
            labelframeleft, textvariable=self.var_total, width=25, font=("arial", 13, "bold"))
        txtTotal.grid(row=9, column=1)

        # bill button
        btnBill = Button(labelframeleft, text="Bill", command=self.total, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9)
        btnBill.grid(row=10, column=0, padx=1, sticky=W)

        # buttons
        btn_frame = Frame(labelframeleft, bd=2, relief=RIDGE)
        btn_frame.place(x=0, y=400, width=412, height=40)

        btnAdd = Button(btn_frame, text="Add", command=self.add_data, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9)
        btnAdd.grid(row=0, column=0, padx=1)

        btnUpdate = Button(btn_frame, text="Update", command=self.update, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9)
        btnUpdate.grid(row=0, column=1, padx=1)

        btnDelete = Button(btn_frame, text="Delete", command=self.delete, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9)
        btnDelete.grid(row=0, column=2, padx=1)

        btnReset = Button(btn_frame, text="Reset", command=self.reset, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9)
        btnReset.grid(row=0, column=3, padx=1)

        # right side room charges
        RateFrame1 = LabelFrame(self.root, bd=4, relief=RIDGE,
                                text="Room chrages:-", font=("times new roman", 12, "bold"), padx=2)
        RateFrame1.place(x=760, y=55, width=260, height=220)

        lbl_rate1 = Label(RateFrame1, text="Single room = Rs.1500",
                          font=("adabi", 10), padx=2, pady=6)
        lbl_rate1.grid(row=1, column=0, sticky=W)

        lbl_rate2 = Label(RateFrame1, text="Double room = Rs.2000",
                          font=("adabi", 10), padx=2, pady=6)
        lbl_rate2.grid(row=2, column=0, sticky=W)

        lbl_rate3 = Label(RateFrame1, text="Luxury room = Rs.2500",
                          font=("adabi", 10), padx=2, pady=6)
        lbl_rate3.grid(row=3, column=0, sticky=W)

        lbl_rate4 = Label(RateFrame1, text="Tax=18%",
                          font=("adabi", 10), padx=2, pady=6)
        lbl_rate4.grid(row=4, column=0, sticky=W)

        # table frame(search system)
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search system", font=(
            "times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=280, width=860, height=260)

        lblSearchBy = Label(Table_Frame, text="Search by:", font=(
            "arial", 12, "bold"), bg="silver", fg="black")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, width=20, font=(
            "arial", 13, "bold"), state="readonly")
        combo_Search["value"] = ("Contact", "Room")
        combo_Search.current()
        combo_Search.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        txtSearch = ttk.Entry(
            Table_Frame, textvariable=self.txt_search, width=25, font=("arial", 13, "bold"))
        txtSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(Table_Frame, text="Search", command=self.search, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9)
        btnSearch.grid(row=0, column=3, padx=1)

        btnShowAll = Button(Table_Frame, text="Show all", command=self.fetch_data, font=(
            "arial", 13, "bold"), bg="black", fg="silver", width=9)
        btnShowAll.grid(row=0, column=4, padx=1)

        # data table
        details_table = Frame(Table_Frame, bd=2, relief=RIDGE)
        details_table.place(x=0, y=50, width=860, height=180)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.details_table = ttk.Treeview(details_table, column=("Phone", "checkin", "checkout", "roomtype", "floor",
                                          "Room", "noOfdays", "tax", "sub", "total"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.details_table.xview)
        scroll_y.config(command=self.details_table.yview)

        self.details_table.heading("Phone", text="Phone")
        self.details_table.heading("checkin", text="Check in")
        self.details_table.heading("checkout", text="Check out")
        self.details_table.heading("roomtype", text="Room type")
        self.details_table.heading("floor", text="Floor number")
        self.details_table.heading("Room", text="Room no.")
        self.details_table.heading("noOfdays", text="No. of days")
        self.details_table.heading("tax", text="Tax")
        self.details_table.heading("sub", text="Sub total")
        self.details_table.heading("total", text="Total")

        self.details_table["show"] = "headings"
        self.details_table.column("Phone", width=100)
        self.details_table.column("checkin", width=100)
        self.details_table.column("checkout", width=100)
        self.details_table.column("roomtype", width=100)
        self.details_table.column("floor", width=100)
        self.details_table.column("Room", width=100)
        self.details_table.column("noOfdays", width=100)
        self.details_table.column("tax", width=100)
        self.details_table.column("sub", width=100)
        self.details_table.column("total", width=100)
        self.details_table.pack(fill=BOTH, expand=1)
        self.details_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

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
            if self.var_checkin.get() == "" or self.var_checkout.get() == "" or self.var_contact.get() == "" or self.var_roomtype.get() == "" or self.var_roomavailable.get() == "" or self.var_floor.get() == "" or self.var_roomtype.get() == "" or self.var_noOfdays.get() == "" or self.var_paidtax.get() == "" or self.var_paidtax.get() == "" or self.var_total.get() == "" or self.var_actualtotal.get() == "":
                messagebox.showerror(
                    "Error", "Please fill all the details", parent=self.root)
            else:
                try:
                    conn = mysql.connector.connect(
                        host="localhost", username="root", password="1234", database="project")
                    my_cursor = conn.cursor()
                    my_cursor.execute("insert into room values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                        self.var_contact.get(),
                        self.var_checkin.get(),
                        self.var_checkout.get(),
                        self.var_roomtype.get(),
                        self.var_floor.get(),
                        self.var_roomavailable.get(),
                        self.var_noOfdays.get(),
                        self.var_paidtax.get(),
                        self.var_actualtotal.get(),
                        self.var_total.get()
                    ))
                    conn.commit()
                    self.fetch_data()
                    conn.close()
                    messagebox.showinfo(
                        "Success", "Room has been booked", parent=self.root)
                except Exception as es:
                    messagebox.showwarning(
                        "Warning", f"Something went wrong:{str(es)}", parent=self.root)

    # fetch
    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from room")
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
        self.var_checkin.set(row[1]),
        self.var_checkout.set(row[2]),
        self.var_roomtype.set(row[3]),
        self.var_floor.set(row[4]),
        self.var_roomavailable.set(row[5]),
        self.var_noOfdays.set(row[6])

    # update
    def update(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter phone info", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="project")
            my_cursor = conn.cursor()
            my_cursor.execute("update room set Phone=%s,checkin=%s,checkout=%s,roomtype=%s,floor=%s,noOfdays=%s,tax=%s,sub=%s,total=%s where Room=%s", (
                self.var_contact.get(),
                self.var_checkin.get(),
                self.var_checkout.get(),
                self.var_roomtype.get(),
                self.var_floor.get(),
                self.var_noOfdays.get(),
                self.var_paidtax.get(),
                self.var_actualtotal.get(),
                self.var_total.get(),
                self.var_roomavailable.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Room details have been updated")

    # delete
    def delete(self):
        delete = messagebox.askyesno(
            "VManager", "Do you want to delete this entry?", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="project")
            my_cursor = conn.cursor()
            querry = "delete from room where Phone=%s"
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
        self.var_checkin.set(""),
        self.var_checkout.set(""),
        self.var_roomtype.set(""),
        self.var_floor.set(""),
        self.var_roomavailable.set(""),
        self.var_noOfdays.set("")
        self.var_paidtax.set("")
        self.var_actualtotal.set("")
        self.var_total.set("")

    # search system
    def search(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="project")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from room where "+str(self.search_var.get()
                                                          )+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.details_table.delete(*self.details_table.get_children())
            for i in rows:
                self.details_table.insert("", END, values=i)
            conn.commit()
        conn.close()

    # bill generation
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        inDate = datetime.strptime(inDate, "%d/%m/%Y")
        outDate = datetime.strptime(outDate, "%d/%m/%Y")

        self.var_noOfdays.set(abs(outDate-inDate).days)

        if (self.var_roomtype.get() == "Single"):
            q2 = float(1500)
            q3 = float(self.var_noOfdays.get())
            q5 = float(q3*q2)

            Tax = (((q5)*18/100.0))
            ST = ((q5))
            TT = (q5+((q5)*18/100.0))

            self.var_paidtax.set(str(Tax))
            self.var_actualtotal.set(str(ST))
            self.var_total.set(str(TT))

        elif (self.var_roomtype.get() == "Double"):
            q2 = float(2000)
            q3 = float(self.var_noOfdays.get())
            q5 = float(q3*q2)

            Tax = (((q5)*18/100.0))
            ST = ((q5))
            TT = (q5+((q5)*18/100.0))

            self.var_paidtax.set(str(Tax))
            self.var_actualtotal.set(str(ST))
            self.var_total.set(str(TT))

        elif (self.var_roomtype.get() == "Luxury"):
            q2 = float(2500)
            q3 = float(self.var_noOfdays.get())
            q5 = float(q3*q2)

            Tax = (((q5)*18/100.0))
            ST = ((q5))
            TT = (q5+((q5)*18/100.0))

            self.var_paidtax.set(str(Tax))
            self.var_actualtotal.set(str(ST))
            self.var_total.set(str(TT))

    # fetch data for contact

    def fetch_contact(self):
        if self.var_contact.get() == "":
            messagebox.showerror(
                "Error", "Please enter phone info", parent=self.root)
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
                    "Error", "Invalid phone info", parent=self.root)
            else:
                conn.commit()
                conn.close()

                showDataFrame = LabelFrame(self.root, bd=4, relief=RIDGE, padx=2,
                                           text="Customer details:-", font=("times new roman", 12, "bold"))
                showDataFrame.place(x=450, y=55, width=290, height=220)

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

                # address
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

                self.var_roomavailable.set(row)


if __name__ == "__main__":
    root = Tk()
    obj = Roombooking(root)
    root.mainloop()
