from tkinter import*

window = Tk()
window.geometry('268x70')
window.title('DelAIH')
def clicked():
	name = ent.get()
	ent2.insert(0, name)
  
lbl = Label(window, text="Пароль:", width=8)
ent = Entry(window, width = 20)
btn = Button(window, text = 'Ввод',width = 10,command = clicked, fg='white', bg='black')
ent2 = Entry(window, width = 20)
lbl2 = Label(window, text="Результат:", width=8)

lbl.grid(row=0, column=0)
ent.grid(row=0, column=1)
btn.grid(row=0, column=2)
ent2.grid(row=1, column=1)
lbl2.grid(row=1, column=0)

window.mainloop()
