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
    
    justNumber = {
        "one":1,
        "two":2,
        "three":3,
        "four":4,
        "five":5,
        "six":6,
        "seven":7,
        "eight":8,
        "nine":9
    } 
    
    leftnessRankingDict = {}
    for i in wordNumber:
        tempIndexList = [x.start() for x in re.finditer(i, inputItem)]
        if tempIndexList:
            for j in tempIndexList:
                leftnessRankingDict[j] = i
                
    leftnessRankingDictNumbers = {}
    for i in justNumber.values():
        tempIndexList = [x.start() for x in re.finditer(str(i), inputItem)]
        if tempIndexList:
            for j in tempIndexList:
                leftnessRankingDictNumbers[j] = i
    
    if leftnessRankingDict:
        if leftnessRankingDictNumbers:
            leftnessRankingDict.update(leftnessRankingDictNumbers)
            
        leftnessRankingDict = dict(sorted(leftnessRankingDict.items()))
        
        elementMin = (
            min(leftnessRankingDict),
            leftnessRankingDict[min(leftnessRankingDict)]
        )
        elementMax = (
            max(leftnessRankingDict),
            leftnessRankingDict[max(leftnessRankingDict)]
        )
        leftnessRankingDictRestr = dict([elementMin, elementMax])
        
        isItString = [isinstance(x, str) for x in leftnessRankingDictRestr.values()]       
        if isItString.count(True) == 2:
            newIndex = max(leftnessRankingDictRestr) - \
                len(leftnessRankingDictRestr[min(leftnessRankingDictRestr)])
            leftnessRankingDictRestr[newIndex] = leftnessRankingDictRestr.pop(
                max(leftnessRankingDictRestr)
            )
            
        for i in leftnessRankingDictRestr:
            if isinstance(leftnessRankingDictRestr[i], str) \
                and leftnessRankingDictRestr[i] in inputItem:
                stringFirstHalf = inputItem[:i]
                stringSecondHalf = inputItem[i:]
                stringSecondHalf = stringSecondHalf.replace(
                    leftnessRankingDictRestr[i], 
                    wordNumber[leftnessRankingDictRestr[i]], 
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