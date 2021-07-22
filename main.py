import cipher # Модуль шифрования

# Ввод пароля
password = input('Введите пароль: ')

a = cipher.Cipher(password)
print(a) 
