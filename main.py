from tkinter import* # модуль Tkinter
import cipher # Модуль шифрования

def Main():
	
	window = Tk()
	window.geometry('268x70')
	window.title('DelAIH')
	
	def clicked():
		password_cipher = ent.get()
		password_encryption = cipher.Cipher(password_cipher) # шифруется пароль
		ent2.insert(0, password_encryption)
	  
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


if __name__ == "__main__":
	Main()
