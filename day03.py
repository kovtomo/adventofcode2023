import pandas as pd

if __name__ == "__main__":

    with open(
            "C:/Users/kovto/Documents/adventofcode2023/day03Input.txt", "r"
    ) as myFile:
        
        dfS = pd.DataFrame(
            myFile.read().splitlines(),
            columns=["rawInput"]
            )

    """
        Split each character of the imported strings into new column """
        
    df = dfS['rawInput'].apply(lambda x: pd.Series(list(x)))


    """
        Collect all symbols with x,y coordinates in DataFrame """

    symbolList = []
    for i, x in df.iterrows():
        for j, y in enumerate(x):
            try:
                y = int(y)
            except ValueError:
                pass
            if not isinstance(y, int) and y != ".":
                symbolList.append([y, [i, j]])
    """
        Check if there are integers anywhere around the symbol coordinate """
        
    for i in symbolList:
        
        """
            WARNING
        
            Luckily no symbols are in the first/last row or first/last column 
            Currently it would run on error because of index limits """

        """
            Create a list of the neighbouring elements with coordinate 
            of the given symbol """
            
        columnIndex = i[1][1]
        rowIndex = i[1][0]

        neighbourTopLeft = df[columnIndex-1].iloc[rowIndex-1]
        neighbourTop = df[columnIndex].iloc[rowIndex-1]
        neighbourTopRight = df[columnIndex+1].iloc[rowIndex-1]

        neighbourLeft = df[columnIndex-1].iloc[rowIndex]
        neighbourRight = df[columnIndex+1].iloc[rowIndex]

        neighbourBottomLeft = df[columnIndex-1].iloc[rowIndex+1]
        neighbourBottom = df[columnIndex].iloc[rowIndex+1]
        neighbourBottomRight = df[columnIndex+1].iloc[rowIndex+1]
        
        neighbourList = [
            [neighbourTopLeft, [columnIndex-1, rowIndex-1]],
            [neighbourTop,[columnIndex, rowIndex-1]],
            [neighbourTopRight,[columnIndex+1,rowIndex-1]],
            [neighbourRight,[columnIndex+1,rowIndex]],
            [neighbourBottomRight,[columnIndex+1,rowIndex+1]],
            [neighbourBottom,[columnIndex,rowIndex+1]],
            [neighbourBottomLeft,[columnIndex-1,rowIndex+1]],
            [neighbourLeft,[columnIndex-1,rowIndex]]
            ]
        
        """
            Check if there are further digits on the left or right 
            or both sides (and further until all digits found on both sides) 
            of the given digit neighbouring a symbol """
            
            
        """
            WARNING
            
            What do you do if a number is neighbouring two or more symbols? """

        for j in neighbourList:
            
            """ 
                WARNING
                
                Don't exceed index limits here either """
            
            try:
                j[0] = int(j[0])
            except ValueError:
                pass

            if isinstance(j[0], int):
            
                columnIndex = j[1][0]
                rowIndex = j[1][1]
                                
                checkRight = df[columnIndex+1].iloc[rowIndex]
                checkLeft = df[columnIndex-1].iloc[rowIndex]
                
                allDigits = [df[columnIndex].iloc[rowIndex]]
                
                try:
                    checkRight = int(checkRight)
                except ValueError:
                    pass 
                
                try:
                    checkLeft = int(checkLeft)
                except ValueError:
                    pass
                
                if isinstance(checkRight, int) and \
                    not isinstance(checkLeft, int):                        
                    # myCounter=1
                    # nextDigit=0
                    # while nextDigit != ".":
                    #     nextDigit = \
                    #         df[columnIndex+myCounter].iloc[rowIndex]
                    #     allDigits.append(nextDigit)
                    #     nextDigit = \
                    #         df[columnIndex+myCounter+1].iloc[rowIndex]
                    #     myCounter+=1
                    pass
                
                if not isinstance(checkRight, int) and \
                    isinstance(checkLeft, int):
                    pass
                
                if isinstance(checkRight, int) and \
                    isinstance(checkLeft, int):
                    pass
