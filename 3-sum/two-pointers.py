def find_3_sum(user_collection, target):
	result = []
	user_collection.sort()
	for index in range(len(user_collection) - 1):
		low = index + 1
		high = len(user_collection) - 1
		diff = target - user_collection[index]
		while(low < high):
			if (user_collection[low] + user_collection[high]) < diff:
				low += 1
			elif (user_collection[low] + user_collection[high]) > diff:
				high -= 1
			else:
				result.append([user_collection[index], user_collection[low], user_collection[high]])
				break
	return result	


if __name__ == "__main__":
	input = [-1,0,1,2,-1,-4]
	target = 0
	print(find_3_sum(input, target))