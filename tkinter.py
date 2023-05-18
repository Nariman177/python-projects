from tkinter import*

def button_press():
    print("Welcome to the school")

def button_pre():
    print("Welcome")

root = Tk()
root.title("school managment system")
root.geometry("500x500")
btn = Button(root, text = "На Русском", background = "#555", command = button_press)
btn1 = Button(root, text = "На Казахском", background = "#555", command = button_pre)
btn2 = Button(root, text = "English", background = "#555", command = button_press)
btn.pack()
btn1.pack()
btn2.pack()
root.mainloop()



