from tkinter import*
from PIL import Image, ImageTk


class crd:
    def __init__(self, root):
        self.root = root
        self.root.title("Credits")
        self.root.geometry("450x250+720+420")
        self.root.minsize(450, 250)
        self.root.maxsize(450, 250)
        root.iconbitmap(".img\\icon.ico")

    # title
        lbl_title = Label(self.root, text="Credits", font=(
            "times new roman", 30, "bold"), bg="black", fg="silver", anchor="center")
        lbl_title.place(x=0, y=0, width=450, height=55)

    # logo
        img2 = Image.open(".img\\logo.png")
        img2 = img2.resize((50, 50), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)

        lblimg2 = Label(self.root, image=self.photoimg2, bd=0, relief=RIDGE)
        lblimg2.place(x=5, y=2, width=50, height=50)

    # label frame
        labelframeleft = LabelFrame(self.root, bd=8, relief=RIDGE, font=(
            "times new roman", 20, "bold"), padx=2, bg="sky blue")
        labelframeleft.place(x=0, y=55, width=450, height=198)

    # labels
        lbl_developedby = Label(labelframeleft, text="Developed by:-", font=(
            "times new roman", 20, "bold"), padx=2, pady=6, bg="sky blue")
        lbl_developedby.grid(row=0, column=0, sticky=W)

        lbl_dev1 = Label(labelframeleft, text="Devansh Arora", font=(
            "adabi", 13, "italic"), padx=2, pady=6, bg="sky blue")
        lbl_dev1.grid(row=1, column=0, sticky=W)



if __name__ == "__main__":
    root = Tk()
    obj = crd(root)
    root.mainloop()
