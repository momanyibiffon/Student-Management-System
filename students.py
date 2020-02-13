from tkinter import *
from tkinter import ttk
import pymysql
from tkinter import messagebox


class Student:
    def __init__(self, root):
        self.root = root
        self.root.title("Student Management System")
        self.root.geometry("1350x700+0+0")

        title = Label(self.root, text="Student Management System",
                      font=("times new roman", 30, "bold"), bg="navy",
                      fg="white", bd=10, relief=GROOVE)
        title.pack(side=TOP, fill=X)

        # ===All variables===
        self.Roll_No_var = StringVar()
        self.name_var = StringVar()
        self.email_var = StringVar()
        self.gender_var = StringVar()
        self.contact_var = StringVar()
        self.dob_var = StringVar()

        self.search_by = StringVar()
        self.search_txt = StringVar()

        #  ===== Manage frame======
        Manage_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="lavender")
        Manage_Frame.place(x=20, y=100, width=425, height=550)

        m_title = Label(Manage_Frame, text="Manage Students", bg="lavender", font=("times new roman", 20, "bold"))
        m_title.grid(row=0, columnspan=2, pady=20)

        lbl_roll = Label(Manage_Frame, text="Roll No.", bg="lavender", font=("times new roman", 15, "bold"))
        lbl_roll.grid(row=1, column=0, pady=10, sticky="W")
        txt_roll = Entry(Manage_Frame, textvariable=self.Roll_No_var, font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_roll.grid(row=1, column=1, pady=10, padx=10)

        lbl_name = Label(Manage_Frame, text="Name", bg="lavender", font=("times new roman", 15, "bold"))
        lbl_name.grid(row=2, column=0, pady=10, sticky="W")
        txt_name = Entry(Manage_Frame, textvariable=self.name_var , font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_name.grid(row=2, column=1, pady=10, padx=10)

        lbl_email = Label(Manage_Frame, text="Email", bg="lavender", font=("times new roman", 15, "bold"))
        lbl_email.grid(row=3, column=0, pady=10, sticky="W")
        txt_email = Entry(Manage_Frame, textvariable=self.email_var, font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_email.grid(row=3, column=1, pady=10, padx=10)

        lbl_gender = Label(Manage_Frame, text="Gender", bg="lavender", font=("times new roman", 15, "bold"))
        lbl_gender.grid(row=4, column=0, pady=10, sticky="W")
        combo_gender = ttk.Combobox(Manage_Frame, textvariable=self.gender_var, font=("times new roman", 13, "bold"), state="readonly")
        combo_gender['values'] = ("Male", "Female", "Other")
        combo_gender.grid(row=4, column=1, pady=10, padx=20)

        lbl_contact = Label(Manage_Frame, text="Contact", bg="lavender", font=("times new roman", 15, "bold"))
        lbl_contact.grid(row=5, column=0, pady=10, sticky="W")
        txt_contact = Entry(Manage_Frame, textvariable=self.contact_var, font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_contact.grid(row=5, column=1, pady=10, padx=10)

        lbl_dob = Label(Manage_Frame, text="D.O.B", bg="lavender", font=("times new roman", 15, "bold"))
        lbl_dob.grid(row=6, column=0, pady=10, sticky="W")
        txt_dob = Entry(Manage_Frame, textvariable=self.dob_var, font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_dob.grid(row=6, column=1, pady=10, padx=10)

        lbl_address = Label(Manage_Frame, text="Address", bg="lavender", font=("times new roman", 15, "bold"))
        lbl_address.grid(row=7, column=0, pady=20, sticky="W")
        self.txt_address = Text(Manage_Frame, width=25, height=4)
        self.txt_address.grid(row=7, column=1, pady=10, padx=10)

        # === Button Frame ===
        btn_Frame = Frame(Manage_Frame, bd=4, relief=RIDGE, bg="lavender")
        btn_Frame.place(x=5, y=460, width=405)

        AddBtn = Button(btn_Frame, text="Save", width=10, command=self.add_students).grid(row=0, column=0, padx=5, pady=10)
        UpdateBtn = Button(btn_Frame, text="Update", width=10, command=self.update_data).grid(row=0, column=1, padx=5, pady=10)
        DeleteBtn = Button(btn_Frame, text="Delete", width=10, command=self.delete_data).grid(row=0, column=2, padx=5, pady=10)
        ClearBtn = Button(btn_Frame, text="Clear", width=10, command=self.clear).grid(row=0, column=3, padx=10, pady=10)


        # === Detail Frame===
        Detail_Frame = Frame(self.root, bd=4, relief=RIDGE, bg="lavender")
        Detail_Frame.place(x=450, y=100, width=800, height=550)

        lbl_search = Label(Detail_Frame, text="Search By", bg="lavender", font=("times new roman", 15, "bold"))
        lbl_search.grid(row=0, column=0, pady=10, padx=20, sticky="w")
        combo_search = ttk.Combobox(Detail_Frame, width=10, textvariable=self.search_by, font=("times new roman", 13, "bold"), state="readonly")
        combo_search['values'] = ("Roll_no", "Name", "Contact")
        combo_search.grid(row=0, column=1, pady=10, padx=20)

        txt_search = Entry(Detail_Frame, width=15, textvariable=self.search_txt ,font=("times new roman", 15, "bold"), relief=GROOVE)
        txt_search.grid(row=0, column=2, pady=10, padx=10)

        SearchBtn = Button(Detail_Frame, text="Search", width=10, pady=5, command=self.search_data).grid(row=0, column=3, padx=10, pady=10)
        ShowAllBtn = Button(Detail_Frame, text="Show All", width=10, pady=5, command=self.fetch_data).grid(row=0, column=4, padx=10, pady=10)

        # === Table Frame ===
        Table_Frame = Frame(Detail_Frame, bd=4, relief=RIDGE, bg="lavender")
        Table_Frame.place(x=10, y=70, width=772, height=450)

        # scroll bars
        scroll_x = Scrollbar(Table_Frame, orient=HORIZONTAL)
        scroll_y = Scrollbar(Table_Frame, orient=VERTICAL)

        # table
        self.Student_table = ttk.Treeview(Table_Frame, columns=("roll", "name", "email", "gender", "contact", "dob",
                                                           "Address"), xscrollcommand=scroll_x.set,
                                     yscrollcommand=scroll_y.set)
        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)

        scroll_x.config(command=self.Student_table.xview)
        scroll_y.config(command=self.Student_table.yview)

        # table headings
        self.Student_table.heading("roll", text="Roll No.")
        self.Student_table.heading("name", text="Name")
        self.Student_table.heading("email", text="Email")
        self.Student_table.heading("gender", text="Gender")
        self.Student_table.heading("contact", text="Contact")
        self.Student_table.heading("dob", text="D.O.B")
        self.Student_table.heading("Address", text="Address")
        self.Student_table['show'] = 'headings'

        # table column widths
        self.Student_table.column("roll", width=105)
        self.Student_table.column("name", width=105)
        self.Student_table.column("email", width=105)
        self.Student_table.column("gender", width=105)
        self.Student_table.column("contact", width=105)
        self.Student_table.column("dob", width=105)
        self.Student_table.column("Address", width=105)
        self.Student_table.pack(fill=BOTH, expand=1)
        self.Student_table.bind("<ButtonRelease-1>", self.get_cursor)
        self.fetch_data()

    # ===method adding students to the database===
    def add_students(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or \
                self.gender_var.get() == "" or self.contact_var.get() == "" or self.dob_var.get() == "" or \
                self.txt_address.get('1.0', END) == "":
            messagebox.showerror("Error", "All fields are required!")

        else:
            con = pymysql.connect(host="localhost", user="root", password="", database="student_management")

            cur2 = con.cursor()
            cur2.execute("SELECT * FROM students WHERE roll_no=%s", (self.Roll_No_var.get()))
            row_count = cur2.rowcount
            if row_count > 0:
                messagebox.showerror("ERROR", "Student Roll Number "+self.Roll_No_var.get()+" is invalid or already exists")
            else:
                cur = con.cursor()
                cur.execute("insert into students values(%s,%s,%s,%s,%s,%s,%s)", (self.Roll_No_var.get(),
                                                                                  self.name_var.get(),
                                                                                  self.email_var.get(),
                                                                                  self.gender_var.get(),
                                                                                  self.contact_var.get(),
                                                                                  self.dob_var.get(),
                                                                                  self.txt_address.get('1.0', END)
                                                                                  ))

                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success", "Record has been inserted")

    # ===fetching data===
    def fetch_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management")
        cur = con.cursor()
        cur.execute("select * from students")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()

    # === clearing all fields ===
    def clear(self):
        confirm = messagebox.askquestion("Confirm", " Do you want to clear all fields?")
        if confirm == 'yes':
            self.Roll_No_var.set("")
            self.name_var.set("")
            self.email_var.set("")
            self.gender_var.set("")
            self.contact_var.set("")
            self.dob_var.set("")
            self.txt_address.delete("1.0", END)

    # === getting clicked row to be edited ===
    def get_cursor(self, ev):
        cursor_row = self.Student_table.focus()
        contents = self.Student_table.item(cursor_row)
        row = contents['values']
        # === auto filling fields ===
        self.Roll_No_var.set(row[0])
        self.name_var.set(row[1])
        self.email_var.set(row[2])
        self.gender_var.set(row[3])
        self.contact_var.set(row[4])
        self.dob_var.set(row[5])
        self.txt_address.delete("1.0", END)
        self.txt_address.insert(END, row[6])

    # ===updating data===
    def update_data(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or \
                self.gender_var.get() == "" or self.contact_var.get() == "" or self.dob_var.get() == "" or \
                self.txt_address.get('1.0', END) == "":
            messagebox.showinfo("Warning", "All fields are required while updating")
        else:
            confirm = messagebox.askquestion("Confirm", "Do you want to update this record?")
            if confirm == 'yes':
                con = pymysql.connect(host="localhost", user="root", password="", database="student_management")
                cur = con.cursor()
                cur.execute("update students set name=%s, email=%s,gender=%s,contact=%s, dob=%s, address=%s where roll_no=%s", (
                                                                                  self.name_var.get(),
                                                                                  self.email_var.get(),
                                                                                  self.gender_var.get(),
                                                                                  self.contact_var.get(),
                                                                                  self.dob_var.get(),
                                                                                  self.txt_address.get('1.0', END),
                                                                                  self.Roll_No_var.get()
                                                                                  ))
                con.commit()
                self.fetch_data()
                self.clear()
                con.close()
                messagebox.showinfo("Success", "Record successfully updated")
            else:
                messagebox.showinfo("Information", "Record not updated")

    def delete_data(self):
        if self.Roll_No_var.get() == "" or self.name_var.get() == "" or self.email_var.get() == "" or \
                self.gender_var.get() == "" or self.contact_var.get() == "" or self.dob_var.get() == "" or \
                self.txt_address.get('1.0', END) == "":
            messagebox.showinfo("Warning", "No record selected")
        else:
            confirm = messagebox.askquestion("Confirm", "Are you sure you want to delete this record?")
            if confirm == 'yes':
                con = pymysql.connect(host="localhost", user="root", password="", database="student_management")
                cur = con.cursor()
                cur.execute("delete from students where roll_no=%s", self.Roll_No_var.get())
                con.commit()
                con.close()
                self.fetch_data()
                self.clear()
                messagebox.showinfo("Success", "One record has been deleted")

    # ===searching data===
    def search_data(self):
        con = pymysql.connect(host="localhost", user="root", password="", database="student_management")
        cur = con.cursor()
        cur.execute("select * from students where "+str(self.search_by.get())+" LIKE '%"+str(self.search_txt.get())+"%'")
        rows = cur.fetchall()
        if len(rows) != 0:
            self.Student_table.delete(*self.Student_table.get_children())
            for row in rows:
                self.Student_table.insert('', END, values=row)
            con.commit()
        con.close()


root = Tk()
ob = Student(root)
root.mainloop()
