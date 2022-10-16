
from tkinter import *
import random
root=Tk()

root.title("TESTING RANDOM FUNCTION")
root.geometry("500x500")

input_password_GUI = Entry(root)
guessed_passward_GUI_label = Label(root)
generated_passward_GUI_label= Label(root)

array_3d = [[["IronMan","SpiderMan","CaptainAmerica"],["$","*","&"],["Fan","DieHeartFan","UltraDieHeartFan"]]]
print(array_3d[0][2][1])

def new_password(): 
    guessed_passward_label["text"] = "Guessed Password: " + input_password.get()
    
    r1 = random.randint(0,2)
    r2 = random.randint(0,2)
    r3 = random.randint(0,2)
    
    letter1 = array_3d[0][0][r1]
    letter2 = array_3d[0][1][r2]
    letter3 = array_3d[0][2][r3]
    
    generated_passward_label["text"] = "Generated Password: " + letter1 + "" + letter2 + "" + letter3
    
    
input_password_GUI.place(relx = 0.5, rely =0.3, anchor = CENTER)

guessed_passward_GUI_label.place(relx = 0.5, rely =0.4, anchor = CENTER)

btn = Button(root, text= "new password", command = new_password)
btn.place(relx = 0.5, rely =0.5, anchor = CENTER)

generated_passward_GUI_label.place(relx = 0.5, rely =0.7, anchor = CENTER)
root.mainloop()
