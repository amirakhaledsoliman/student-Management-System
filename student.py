import tkinter as tk
import tkinter as tk
from tkinter import messagebox
import csv
import os

class student:
    def __init__(self, master):
        
        self.master = master
        self.master.title("student Management System")
        self.master.geometry("600x600")
        self.master.config(bg='#708090')
        self .subject=[]
        self.stu = []
         # Labels
        self.login_label = tk.Label(self.master, text="student Management System", font=("Helvetica", 16), bg='#708090', fg='white')
        self.login_label.pack()
        self.username_label = tk.Label(self.master, text="Username", font=("Helvetica", 12), bg='#708090', fg='white')
        self.username_label.pack()
        self.username_entry = tk.Entry(self.master, font=("Helvetica", 12))
        self.username_entry.pack()
        self.password_label = tk.Label(self.master, text="Password", font=("Helvetica", 12), bg='#708090', fg='white')
        self.password_label.pack()
        self.password_entry = tk.Entry(self.master, font=("Helvetica", 12), show="*")
        self.password_entry.pack()
         # Login
        self.login_button = tk.Button(self.master, text="Login", command=self.login, font=("Helvetica", 12))
        self.login_button.pack()
    def login(self):
            if self.username_entry.get()=="" or self.password_entry.get()=="":
             messagebox.showerror("Error", "Invalid username or password")
            elif self.username_entry.get()=="111" and self.password_entry.get()=="111":
                 self.username_entry.delete(0, tk.END)
                 self.password_entry.delete(0, tk.END)
                 self.login_label.destroy()
                 self.username_label.destroy()
                 self.username_entry.destroy()
                 self.password_label.destroy()
                 self.password_entry.destroy()
                 self.login_button.destroy()
                 self.screen()
                 return
            else :
                 messagebox.showerror("error","plz enter pass or username again")
    def screen(self):         

            self.name = tk.Label(self.master, text="studestudent's name", font=("Helvetica", 16), bg='#708090', fg='white')
            self.name.grid(row=1, column=0, padx=10, pady=10)
            self.name = tk.Entry(self.master, font=("Helvetica", 12))
            self.name.grid(row=1, column=1, padx=10, pady=10)

            self. id = tk.Label(self.master, text="student's ID", font=("Helvetica", 16), bg='#708090', fg='white')
            self. id.grid(row=2, column=0, padx=10, pady=10)
            self. id= tk.Entry(self.master, font=("Helvetica", 12))
            self. id.grid(row=2, column=1, padx=10, pady=10)

            self.email = tk.Label(self.master, text="student's Email", font=("Helvetica", 16), bg='#708090', fg='white')
            self.email.grid(row=3, column=0, padx=10, pady=10)
            self.email= tk.Entry(self.master, font=("Helvetica", 12))
            self.email.grid(row=3, column=1, padx=10, pady=10)

            self.phone = tk.Label(self.master, text="phone number", font=("Helvetica", 16), bg='#708090', fg='white')
            self.phone.grid(row=4, column=0, padx=10, pady=10)
            self.phone= tk.Entry(self.master, font=("Helvetica", 12))
            self.phone.grid(row=4, column=1, padx=10, pady=10)

            self.sub = tk.Label(self.master, text="subject", font=("Helvetica", 16), bg='#708090', fg='white')
            self.sub.grid(row=5, column=0, padx=10, pady=10)
            self.sub= tk.Entry(self.master, font=("Helvetica", 12))
            self.sub.grid(row=5, column=1, padx=10, pady=10)


        # Buttons

            self.add_stu_button = tk.Button(self.master, text="Add student", command= self.Add_student, font=("Helvetica", 12))
            self.add_stu_button.grid(row=6, column=0, padx=10, pady=10)
            
            self.add_button = tk.Button(self.master, text="Add subject", command= self. Add_subject, font=("Helvetica", 12))
            self.add_button.grid(row=6, column=1, padx=10, pady=10)

            self.grd_button = tk.Button(self.master, text="Student Grade", command=self. Student_Grade, font=("Helvetica", 12))
            self. grd_button.grid(row=7, column=0, padx=10, pady=10)

           


    def Add_student(self):
        self.namea=  self.name.get()
        self. ida = self. id.get()
        self.emaila = self.email.get()
        self.phonea=self.phone.get()
        self.studenta=self.name.get()+self. id.get()+self.email.get()+self.phone.get()  
        if self.namea == "" or  self. ida  == "" or self.emaila == "" or self.phonea=="" :
          messagebox.showerror("Error","Please fill all the fields")
        else:   
         with open("student", "a", newline="") as file:
           writer = csv.writer(file)
           writer.writerow([self.namea,self. ida ,self.emaila,self.phonea])
         messagebox.showinfo("Success", "student added successfully!")
        
         self.sub.delete(0,END)
         self.name.delete(0, END)
         self.id.delete(0, END)
         self.email.delete(0, END) 
         self.phone.delete(0, END)
        
    def Add_subject(self):
         self.suba=  self.sub.get()
         if self.sub==" ":
               messagebox.showerror("Error")
         else:
          self .subject.append( self.suba)
         messagebox.showinfo("Success", "subject added successfully")
         message = "\n".join(self .subject)
         messagebox.showinfo("subject", message)
         self.sub.delete(0, tk.END)


    def Student_Grade(self):
        root=tk.Tk()
        self.root = root
        self.root.title(" grad student")
        self.root.geometry("400x400")
        self.root.config(bg='#708090')

        self.sub1 = tk.Label(self.root, text="english", font=("Helvetica", 16), bg='#708090', fg='white')
        self.sub1.grid(row=1, column=0, padx=10, pady=10)
        self.sub1 = tk.Entry(self.root, font=("Helvetica", 12))
        self.sub1.grid(row=1, column=1, padx=10, pady=10)

        self.sub2 = tk.Label(self.root, text="math", font=("Helvetica", 16), bg='#708090', fg='white')
        self.sub2.grid(row=2, column=0, padx=10, pady=10)
        self.sub2 = tk.Entry(self.root, font=("Helvetica", 12))
        self.sub2.grid(row=2, column=1, padx=10, pady=10)

        self.sub3 = tk.Label(self.root, text="physics ", font=("Helvetica", 16), bg='#708090', fg='white')
        self.sub3.grid(row=3, column=0, padx=10, pady=10)
        self.sub3 = tk.Entry(self.root, font=("Helvetica", 12))
        self.sub3.grid(row=3, column=1, padx=10, pady=10)

        self.t = tk.Label(self.root, text="total", font=("Helvetica", 16), bg='#708090', fg='white')
        self.t.grid(row=4, column=0, padx=10, pady=10)

        self.g = tk.Label(self.root, text="grad", font=("Helvetica", 16), bg='#708090', fg='white')
        self.g.grid(row=6, column=0, padx=10, pady=10)

        self.a = tk.Label(self.root, text="GPA", font=("Helvetica", 16), bg='#708090', fg='white')
        self.a.grid(row=7, column=0, padx=10, pady=10)

        self.ava = tk.Label(self.root, text="avarge", font=("Helvetica", 16), bg='#708090', fg='white')
        self.ava.grid(row=5, column=0, padx=10, pady=10)

        self.calculatio_button = tk.Button(self.root, text="calculatiot", command=self.calculation, font=("Helvetica", 12))
        self.calculatio_button.grid(row=8, column=1, padx=10, pady=10)
    def calculation(self):
            self.englis=int(self.sub1.get())
            self.math=int(self.sub2.get())
            self.arabic=int(self.sub3.get())

            self.totall=(self.englis +self.math+self.arabic)
            self.total=tk.Label(self.root, text=f"{self.totall}", font=("Helvetica", 16), bg='#708090', fg='white')
            self.total.grid(row=4, column=1, padx=10, pady=10)

            self.aval=int(self.totall/3)
            self.aval=tk.Label(self.root, text=f"{self.aval}", font=("Helvetica", 16), bg='#708090', fg='white')
            self.aval.grid(row=5, column=1, padx=10, pady=10)
            self.gr=" "
            if (self.aval>50):
                 self.gr="pass"
            else:
                 self.g="fail"
            self.gg=tk.Label(self.root, text=f"{ self.gr}", font=("Helvetica", 16), bg='#708090', fg='white')
            self.gg.grid(row=6, column=1, padx=10, pady=10)

           







       


    
if __name__ == "__main__":
    root = tk.Tk()
    app = student(root)
    root.mainloop()   
    
    
