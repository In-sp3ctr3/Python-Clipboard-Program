import clipboard
import sys
import json

FILE = 'clippy.json'


def saveBoard(FILEPATH, data):
	with open( FILE , 'w') as f:
		json.dump(data,f)

def loadBoard(FILEPATH):
	try:
		with open( FILE , 'r') as f:
			data = json.load(f)
			return data
	except:
		return {}

if len(sys.argv) == 2:
	command = sys.argv[1]
	data = loadBoard(FILE)

	if command == 'save':
		key = input('enter a key: ')

		data[key] = clipboard.paste()

		saveBoard(FILE,data)

		print('Data Saved')

	elif command == 'load':
		key = input('enter the key: ')

		data = loadBoard(FILE)

		print(data[key])

	elif command == 'list':
		for x in data:
			print('Key: ', x)
			print('Data: ', data[x])
	else:
		print("Command Doesn't exist")
