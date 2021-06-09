def print_all_dash(times):
	str = ""
	for i in range(times):
		str += "-"
	return str	

def print_dot_horizontal(times):
	str = ""
	for i in range(times):
		str += " "
	return str

def generate_full_row(width, num_mid_section, msg = ""):
	num_dash = (width - num_mid_section) // 2
	p1 = print_all_dash(num_dash)
	if msg:
		p2 = msg
	else:	
		p2 = print_dot_horizontal(num_mid_section)
	p3 = print_all_dash(num_dash)	
	return p1 + p2 + p3


if __name__ == "__main__":
	user_input = input()
	
	row = int(user_input.split(" ")[0])
	col = int(user_input.split(" ")[1])
	mid = row // 2 							# 'welcome' would be printed on this row
	message = 'WELCOME'

	for i in range(row):
		if i < mid:
			num_dot_horizontal = 3 if i == 0 else (num_dot_horizontal + 6)
			for j in range(col):
				row_str = generate_full_row(col, num_dot_horizontal)	
			print(row_str)

		elif i == mid:	
			for j in range(col):
				row_str = generate_full_row(col, len(message), message)	
			print(row_str)

		else:	
			num_dot_horizontal = num_dot_horizontal if i == (mid + 1) else (num_dot_horizontal - 6)
			for j in range(col):
				row_str = generate_full_row(col, num_dot_horizontal)	
			print(row_str)
	