import sys, binascii

def writeTextFile(filename, textData):
	with open(filename, 'w',encoding='utf-8') as f:
		f.write(textData)


def readTextFile(filename):
	with open(filename, 'r',encoding='utf-8') as f:
		textData = f.read()
	return textData


def writeHexFile(filename, hexData):
	with open(filename, 'wb') as f:
		f.write(hexData)


def readHexFile(filename):
	with open(filename, 'rb') as f:
		hexData = f.read()
	return hexData


def bytesToHex(bArray):
	return binascii.hexlify(bArray)


def hexToBytes(hexData):
	return binascii.unhexlify(hexData)


def getText(bArray):
	lst = []
	for i in range(len(bArray)):
		if 0<bArray[i]<9 or 9<bArray[i]<13 or 13<bArray[i]<32:
			lst.append('.')
		elif bArray[i]==9 or bArray[i]==13:
			lst.append(' ')
		else:
			lst.append(chr(bArray[i]))
	return lst


def show(hexData, textData, **kwargs):
	if len(hexData)==2*len(textData):
		for key, value in kwargs.items():
			if key=='characters':
				characters = value
			elif key=='view':
				view = value
		k=0
		while k*characters<len(hexData)//2:
			start = k * characters
			end = min((k + 1) * characters, len(hexData))
			byte = []
			string =[e.replace('\n',' ').replace('\r', ' ').replace('\b','') for e in textData[start: end]]
			if view == 'B':
				for i in  range(start*2,end*2,2):
					byte.append(hexData[i:i+2])
			elif view== 'b':
				for i in  range(start*2,end*2,2):
					if hexData[i:i+2] != '':
						byte.append(bin(int(hexData[i:i+2], 16))[2:].zfill(8))
					else:
						byte.append(' '*8)
			elif view== 'd':
				for i in  range(start*2,end*2,2):
					if hexData[i:i+2] != '':
						byte.append(str(int(hexData[i:i+2], 16)).zfill(3))
					else:
						byte.append(' '*3)
			
			print('{}\t\t{}'.format(' '.join(e for e in byte),''.join(e for e in string)))
			k+=1
	else:
		raise Exception('Длина байтов != 2 * длина символов')


def run(args):
	filename=''
	characters=16
	view = 'B'
	plain=False
	plainFile=''
	reverse=False
	reverseFile=''
	i=0
	while i <len(args):
		arg = args[i]
		if arg == '-f':
			try:
				filename = args[i+1]
				i+=1
			except:
				raise Exception('Не указано имя файла')
		elif arg == '-c':
			try:
				characters=int(args[i+1])
				i+=1
			except:
				raise Exception('Не указано количество символов')
		elif arg == '-B':
			view = 'B'
		elif arg == '-b':
			view = 'b'
		elif arg == '-d':
			view = 'd'
		elif arg == '-p':
			plain=True
			try:
				plainFile=args[i+1]
				i+=1
			except:
				pass
		elif arg == '-r':
			reverse=True
			try:
				reverseFile=args[i+1]
				i+=1
			except:
				pass
		else:
			raise Exception('Неизвестный аргумент: '+args[i])
		i+=1
	if plain and reverse:
		print('-p и -r  не совместимы!')
		return
	if plain:
		data =str(bytesToHex(readHexFile(filename)))[2:-1]
		if not plainFile:
			print(data)
		else:
			writeTextFile(plainFile, data)
	elif reverse:
		data = hexToBytes(readTextFile(filename))
		if not reverseFile:
			print(str(data)[2:-1])
		else:
			writeHexFile(reverseFile, data)
	else:
		hexData = readHexFile(filename)
		textData = getText(hexData)
		hexData = bytesToHex(hexData)
		show(str(hexData)[2:-1],textData, characters=characters, view=view, plain=plain)


if __name__ == '__main__':
	args = sys.argv[1:]
	if '-h' in args or 	len(args)==0:
		print('''
			\r\tСПРАВКА:\n
			\r\t-h\tВызов этой справки\n\n
			\r\t-f\tУказание файла\n\t\t\tПример: python hex_viewer.py -f program.exe\n\n
			\r\t-c\tУказание количества симолов в строке. По умолчанию равно 16\n\t\t\t	Пример: python hex_viewer.py -f program.exe -c 1\n\n
			\r\t-b\tУказание отображения в двоичной системе счисления. По умолчанию в 16 СС\n\t\t\tПример: python hex_viewer.py -f program.exe -b\n\n
			\r\t-B\tУказание отображения в шестнадцатеричной системе счисления. По умолчанию в 16 СС\n\t\t\tПример: python hex_viewer.py -f program.exe -B\n\n
			\r\t-d\tУказание отображения в десятичной системе счисления. По умолчанию в 16 СС\n\t\t\tПример: python hex_viewer.py -f program.exe -d\n\n
			\r\t-p\tНепрерывное отображение кода\n\t\t\tПример: python hex_viewer.py -f program.exe -p\n\t\t\tПример: python hex_viewer.py -f program.exe -p program.txt\n\n
			\r\t-r\tПреобразование шестнадцатеричного представления в бинарный код\n\t\t\tПример: python hex_viewer.py -f program.txt -r\n\t\t\tПример: python hex_viewer.py -f program.txt -r program.exe\n\n
			''')
	else:
		run(args)