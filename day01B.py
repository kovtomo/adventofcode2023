import pandas as pd
import re

def firstLastDigit(inputItem):
        
    wordList = [x for x in inputItem]
    
    onlyNumberList = []
    for i in wordList:
        try:
            onlyNumberList.append(int(i))
        except ValueError:
            pass
        
    if len(onlyNumberList) == 1:
        return (onlyNumberList[0] * 10) + onlyNumberList[0]
       
    if len(onlyNumberList) > 1:
        return (onlyNumberList[0] * 10) + onlyNumberList[-1]
    
    else: 
        return 0
    
def wordToNumber(inputItem):

    """" Looking for the first index in the <inputItem> string 
            of each occurance of each number written with letters 
            and create a dict of the index, values pairs """    

    wordNumber = {
        "one":"1",
        "two":"2",
        "three":"3",
        "four":"4",
        "five":"5",
        "six":"6",
        "seven":"7",
        "eight":"8",
        "nine":"9"
    } 
    
    numberWithLetterDict = {}
    for i in wordNumber:
        tempIndexList = [x.start() for x in re.finditer(i, inputItem)]
        if tempIndexList:
            for j in tempIndexList:
                numberWithLetterDict[j] = i
        
    """" Looking for the first index in the <inputItem> string 
            of each occurance of each number written as a number 
            and create a dict of the index, values pairs """ 
            
    numberList = list(range(1,10))
    
    numberWithNumberDict = {}
    for i in numberList:
        tempIndexList = [x.start() for x in re.finditer(str(i), inputItem)]
        if tempIndexList:
            for j in tempIndexList:
                numberWithNumberDict[j] = i
    
    """" In case both above created dict exists, 
            create a single dict and sort it by key 
        
         Then choose the first and last item by key in the sorted dict. These
         are the first and last occurances of numbers in <inputItem> string,
         written either by letters or as a number
         
         If both the first and last number in the <inputItem> string are 
         written by letters, then modify the positional index of the
         last item (decrease by the lenght of the first number written as a
         word) as it will change after the replacement of the first number
         written with letters (the <inputItem> string will be shorter after the 
         first iteration of replacement)
         
             eg. nine54gfdgeight -> 0-nine; 10-eight
             
                 After replacing "0-nine", the initial string will be shorter
                 So "10-eight"" is no longer true: 954gfdgeight -> 7-eight
         
        Finally cut the <inputItem> string by half at the start index of the 
        number written with letters (which is the key of the our dict) 
        which we want to replace to make sure we replace the number written 
        with letters at the right position starting from left to right and
        going to replace only the first occurance. At the end we just concat
        back the two halves and we are finished with the replacement """ 
            
    if numberWithLetterDict:
        
        allNumbersRankedDict = dict()
        allNumbersRankedDict.update(numberWithLetterDict)

        if numberWithNumberDict:
            allNumbersRankedDict.update(numberWithNumberDict)
            
        allNumbersRankedDict = dict(sorted(allNumbersRankedDict.items()))
        
        elementMin = (
            min(allNumbersRankedDict),
            allNumbersRankedDict[min(allNumbersRankedDict)]
        )
        elementMax = (
            max(allNumbersRankedDict),
            allNumbersRankedDict[max(allNumbersRankedDict)]
        )
        minMaxDict = dict([elementMin, elementMax])
        
        isItString = [isinstance(x, str) for x in minMaxDict.values()]       
        if isItString.count(True) == 2:
            newIndex = max(minMaxDict) - \
                len(minMaxDict[min(minMaxDict)])
            minMaxDict[newIndex] = minMaxDict.pop(
                max(minMaxDict)
            )
            
        for i in minMaxDict:
            if isinstance(minMaxDict[i], str) \
                and minMaxDict[i] in inputItem:
                stringFirstHalf = inputItem[:i]
                stringSecondHalf = inputItem[i:]
                stringSecondHalf = stringSecondHalf.replace(
                    minMaxDict[i], 
                    wordNumber[minMaxDict[i]], 
                    1
                )
                inputItem = stringFirstHalf + stringSecondHalf
      
    return inputItem

if __name__ == "__main__":
       
    with open(
            "C:/Users/kovto/Documents/adventofcode2023/day01Input.txt", "r"
    ) as inputList:
                
        inputList = inputList.read().splitlines()
        df = pd.DataFrame(inputList, columns=["rawInput"])
        
        df["editedInput"] = df["rawInput"].apply(
            lambda row: wordToNumber(row)
        )
        
        df["solution"] = pd.Series(dtype=int)
        df["cumSum"] = pd.Series(dtype=int)
        mySum=0
        for i, x in df["editedInput"].items():
            mySum+=firstLastDigit(x)
            df["solution"].at[i] = firstLastDigit(x)
            df["cumSum"].at[i] = mySum
            print(
                "Index: ", i, 
                "Value: ", x, 
                "Solution :", firstLastDigit(x), 
                "cumSum :", mySum
            )