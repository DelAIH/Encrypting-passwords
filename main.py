import cipher # Модуль шифрования

сhoice = int(input('Выберите шифрование или дешифрование 1/2 :'))

if сhoice == 1:
	password = input('Введите пароль: ')
	a = cipher.Cipher(password)
	print('Результат шифрования: ', a)

elif сhoice == 2:
	password = input('Введите пароль для дешифрования: ')
	a = cipher.Cipher(password)
	print('Результа дешифрования: ', a)

else:
	print('Введите повторно')
