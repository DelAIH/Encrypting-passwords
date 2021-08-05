from tkinter import*

window = Tk()
window.geometry('300x150')

def clicked():
	name = ent.get()
	ent1.insert(0, name)
  
  
lbl = Label(
	text="Пароль",
	width=20
	)

ent = Entry(
	width=20
	)


	
btn = Button(
	text='Ввод',
	width=20,
	command = clicked
	)

ent1 = Entry(
	width=20
	)

lbl.pack()
ent.pack()
btn.pack()
ent1.pack()

window.mainloop()
