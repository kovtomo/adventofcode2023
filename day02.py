import pandas as pd

def isItPossible(redInput, greenInput, blueInput):
    
    if redInput <= 12 and greenInput <= 13 and blueInput <= 14:
        return True
    else:
        return False

def numbersOfColours(inputList):
    
    redValue, greenValue, blueValue = 0, 0, 0
       
    for i, x in enumerate(inputList):
        if isinstance(x, str):
            if "red" in x:
                redValue = int(inputList[i-1])
                
            if "green" in x:
                greenValue = int(inputList[i-1])
                
            if "blue" in x:
                blueValue = int(inputList[i-1])
    
    return redValue, greenValue, blueValue

if __name__ == "__main__":

    with open(
            "C:/Users/kovto/Documents/adventofcode2023/day02Input.txt", "r"
    ) as myFile:
        
        gamesList = myFile.read().splitlines()
    
        gamesList = [
            x.split("; ") for x in gamesList
        ]    

        drawList = []
        for i in gamesList:
            for j in i:
                drawList.append(j.split(" "))
                
        for i in drawList:
            if 'Game' not in i:
                i.insert(0, None)
                i.insert(0, 'Game')
        df = pd.DataFrame(drawList)
        
        df = df.replace(",", "", regex=True)

        df[1].ffill(inplace=True)
        df[1] = [x.replace(':', '') for x in df[1]]

        df['trueFalse'] = pd.Series(dtype=bool)
        for i, x in df.iterrows():
            drawSplitList = x.tolist()
            
            redValue, greenValue, blueValue = numbersOfColours(drawSplitList)
                    
            df['trueFalse'].at[i] = \
                isItPossible(redValue, greenValue, blueValue)

    mySolution = 0
    df['finalSol'] = pd.Series(dtype=bool)
    for i in df[1].unique():
        tempDf = df[df[1] == i]
        
        if False not in tempDf['trueFalse'].tolist():
            mySolution += int(i)