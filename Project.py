import tkinter as tk

root = tk.Tk()
text=tk.StringVar()

def clickme():
	x= int(enter_1.get()) * 1.8 + 32
	text.set('')
	enter_2.insert(0,x)

lbl_title = tk.Label(root, fg='white',bg='black', text="Temperature Converter")
lbl_celsius = tk.Label(root,fg='blue', text="Celsius")
lbl_fahrenheit = tk.Label(root,fg='red', text="Fahrenheit")


button_convert=tk.Button(root,fg='white', bg='black', text="Convert", command=clickme) 

enter_1=tk.Entry(root,fg='blue', font=('arial', 10, 'bold'))
enter_2=tk.Entry(root, textvar=text,fg='red' , font=('arial', 10, 'bold'))

lbl_title.grid(row=1, column=2)
lbl_celsius.grid(row=2, column=1)
lbl_fahrenheit.grid(row=2, column=3)
button_convert.grid(row=3, column=2)
enter_1.grid(row=3, column=1)
enter_2.grid(row=3, column=3)













tk.mainloop()