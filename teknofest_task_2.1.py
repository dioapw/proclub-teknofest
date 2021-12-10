def NonRepeating(arr, n):

	repeatingList=[]
	hashTable={}

	for i in range(n):
		if arr[i] not in hashTable:
			hashTable[arr[i]]=0
		hashTable[arr[i]]+=1

	for j in hashTable:
		if (hashTable[j]== 1):
			repeatingList.append(j)

	return repeatingList  

arrNum = input()
arrNum = list(arrNum)
length = len(arrNum)
print(NonRepeating(arrNum, length))