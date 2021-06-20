def find_3_sum(user_collection, target):
	result = []
	for index in range(len(user_collection) - 1):
		low = index + 1
		high = len(user_collection) - 1
		diff = target - user_collection[index]
		while(low < high):
			sum = user_collection[low] + user_collection[high]
			if sum < diff:
				low += 1
			elif sum > diff:
				high -= 1
			else:
				result.append([user_collection[index], user_collection[low], user_collection[high]])
				break
	return result					

def find_4_sum(user_collection, target):
	user_collection.sort()
	result = []
	for index in range(len(user_collection)):
		sublist = user_collection[index+1::]
		diff = target - user_collection[index]
		sub_result = find_3_sum(sublist, diff)
		for each_result in sub_result:
			each_result.append(user_collection[index])
		#print(sub_result)	
		result = result + sub_result
	return result	


if __name__ == "__main__":
	input = [1,0,-1,0,-2,2]
	target = 0
	print(find_4_sum(input, target))