def NonRepeating(arr, n):

	hashTable={}

	for i in range(n):
		if arr[i] not in hashTable:
			hashTable[arr[i]]=0
		hashTable[arr[i]]+=1

	return [j for j, value in hashTable.items() if value == 1]  

arrNum = input()
arrNum = list(arrNum)
length = len(arrNum)
print(NonRepeating(arrNum, length))