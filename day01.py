import pandas as pd

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

if __name__ == "__main__":
       
    with open("C:/Users/kovto/Documents/day01Input.txt", "r") as inputList:
                
        inputList = inputList.read().splitlines()
        df = pd.DataFrame(inputList, columns=["rawInput"])
        
        df["solution"] = pd.Series(dtype=int)
        df["cumSum"] = pd.Series(dtype=int)
        mySum=0
        for i, x in df["rawInput"].items():
            mySum+=firstLastDigit(x)
            df["solution"].at[i] = firstLastDigit(x)
            df["cumSum"].at[i] = mySum
            
            print(
                "Index: ", i, 
                "Value: ", x, 
                "Solution :", firstLastDigit(x), 
                "cumSum :", mySum
            )
            
    """
        github test """