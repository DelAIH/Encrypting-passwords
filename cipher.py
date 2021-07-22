# Модуль шифрования

def Cipher(b):
	list_cipher = []
	for i in b:
		
		# Шифрует числа
		if i == "1":
			list_cipher.append('2')
		elif i == '2':
			list_cipher.append('1')
		elif i == '3':
			list_cipher.append('4')
		elif i == '4':
			list_cipher.append('3')	
		elif i == '5':
			list_cipher.append('6')
		elif i == '6':
			list_cipher.append('5')
		elif i == '7':
			list_cipher.append('8')
		elif i == '8':
			list_cipher.append('7')
		elif i == '9':
			list_cipher.append('0')
		elif i == '0':
			list_cipher.append('9')
			
		# Шифрует большие буквы
		elif i == 'A':
			list_cipher.append('D')
		elif i == 'B':
			list_cipher.append('E')
		elif i == 'C':
			list_cipher.append('F')
		elif i == 'D':
			list_cipher.append('A')
		elif i == 'E':
			list_cipher.append('B')
		elif i == 'F':
			list_cipher.append('C')
		elif i == 'G':
			list_cipher.append('I')
		elif i == 'H':
			list_cipher.append('J')	
		elif i == 'I':
			list_cipher.append('G')	
		elif i == 'J':
			list_cipher.append('H')
		elif i == 'K':
			list_cipher.append('M')
		elif i == 'L':
			list_cipher.append('J')
		elif i == 'M':
			list_cipher.append('K')
		elif i == 'N':
			list_cipher.append('L')
		elif i == 'O':
			list_cipher.append('Q')
		elif i == 'P':
			list_cipher.append('R')
		elif i == 'Q':
			list_cipher.append('O')	
		elif i == 'R':
			list_cipher.append('P')
		elif i == 'S':
			list_cipher.append('U')	
		elif i == 'T':
			list_cipher.append('V')	
		elif i == 'U':
			list_cipher.append('S')
		elif i == 'V':
			list_cipher.append('T')	
		elif i == 'W':
			list_cipher.append('Y')	
		elif i == 'X':
			list_cipher.append('Z')	
		elif i == 'Y':
			list_cipher.append('W')	
		elif i == 'Z':
			list_cipher.append('X')	
		
		# Шифрует маленькие буквы
		elif i == 'a':
			list_cipher.append('d')
		elif i == 'b':
			list_cipher.append('e')	
		elif i == 'c':
			list_cipher.append('f')	
		elif i == 'd':
			list_cipher.append('a')	
		elif i == 'e':
			list_cipher.append('b')	
		elif i == 'f':
			list_cipher.append('c')	
		elif i == 'g':
			list_cipher.append('i')	
		elif i == 'h':
			list_cipher.append('j')	
		elif i == 'k':
			list_cipher.append('m')	
		elif i == 'l':
			list_cipher.append('n')	
		elif i == 'm':
			list_cipher.append('k')	
		elif i == 'n':
			list_cipher.append('l')	
		elif i == 'o':
			list_cipher.append('q')	
		elif i == 'p':
			list_cipher.append('r')	
		elif i == 'q':
			list_cipher.append('o')	
		elif i == 'r':
			list_cipher.append('p')	
		elif i == 's':
			list_cipher.append('u')	
		elif i == 't':
			list_cipher.append('v')	
		elif i == 'u':
			list_cipher.append('s')	
		elif i == 'v':
			list_cipher.append('t')	
		elif i == 'w':
			list_cipher.append('y')	
		elif i == 'x':
			list_cipher.append('z')	
		elif i == 'y':
			list_cipher.append('w')	
		elif i == 'z':
			list_cipher.append('x')	
		
		# Знаки
		elif i == '_':
			list_cipher.append('-')
		elif i == '-':
			list_cipher.append('_')	
			
		
	b = ''.join(list_cipher)
	return b
