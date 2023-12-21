import pandas as pd

def isItPossible(red, green, blue):
    
    if red <= 12 and green <= 13 and blue <= 14:
        return True
    else:
        return False


if __name__ == "__main__":

    with open("C:/Users/kovto/Documents/day02Input.txt") as myFile:
        
        nStringList = myFile.readlines()
    
        nStringList = [
            x.split(";") for x in nStringList
        ]    

        valamiList = []
        for i in nStringList:
            for j in i:
                valamiList.append(j.split(" "))
                
        gameList = [x if "Game" in x else x[1:] for x in valamiList]
        for i in gameList:
            if 'Game' not in i:
                i.insert(0, None)
                i.insert(0, 'Game')
        df = pd.DataFrame(gameList)
        
        df[1] = df[1].fillna(method='ffill')
        df[1] = [x.replace(':', '') for x in df[1]]
        
        df['trueFalse'] = pd.Series(dtype=bool)
        for p, k in df.iterrows():
            myStringSplit = k.tolist()
            print(myStringSplit)
            myStringSplit = [str(x).replace(',', '') for x in myStringSplit]
            myStringSplit = [str(x).replace('\n', '') for x in myStringSplit]

            redValue, greenValue, blueValue = 0, 0, 0
            for i, x in enumerate(myStringSplit):
                
                try:
                    if x == 'red':
                        redValue = int(myStringSplit[i-1])
                except ValueError:
                    redValue = 0
                
                try:
                    if x == 'green':
                        greenValue = int(myStringSplit[i-1])
                except ValueError:
                    greenValue = 0
                
                try:
                    if x == 'blue':
                        blueValue = int(myStringSplit[i-1])
                except ValueError:
                    blueValue = 0
                    
            df['trueFalse'].at[p] = isItPossible(redValue, greenValue, blueValue)

    maxCounter = 0
    myCounter = 0
    df['finalSol'] = pd.Series(dtype=bool)
    for i in df[1].unique():
        ddf = df[df[1] == i]
        maxCounter += int(i)
        
        if False in ddf['trueFalse'].tolist():
            myCounter += int(i)

    realSolution = maxCounter - myCounter    