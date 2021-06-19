if __name__ == "__main__":
	phonebook = {}
	cases = int(input())
	
	# for reading input and process them
	for i in range(cases):
		entry = input()
		key = entry.split(" ")[0]
		value = entry.split(" ")[1]
		phonebook[key] = value

	while True:
		try:
			query = input()
			if query in phonebook:
				print(query + "=" + phonebook[query])
			else:
				print("Not found")
		except:
			break			