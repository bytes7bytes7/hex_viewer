# Hex Viewer

Hex-просмоторщик, написанный на Python

## Использование

По умолчанию отображает 16 символов и их кодов в одной строке, причем код каждого символа отображается в шестнадцатеричной системе счисления.
```
python hex_viewer.py -f program.exe
```
Дополнительные параметры:
```
СПРАВКА:

	-h    Вызов этой справки

	-f    Указание файла
			Пример: python hex_viewer.py -f program.exe

	-c    Указание количества симолов в строке. По умолчанию равно 16
			Пример: python hex_viewer.py -f program.exe -c 1

	-b    Указание отображения в двоичной системе счисления. По умолчанию в 16 СС
			Пример: python hex_viewer.py -f program.exe -b

	-B    Указание отображения в шестнадцатеричной системе счисления. По умолчанию в 16 СС
			Пример: python hex_viewer.py -f program.exe -B

	-d    Указание отображения в десятичной системе счисления. По умолчанию в 16 СС
			Пример: python hex_viewer.py -f program.exe -d

	-p    Непрерывное отображение кода
			Пример: python hex_viewer.py -f program.exe -p
			Пример: python hex_viewer.py -f program.exe -p program.txt

	-r    Преобразование шестнадцатеричного представления в бинарный код
			Пример: python hex_viewer.py -f program.txt -r
			Пример: python hex_viewer.py -f program.txt -r program.exe
```