from tkinter import*
from PIL import Image,ImageTk 
from datetime import datetime
from customer import Cust_Win
from room import Roombooking
from extras import Extras
from credits import crd
from feedback import Feedback


class ManagementSystem:
    def __init__(self,root):
        self.root=root
        self.root.title("VManager")
        self.root.geometry("1280x798+300+120")
        self.root.minsize(1280,798)
        self.root.maxsize(1280,798)
        root.iconbitmap(".img\\icon.ico")
        

        #var
        txt = StringVar()
        
        
        #exterior img
        img1=Image.open(".img\\outer.jpg")
        img1=img1.resize((1280,240),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        lblimg1=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lblimg1.place(x=0,y=0,width=1280,height=240)
    

        #title
        lbl_title=Label(self.root,text="VRecords",font=("times new roman",36,"bold"),bg="black",fg="silver",anchor="center")
        lbl_title.place(x=0,y=241,width=1280,height=60)
        lbl_title1=Label(self.root,text="Your personalised digital database",font=("arial",10),bg="black",fg="dark gray",anchor="center")
        lbl_title1.place(x=0,y=301,width=1280,height=40)
        
        #main frame
        main_frame=Frame(self.root,bd=4,relief=RIDGE)
        main_frame.place(x=0,y=342,width=1280,height=456)

        #logo
        img2=Image.open(".img\\logo.png")
        img2=img2.resize((120,100),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        credits_btn=Button(self.root,command=self.creds,image=self.photoimg2,relief=RAISED,bd=8,bg="black")
        credits_btn.place(x=1160,y=240,width=120,height=101)

        #clock
        def clock_time():
            
            time= datetime.now()
            time= (time.strftime("""%H:%M:%S
%d/%m/%Y"""))
            txt.set(time)

            self.root.after(1000,clock_time)
            
        clock_time()

        lbl100=Label(self.root,textvariable=txt, font =("times new roman",12,"bold"),fg="black",bg="sky blue",relief=GROOVE)
        lbl100.place(x=525,y=702,width=230,height=90)
        
        #menu
        lbl_menu=Label(main_frame,text="MENU",font=("roboto",30,"bold"),bg="sky blue",fg="black",bd=4,relief=RIDGE,anchor="center")
        lbl_menu.place(x=520,y=0,width=230)


        #buttons
        btn_frame=Frame(main_frame,bd=4,relief=SUNKEN)
        btn_frame.place(x=520,y=55,width=232,height=302)
        
        cust_btn=Button(btn_frame,text="Customer",command=self.cust_details,width=20,height=2,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2",anchor="center")
        cust_btn.grid(row=0,column=0,pady=(1,1))

        room_btn=Button(btn_frame,text="Room",command=self.roombooking,width=20,height=2,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2",anchor="center")
        room_btn.grid(row=1,column=0,pady=(1,1))

        extras_btn=Button(btn_frame,text="Extras",command=self.extras,width=20,height=2,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2",anchor="center")
        extras_btn.grid(row=2,column=0,pady=(1,1))

        feedback_btn=Button(btn_frame,text="Feedback",command=self.feedback,width=20,height=2,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2",anchor="center")
        feedback_btn.grid(row=3,column=0,pady=(1,1))

        exit_btn=Button(btn_frame,text="Log out",command=self.exit,width=20,height=2,font=("times new roman",14,"bold"),bg="black",fg="white",bd=0,cursor="hand2",anchor="center")
        exit_btn.grid(row=4,column=0,pady=(1,1))

        #interior img
        img3=Image.open(".img\\interior.jpg")
        img3=img3.resize((518,449),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        lblimg3=Label(main_frame,image=self.photoimg3,bd=4)
        lblimg3.place(x=0,y=0,width=518,height=449)

        #bathroom img
        img4=Image.open(".img\\bathroom.jpg")
        img4=img4.resize((519,449),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        lblimg4=Label(main_frame,image=self.photoimg4,bd=4)
        lblimg4.place(x=754,y=0,width=519,height=449)


    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Cust_Win(self.new_window)

    def roombooking(self):
        self.new_window=Toplevel(self.root)
        self.app=Roombooking(self.new_window)

    def extras(self):
        self.new_window=Toplevel(self.root)
        self.app=Extras(self.new_window)
        
    def exit(self):
        self.root.destroy()
    
    def creds(self):
        self.new_window=Toplevel(self.root)
        self.app=crd(self.new_window)
    
    def feedback(self):
        self.new_window=Toplevel(self.root)
        self.app=Feedback(self.new_window)



if __name__ == "__main__":
    root=Tk()
    obj=ManagementSystem(root)
    root.mainloop()