
def checker(self, name, ing, bakeTime, directions):
	holder = [name, ing, bakeTime, directions]
	toBeReturn = ""

	for x in holder:
		x = x.strip()
		toBeReturn += x

	return toBeReturn