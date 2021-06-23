import sys


def readFile(filename):
	with open(filename, 'rb') as f:
		hexData = f.read()
	bArray=[]
	for b in hexData:
		bArray.append(int(b))
	return bArray


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
		else:
			raise Exception('Неизвестный аргумент: '+args[i])
		i+=1
	bArray = readFile(filename)
	tArray = getText(bArray)
	show(bArray,tArray, characters=characters, view=view)


if __name__ == '__main__':
	args = sys.argv[1:]
	if '-h' in args or 	len(args)==0:
		print('''
			\r\tСПРАВКА:\n
			\r\t-h\tВызов этой справки\n
			\r\t-f\tУказание файла\n\t\t\tПример: -f program.exe\n
			\r\t-c\tУказание количества симолов в строке. По умолчанию равно 16\n\t\t\tПример: -c 1\n
			\r\t-b\tУказание отображения в двоичной системе счисления. По умолчанию в 16 СС\n\t\t\tПример: -b\n
			\r\t-B\tУказание отображения в шестнадцатеричной системе счисления. По умолчанию в 16 СС\n\t\t\tПример: -B\n
			\r\t-d\tУказание отображения в десятичной системе счисления. По умолчанию в 16 СС\n\t\t\tПример: -d\n
			''')
	else:
		run(args)