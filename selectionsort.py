import random
import datetime

test = []
for x in range(1,101):
	test.append(random.randint(0, 10000))

start = datetime.datetime.now()
def selectionSort(list):
	index = 0
	for i in range(0, len(list)):
		min = list[i]
		for j in range(i, len(list)):
			if list[j] < min:
				min = list[j]
				index = j
		(list[i], list[index]) = (list[index], list[i])
	return list
print selectionSort(test)

print datetime.datetime.now() - start