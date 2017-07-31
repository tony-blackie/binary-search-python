# Hello World program in Python
    
array = [2, 4, 8, 15, 22, 32, 43, 52, 64, 77, 82, 91, 102, 109, 111, 123, 175, 178]
item = 3

def binarySearch(list, item):
    print ('worked')
    lowIndex = 0
    highIndex = len(list) - 1
    iterationsCounter = 0
    
    while lowIndex <= highIndex:
        iterationsCounter += 1
        midIndex = round((lowIndex + highIndex) / 2)
        midItem = list[midIndex]
        
        print("midItem: #{0}".format(midItem))
        print("midIndex: #{0}".format(midIndex))
        
        if (midItem == item):
            print("number of iterations #{0}".format(iterationsCounter))
            return midIndex
        
        if (midItem < item):
            lowIndex = midIndex + 1
            
        if (midItem > item):
            highIndex = midIndex - 1
        
    if (lowIndex <= highIndex and midItem != item):
        return None
    
    print("number of iterations #{0}".format(iterationsCounter))
    
result = binarySearch(array, item)
print("result: #{0}".format(result))