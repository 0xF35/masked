__author__ = 'Dhruval Parmar'
__version__ = '1.0.0'
__email__ = 'dhruvalparmar@duck.com'

import msvcrt

def mask_input(p, mask_with='•'):
	print(p, end='', flush=True)
	char_count, text = 0, ''
	while True:
		try:
			char = msvcrt.getch().decode()
			if char == '\r':break
			elif char == '\x08':
				text = text[:-1]
				print(f'\r{p}{mask_with*(char_count - 1) + " "}' if char_count > 0 else f'\r{p}{mask_with*(char_count - 1)}', end='')
				char_count -= 1 if char_count > 0 else 0
			else:
				text+=char
				char_count+=1
			print(f'\r{p}{mask_with*char_count}', end='')
		except:msvcrt.getch()
	return text
