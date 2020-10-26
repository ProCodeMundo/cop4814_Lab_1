def sumValues(myDictionary):
    sum = 0  ##  Intiation of the sum == 0
    for i in myDictionary:  ## for each element in dictonary
        sum = sum + myDictionary[i]  ## add to the variable sum -- sum (0) + elements in dictionary one by one
        print(sum)  ## Print Each time that is added to the list
    return sum


dictionary: [str, int] = {'A': 100, 'B': 80, 'C': 70}  ## Fuction
print("Sum : ", sumValues(dictionary))

sumValues(dictionary)
