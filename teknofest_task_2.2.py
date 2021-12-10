def twoSum(array, targetSum):
    matches = {}
    for number in array:
        match = targetSum - number
        if match in matches:
            return [array.index(match), array.index(number)]
        else:
            matches[number] = True
    return []

arrNum = input("Input array of numbers: ").split(" ")
arrNum = [int(i) for i in arrNum]
target = int(input("Input target sum: "))
print(twoSum(arrNum, target))