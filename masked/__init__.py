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
				print(f'\r{p}{" "*char_count}', end='')
				char_count -= 1 if char_count > 0 else 0
			else:
				text+=char
				char_count+=1
			print(f'\r{p}{mask_with*char_count}', end='')
		except:msvcrt.getch()
	return text
