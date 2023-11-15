import tkinter as tk
from tkinter import messagebox

# call this when Submit is clicked
def submit_action():
    messagebox.showinfo(title="Registration successfull!!", message="Yess!!")

# create a window
root = tk.Tk()
root.title("Student Registration form")

# name
name_label = tk.Label(root, text="Student name")
name_label.pack()
name = tk.Entry(root)
name.pack()

# age
age_label = tk.Label(root, text="Student age")
age_label.pack()
age = tk.Entry(root)
age.pack()

## gender

# gender label
gender_label = tk.Label(root, text="Gender")
gender_label.pack()
# gender variable
gender = tk.StringVar()
gender.set("Male") # default value
# male button
male = tk.Radiobutton(root, text="Male", variable=gender, value="Male")
male.pack()
# female button
female = tk.Radiobutton(root, text="Female", variable=gender, value="Female")
female.pack()

## course
#course label
course_label = tk.Label(root, text="Course")
course_label.pack()
# course variable
course_list = ["BCA", "BBA", "BE"]
course = tk.StringVar()
course.set(course_list[0]) # default value
#dropdown
course_menu = tk.OptionMenu(root, course, *course_list)
course_menu.pack()

# submit button
submit = tk.Button(root, text="Submit", command=submit_action)
submit.pack()

# open the created window
root.mainloop()

