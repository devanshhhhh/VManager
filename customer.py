from tkinter import*
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Cust_Win:
    def __init__(self, root):
        self.root = root
        self.root.title("Customer details")
        self.root.geometry("1295x550+400+320")
        self.root.minsize(1295, 550)
        self.root.maxsize(1295, 550)
        root.iconbitmap(".img\\icon.ico")

        # variables
        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

        self.var_cust_name = StringVar()
        self.var_cust_checkin = StringVar()
        self.var_cust_gender = StringVar()
        self.var_cust_postal = StringVar()
        self.var_cust_mobile = StringVar()
        self.var_cust_email = StringVar()
        self.var_cust_nationality = StringVar()
        self.var_cust_idp = StringVar()
        self.var_cust_idn = StringVar()
        self.var_cust_addd = StringVar()

        # title
        lbl_title = Label(self.root, text="Customer details", font=(
            "times new roman", 30, "bold"), bg="black", fg="silver", anchor="center")
        lbl_title.place(x=0, y=0, width=1295, height=50)

        # logo
        img2 = Image.open(".img\\logo.png")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=50, height=50)

        # label frame
        labelframeleft = LabelFrame(self.root, bd=2, relief=RIDGE, text="Customer details", font=(
            "times new roman", 12, "bold"), padx=2)
        labelframeleft.place(x=5, y=50, width=425, height=490)

        #########labels and enteries
        # cust ID
        lbl_cust_ref = Label(labelframeleft, text="ID:", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        lbl_cust_ref.grid(row=0, column=0, sticky=W)

        entry_ref = ttk.Entry(labelframeleft, textvariable=self.var_ref, width=25, font=(
            "arial", 13, "bold"), state='readonly')
        entry_ref.grid(row=0, column=1)

        # cust name
        cname = Label(labelframeleft, text="Name:", font=(
            "arial", 13, "bold"), padx=2, pady=6)
        cname.grid(row=1, column=0, sticky=W)

        txtcname = ttk.Entry(
            labelframeleft, textvariable=self.var_cust_name, width=25, font=("arial", 13, "bold"))
        txtcname.grid(row=1, column=1)

        # checkin
        lblmname = Label(labelframeleft, text="Check-in:",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lblmname.grid(row=2, column=0, sticky=W)

        txtmname = ttk.Entry(
            labelframeleft, textvariable=self.var_cust_checkin, width=25, font=("arial", 13, "bold"))
        txtmname.grid(row=2, column=1)

        # gender combobox
        label_gender = Label(labelframeleft, text="Gender:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        label_gender.grid(row=3, column=0, sticky=W)

        combo_gender = ttk.Combobox(labelframeleft, textvariable=self.var_cust_gender, width=23, font=(
            "arial", 13, "bold"), state="readonly")
        combo_gender["value"] = ("Male", "Female", "Other")
        combo_gender.current()
        combo_gender.grid(row=3, column=1)

        # postcode
        lblPostCode = Label(labelframeleft, text="Postal code:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblPostCode.grid(row=4, column=0, sticky=W)

        txtPostCode = ttk.Entry(
            labelframeleft, textvariable=self.var_cust_postal, width=25, font=("arial", 13, "bold"))
        txtPostCode.grid(row=4, column=1)

        # contact
        lblMobile = Label(labelframeleft, text="Contact:",
                          font=("arial", 12, "bold"), padx=2, pady=6)
        lblMobile.grid(row=5, column=0, sticky=W)

        txtMobile = ttk.Entry(
            labelframeleft, textvariable=self.var_cust_mobile, width=25, font=("arial", 13, "bold"))
        txtMobile.grid(row=5, column=1)

        # email
        lblEmail = Label(labelframeleft, text="Email:",
                         font=("arial", 12, "bold"), padx=2, pady=6)
        lblEmail.grid(row=6, column=0, sticky=W)

        txtEmail = ttk.Entry(
            labelframeleft, textvariable=self.var_cust_email, width=25, font=("arial", 13, "bold"))
        txtEmail.grid(row=6, column=1)

        # nationality combobox
        lblNationality = Label(labelframeleft, text="Nationality:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblNationality.grid(row=7, column=0, sticky=W)

        combo_Nationality = ttk.Combobox(labelframeleft, textvariable=self.var_cust_nationality, width=23, font=(
            "arial", 13, "bold"), state="readonly")
        combo_Nationality["value"] = ("Indian", "Other")
        combo_Nationality.current()
        combo_Nationality.grid(row=7, column=1)

        # idproof combobox
        lblIdProof = Label(labelframeleft, text="ID proof type:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblIdProof.grid(row=8, column=0, sticky=W)

        combo_Id = ttk.Combobox(labelframeleft, textvariable=self.var_cust_idp, width=23, font=(
            "arial", 13, "bold"), state="readonly")
        combo_Id["value"] = ("Aadhar", "Driving License",
                             "Passport", "PAN Card")
        combo_Id.current()
        combo_Id.grid(row=8, column=1)

        # id no.
        lblIdNumber = Label(labelframeleft, text="ID number:", font=(
            "arial", 12, "bold"), padx=2, pady=6)
        lblIdNumber.grid(row=9, column=0, sticky=W)

        txtIdNumber = ttk.Entry(
            labelframeleft, textvariable=self.var_cust_idn, width=25, font=("arial", 13, "bold"))
        txtIdNumber.grid(row=9, column=1)

        # address
        lblAddress = Label(labelframeleft, text="Address:",
                           font=("arial", 12, "bold"), padx=2, pady=6)
        lblAddress.grid(row=10, column=0, sticky=W)

        txtAddress = ttk.Entry(
            labelframeleft, textvariable=self.var_cust_addd, width=25, font=("arial", 13, "bold"))
        txtAddress.grid(row=10, column=1)

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

        # table frame(search system)
        Table_Frame = LabelFrame(self.root, bd=2, relief=RIDGE, text="View details and search system", font=(
            "times new roman", 12, "bold"), padx=2)
        Table_Frame.place(x=435, y=50, width=860, height=490)

        lblSearchBy = Label(Table_Frame, text="Search by:", font=(
            "arial", 12, "bold"), bg="silver", fg="black")
        lblSearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_Search = ttk.Combobox(Table_Frame, textvariable=self.search_var, width=20, font=(
            "arial", 13, "bold"), state="readonly")
        combo_Search["value"] = ("Contact", "ID")
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
        details_table.place(x=0, y=50, width=852, height=416)

        scroll_x = ttk.Scrollbar(details_table, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(details_table, orient=VERTICAL)

        self.Cust_Details_Table = ttk.Treeview(details_table, column=("ID", "name", "checkin", "gender", "postal", "Contact",
                                               "email", "nationality", "idp", "idn", "addd"), xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Cust_Details_Table.xview)
        scroll_y.config(command=self.Cust_Details_Table.yview)

        self.Cust_Details_Table.heading("ID", text="ID")
        self.Cust_Details_Table.heading("name", text="Name")
        self.Cust_Details_Table.heading("checkin", text="Check-in")
        self.Cust_Details_Table.heading("gender", text="Gender")
        self.Cust_Details_Table.heading("postal", text="Postal code")
        self.Cust_Details_Table.heading("Contact", text="Contact")
        self.Cust_Details_Table.heading("email", text="Email")
        self.Cust_Details_Table.heading("nationality", text="Nationality")
        self.Cust_Details_Table.heading("idp", text="ID Proof")
        self.Cust_Details_Table.heading("idn", text="ID number")
        self.Cust_Details_Table.heading("addd", text="Address")

        self.Cust_Details_Table["show"] = "headings"
        self.Cust_Details_Table.column("ID", width=100)
        self.Cust_Details_Table.column("name", width=100)
        self.Cust_Details_Table.column("checkin", width=100)
        self.Cust_Details_Table.column("gender", width=100)
        self.Cust_Details_Table.column("postal", width=100)
        self.Cust_Details_Table.column("Contact", width=100)
        self.Cust_Details_Table.column("email", width=100)
        self.Cust_Details_Table.column("nationality", width=100)
        self.Cust_Details_Table.column("idp", width=100)
        self.Cust_Details_Table.column("idn", width=100)
        self.Cust_Details_Table.column("addd", width=100)

        self.Cust_Details_Table.pack(fill=BOTH, expand=1)
        self.Cust_Details_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    def add_data(self):
        if self.var_cust_mobile.get() == "" or self.var_cust_name.get() == "" or self.var_cust_checkin.get() == "" or self.var_cust_email.get() == "" or self.var_cust_addd.get() == "" or self.var_cust_gender.get() == "" or self.var_cust_idn.get() == "" or self.var_cust_idp.get() == "" or self.var_cust_postal.get() == "" or self.var_cust_nationality.get() == "":
            messagebox.showerror(
                "Error", "Please fill all the details", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(
                    host="localhost", username="root", password="1234", database="project")
                my_cursor = conn.cursor()
                my_cursor.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)", (
                    self.var_ref.get(),
                    self.var_cust_name.get(),
                    self.var_cust_checkin.get(),
                    self.var_cust_gender.get(),
                    self.var_cust_postal.get(),
                    self.var_cust_mobile.get(),
                    self.var_cust_email.get(),
                    self.var_cust_nationality.get(),
                    self.var_cust_idp.get(),
                    self.var_cust_idn.get(),
                    self.var_cust_addd.get()
                ))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo(
                    "Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning(
                    "Warning", f"Something went wrong:{str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="project")
        my_cursor = conn.cursor()
        my_cursor.execute("select * from customer")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
        conn.commit()
        conn.close()

    def get_cursor(self, event=""):
        cursor_row = self.Cust_Details_Table.focus()
        content = self.Cust_Details_Table.item(cursor_row)
        row = content["values"]

        self.var_ref.set(row[0]),
        self.var_cust_name.set(row[1])
        self.var_cust_checkin.set(row[2])
        self.var_cust_gender.set(row[3])
        self.var_cust_postal.set(row[4])
        self.var_cust_mobile.set(row[5])
        self.var_cust_email.set(row[6])
        self.var_cust_nationality.set(row[7])
        self.var_cust_idp.set(row[8])
        self.var_cust_idn.set(row[9])
        self.var_cust_addd.set(row[10])

    def update(self):
        if self.var_cust_mobile.get() == "":
            messagebox.showerror(
                "Error", "Please enter mobile number", parent=self.root)
        else:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="project")
            my_cursor = conn.cursor()
            my_cursor.execute("update customer set name=%s,checkin=%s,gender=%s,postal=%s,Contact=%s,email=%s,nationality=%s,idp=%s,idn=%s,address=%s where ID=%s", (

                self.var_cust_name.get(),
                self.var_cust_checkin.get(),
                self.var_cust_gender.get(),
                self.var_cust_postal.get(),
                self.var_cust_mobile.get(),
                self.var_cust_email.get(),
                self.var_cust_nationality.get(),
                self.var_cust_idp.get(),
                self.var_cust_idn.get(),
                self.var_cust_addd.get(),
                self.var_ref.get()
            ))
            conn.commit()
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Update", "Details have been updated")

    def delete(self):
        delete = messagebox.askyesno(
            "VManager", "Do you want to delete this entry?", parent=self.root)
        if delete > 0:
            conn = mysql.connector.connect(
                host="localhost", username="root", password="1234", database="project")
            my_cursor = conn.cursor()
            querry = "delete from customer where ID=%s"
            value = (self.var_ref.get(),)
            my_cursor.execute(querry, value)
        else:
            if not delete:
                return
        conn.commit()
        self.fetch_data()
        conn.close()

    def reset(self):
        self.var_ref.set(""),
        self.var_cust_name.set(""),
        self.var_cust_checkin.set(""),
        self.var_cust_gender.set(""),
        self.var_cust_postal.set(""),
        self.var_cust_mobile.set(""),
        self.var_cust_email.set(""),
        self.var_cust_nationality.set(""),
        self.var_cust_idp.set(""),
        self.var_cust_idn.set(""),
        self.var_cust_addd.set("")

        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))

    def search(self):
        conn = mysql.connector.connect(
            host="localhost", username="root", password="1234", database="project")
        my_cursor = conn.cursor()

        my_cursor.execute("select * from customer where " +
                          str(self.search_var.get())+" LIKE '%"+str(self.txt_search.get())+"%'")
        rows = my_cursor.fetchall()
        if len(rows) != 0:
            self.Cust_Details_Table.delete(
                *self.Cust_Details_Table.get_children())
            for i in rows:
                self.Cust_Details_Table.insert("", END, values=i)
            conn.commit()
        conn.close()


if __name__ == "__main__":
    root = Tk()
    obj = Cust_Win(root)
    root.mainloop()
