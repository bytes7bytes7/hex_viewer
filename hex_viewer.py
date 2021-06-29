import sys

def writeTextFile(filename, textData):
	with open(filename, 'w') as f:
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


def bytesToInt(bArray):
	ints=[]
	for b in bArray:
		ints.append(int(b))
	return ints


def hexToBytes(hexData):
	return bytes(bytearray([int(hexData[i:i+2],16) for i in range(0, len(hexData), 2)]))


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


def show(bArray, tArray, **kwargs):
	if len(bArray)==len(tArray):
		for key, value in kwargs.items():
			if key=='characters':
				characters = value
			elif key=='view':
				view = value
		i=0
		while i*characters<len(bArray):
			start = i * characters
			end = min((i + 1) * characters, len(bArray))
			byte = []
			string =[e.replace('\n',' ').replace('\r', ' ').replace('\b','') for e in tArray[start: end]]
			if view == 'B':
				for b in  bArray[start: end]:
					b = str(hex(b))[2:]
					while len(b) < 2:
						b = ' '+ b
					byte.append(b)
			elif view== 'b':
				for b in  bArray[start: end]:
					b = bin(b)[2:]
					while len(b) < 8:
						b = '0'+ b
					byte.append(b)
			elif view== 'd':
				for b in  bArray[start: end]:
					b = str(b)
					while len(b) < 3:
						b = ' '+ b
					byte.append(b)
			
			print('{}\t\t{}'.format(' '.join(e for e in byte),''.join(e for e in string)))
			i+=1
	else:
		raise Exception('Длина байтов != длина символов')


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
		data = readHexFile(filename)
		bArray = bytesToInt(data)
		byte = []
		for b in  bArray:
			b = str(hex(b))[2:]
			while len(b)<2:
				b = '0'+b
			byte.append(b)
		byte = ''.join(e for e in byte)
		if not plainFile:
			print(byte)
		else:
			writeTextFile(plainFile, byte)
	elif reverse:
		data = hexToBytes(readTextFile(filename))
		if not reverseFile:
			print(str(data)[2:-1])
		else:
			writeHexFile(reverseFile, data)
	else:
		hexData = readHexFile(filename)
		bArray = bytesToInt(hexData)
		tArray = getText(bArray)
		show(bArray,tArray, characters=characters, view=view, plain=plain)


if __name__ == '__main__':
	args = sys.argv[1:]
	if '-h' in args or 	len(args)==0:
		print('''
			\r\tСПРАВКА:\n
			\r\t-h\tВызов этой справки\n
			\r\t-f\tУказание файла\n\t\t\tПример: python -f program.exe\n
			\r\t-c\tУказание количества симолов в строке. По умолчанию равно 16\n\t\t\tПример: python -f program.exe -c 1\n
			\r\t-b\tУказание отображения в двоичной системе счисления. По умолчанию в 16 СС\n\t\t\tПример: python -f program.exe -b\n
			\r\t-B\tУказание отображения в шестнадцатеричной системе счисления. По умолчанию в 16 СС\n\t\t\tПример: python -f program.exe -B\n
			\r\t-d\tУказание отображения в десятичной системе счисления. По умолчанию в 16 СС\n\t\t\tПример: python -f program.exe -d\n
			\r\t-p\tНепрерывное отображение кода\n\t\t\tПример: python -f program.exe -p\n\t\t\tПример: python -f program.exe -p program.txt\n
			\r\t-r\tПреобразование шестнадцатеричного представления в бинарный код\n\t\t\tПример: python -f program.txt -r\n\t\t\tПример: python -f program.txt -r program.exe\n
			''')
	else:
		run(args)