def find_3_sum_unique(user_collection, target):
	result = []
	user_collection.sort()
	#print(user_collection)
	for index1 in range(len(user_collection)):
		if index1 > 0 and user_collection[index1] == user_collection[index1-1]:
			continue
		for index2 in range(index1+1, len(user_collection)):
			if index2 > index1+1 and user_collection[index2] == user_collection[index2-1]:
				continue	
			for index3 in range(index2+1, len(user_collection)):
				if index3 > index2+1 and user_collection[index3] == user_collection[index3-1]:
					continue
				sum = user_collection[index1] + user_collection[index2] + user_collection[index3]
				#print(sum)
				if sum == target:
					result.append([user_collection[index1], user_collection[index2], user_collection[index3]])
	return result					



def find_3_sum_all_combination(user_collection, target):
	result = []
	for index1 in range(len(user_collection)):
		for index2 in range(len(user_collection)):
			# avoiding same number
			if index2 == index1:
				continue
			for index3 in range(len(user_collection)):
				if index3 == index1 or index3 == index2:
					continue
				sum = user_collection[index1] + user_collection[index2] + user_collection[index3]
				if sum == target:
					result.append([user_collection[index1], user_collection[index2], user_collection[index3]])
	return result			

if __name__ == "__main__":
	input = [-1,0,1,2,-1,-4]
	target = 0
	#print(find_3_sum(input, target))
	print(find_3_sum_unique(input, target))