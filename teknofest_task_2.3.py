def countOccurrence(arr):
  hashTable = {}
  for i in arr:
    if i in hashTable:
      hashTable[i] +=1
    else:
      hashTable[i] =1
  return hashTable

arr = input("Input array of strings: ").split(" ")
occurrence = countOccurrence(arr)

for key, value in occurrence.items():
    print(f"{key}: {value}")