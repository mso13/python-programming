# Given an array a that contains only numbers in the range from 1 to a.length, 
# find the first duplicate number for which the second occurrence has the minimal index. In other words, 
# if there are more than 1 duplicated numbers, 
# return the number for which the second occurrence has a smaller index than the second occurrence of the other number does. 
# If there are no such elements, return -1.

# 0 1 2 3 4
#   1 2 3 4


# a = [2, 1, 3, 5, 3, 2]
# b = [2, 4, 3, 5, 1]

# def firstDuplicate(a):

def pares(a):
	lista = list()

	for i in range(len(a)):
		for j in range(len(a) - i):
			if a[i] == a[j+1]:
				lista.append([a[i], i])
				lista.append([a[j], j])
	
	for k in lista:
		print(k)

	return lista


pares([2, 1, 3, 5, 3, 2])