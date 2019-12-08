""" Program name: PASSWORD GENERATOR """

import argparse
import random

parser = argparse.ArgumentParser(description='PASSWORD GENERATOR v0.0.1', epilog='Используйте -h для помощи')
parser.add_argument('-l', '--length', type = int, default = 8, help = 'Укажите желаемую длину пароля, но она должна быть не меньше 4 символов (по умолчанию: 8)')

default = {
	'numbers': True,
	'uppercase_letter': True,
	'lowercase_letter': True,
	'special_char': True
}

def getPassword(length = 8, options = default):
	symbols = {
		'numbers': '0123456789',
		'uppercase_letter': 'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
		'lowercase_letter': 'abcdefghijklmnopqrstuvwxyz',
		'special_char': '@$&%#!?:;/|\\()[]{}_.,+-=~*^`\'"'
	}
	
	password = []
	sym_list = []

	for key in symbols.keys():
		if (options[key]):
			sym_list += list(symbols[key])
	for i in range(0, length):
		password.append(random.choice(sym_list))
	return ''.join(password)

args = parser.parse_args()

if args.length <= 3:
	print('Длина пароля должны быть не менее 4 символов. Попробуйте снова')
else:
	print(getPassword(length = args.length))