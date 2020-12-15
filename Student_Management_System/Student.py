from tkinter import *
from tkinter import ttk
import sqlite3 as sq
from tkinter import messagebox

db = sq.connect("Students.db")
cur = db.cursor()
cur.execute('create table if not exists Student(Rollno text primary key, name text, email text, gender text, '
            'contact int, '
            'dob date, address text)')


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System", bd=10, relief=GROOVE,
                      font=("times new roman", 40, "bold"), bg="yellow",
                      fg="red")
        title.pack(side=TOP, fill=X)
        # =================All variables===================#
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_text = StringVar()

        ######################### Manage_Frame #######################################
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Manage_Frame.place(x=20, y=100, width=450, height=580)

        m_title = Label(Manage_Frame, text="Manage Students", bg="crimson", fg="white",
                        font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, padx=20, sticky="w")

        text_roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        text_roll.grid(row=1, column=1, pady=10, padx=20, sticky="w")

        lbl_name = Label(Manage_Frame, text="Name", bg="crimson", fg="white",
                         font=("times new roman", 20, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, padx=20, sticky="w")

        text_name = Entry(Manage_Frame, textvariable=self.name_var, font=("times new roman", 15, "bold"), bd=5,
                          relief=GROOVE)
        text_name.grid(row=2, column=1, pady=10, padx=20, sticky="w")

        lbl_email = Label(Manage_Frame, text="Email_id", bg="crimson", fg="white",
                          font=("times new roman", 20, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, padx=20, sticky="w")

        text_email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), bd=5,
                           relief=GROOVE)
        text_email.grid(row=3, column=1, pady=10, padx=20, sticky="w")

        lbl_gender = Label(Manage_Frame, text="Gender", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, padx=20, sticky="w")

        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"),
                                    state='readonly')
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20, sticky='w')

        lbl_contact = Label(Manage_Frame, text="Contact", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, padx=20, sticky="w")

        text_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), bd=5,
                             relief=GROOVE)
        text_contact.grid(row=5, column=1, pady=10, padx=20, sticky="w")

        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="crimson", fg="white",
                        font=("times new roman", 20, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, padx=20, sticky="w")

        text_dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), bd=5,
                         relief=GROOVE)
        text_dob.grid(row=6, column=1, pady=10, padx=20, sticky="w")

        lbl_address = Label(Manage_Frame, text="Address", bg="crimson", fg="white",
                            font=("times new roman", 20, "bold"))
        lbl_address.grid(row=7, column=0, pady=10, padx=20, sticky="w")

        self.text_address = Text(Manage_Frame, width=30, height=4, font=("", 10))
        self.text_address.grid(row=7, column=1, pady=10, padx=20, sticky="w")

        ######################### Button_Frame########################################
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="crimson")
        btn_Frame.place(x=15, y=500, width=420)

        add_btn = Button(btn_Frame, text="Add", width=10, command=self.add_student).grid(row=0, column=0, padx=10,
                                                                                         pady=10)
        update_btn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=10,
                                                                                               pady=10)
        delete_btn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=10,
                                                                                               pady=10)
        clear_btn = Button(btn_Frame, text="Clear", command=self.clear(), width=10).grid(row=0, column=3, padx=10,
                                                                                         pady=10)

        ######################### Detail_Frame #######################################
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="crimson")
        Detail_Frame.place(x=500, y=100, width=800, height=580)

        lbl_search = Label(Detail_Frame, text="Search By", bg="crimson", fg="white",
                           font=("times new roman", 20, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")

        combo_search = ttk.Combobox(Detail_Frame, textvariable=self.search_by, font=("times new roman", 13, "bold"),
                                    state='readonly', width=10)
        combo_search['values'] = ("RollNo", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20, sticky='w')

        text_search = Entry(Detail_Frame, textvariable=self.search_text, width=15, font=("times new roman", 15, "bold"),
                            bd=5, relief=GROOVE)
        text_search.grid(row=0, column=2, pady=10, padx=20, sticky="w")

        search_btn = Button(Detail_Frame, text="Search", width=10, command=self.search_data, pady=5).grid(row=0,
                                                                                                          column=3,
                                                                                                          padx=10,
                                                                                                          pady=10)
        show_btn = Button(Detail_Frame, text="Show All", width=10, command=self.show_all, pady=5).grid(row=0,
                                                                                                       column=4,
                                                                                                       padx=10,
                                                                                                       pady=10)

        ######################## Table_Frame #########################################
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="crimson")
        Table_Frame.place(x=10, y=70, width=760, height=500)

        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)
        self.Student_Table = ttk.Treeview(Table_Frame,
                                          columns=("RollNo", "Name", "Email_id", "Gender", "Contact", "DOB", "Address"),
                                          xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.Student_Table.xview)
        scroll_y.config(command=self.Student_Table.yview)
        self.Student_Table.heading("RollNo", text="Roll No")
        self.Student_Table.heading("Name", text="Name")
        self.Student_Table.heading("Email_id", text="Email_id")
        self.Student_Table.heading("Gender", text="Gender")
        self.Student_Table.heading("Contact", text="Contact")
        self.Student_Table.heading("DOB", text="D.O.B")
        self.Student_Table.heading("Address", text="Address")
        self.Student_Table['show'] = "headings"
        self.Student_Table.column("RollNo", width=100)
        self.Student_Table.column("Name", width=100)
        self.Student_Table.column("Email_id", width=100)
        self.Student_Table.column("Gender", width=100)
        self.Student_Table.column("Contact", width=100)
        self.Student_Table.column("DOB", width=100)
        self.Student_Table.column("Address", width=150)
        self.Student_Table.pack(fill=BOTH, expand=1)
        self.Student_Table.bind("<ButtonRelease-1>", self.get_cursor)
        self.show_all()
        ######################################## database connectivity###############################################

    def add_student(self):
        if self.Roll_No_var.get() == "" or self.name_var == "" or self.dob_var == "" or self.gender_var == "":
            messagebox.showerror("Error", "All fields are required!!")
        else:
            cur.execute('insert into Student values(?,?,?,?,?,?,?)', (self.Roll_No_var.get(),
                                                                      self.name_var.get(),
                                                                      self.email_var.get(),
                                                                      self.gender_var.get(),
                                                                      self.contact_var.get(),
                                                                      self.dob_var.get(),
                                                                      self.text_address.get('1.0', END)
                                                                      ))
            self.show_all()
            self.clear()

    def show_all(self):
        cur.execute('select * from Student')
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)

    def clear(self):
        self.Roll_No_var.set('')
        self.name_var.set('')
        self.email_var.set('')
        self.gender_var.set('')
        self.contact_var.set('')
        self.dob_var.set('')
        self.text_address.delete('1.0', END)

    def get_cursor(self, ev):
        cursor_row = self.Student_Table.focus()
        contents = self.Student_Table.item(cursor_row)
        rowx = contents['values']
        self.Roll_No_var.set(rowx[0])
        self.name_var.set(rowx[1])
        self.email_var.set(rowx[2])
        self.gender_var.set(rowx[3])
        self.contact_var.set(rowx[4])
        self.dob_var.set(rowx[5])
        self.text_address.delete('1.0', END)
        self.text_address.insert(END, rowx[6])

    def update_data(self):
        cur.execute('update Student set name=?,email=?,gender=?,contact=?,dob=?,address=? where Rollno=?', (
            self.name_var.get(),
            self.email_var.get(),
            self.gender_var.get(),
            self.contact_var.get(),
            self.dob_var.get(),
            self.text_address.get('1.0', END),
            self.Roll_No_var.get()
        ))
        self.show_all()
        self.clear()

    def delete_data(self):
        cur.execute("delete from Student where Rollno=?", (self.Roll_No_var.get(),))
        self.show_all()
        self.clear()

    def search_data(self):
        cur.execute(
            "select * from Student where " + str(self.search_by.get()) + " LIKE '%" + str(
                self.search_text.get()) + "%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_Table.delete(*self.Student_Table.get_children())
            for row in rows:
                self.Student_Table.insert('', END, values=row)


root = Tk()
ob = Student(root)
root.mainloop()
db.commit()
db.close()
