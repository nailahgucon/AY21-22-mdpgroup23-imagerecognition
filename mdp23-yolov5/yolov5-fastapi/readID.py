def readID():
	with open("TEST.txt", "r") as fp:
		lines = fp.readlines()
		first = lines[0]
		print(first)
		return first