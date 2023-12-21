import pandas as pd
import time

if __name__ == "__main__":
     
    startTime = time.perf_counter()
    with open("C:/Users/kovto/Documents/day07Input.txt") as myFile:
        inputList = myFile.readlines()
        inputList = [
            x.split(" ") for x in inputList
        ]
        
        df = pd.DataFrame(
            data=inputList,
            columns=['handOfCards', 'bet']
        )
        
        df['bet'] = pd.to_numeric(df['bet'])
        
        dfCards=pd.DataFrame()
        dfCards[['cardOne', 'cardTwo', 'cardThree', 'cardFour', 'cardFive']] = df['handOfCards'].apply(lambda x: pd.Series(list(x)))
        
        def valuePairing(inputItem):
            if inputItem == "2":
                return 2
            if inputItem == "3":
                return 3
            if inputItem == "4":
                return 4
            if inputItem == "5":
                return 5
            if inputItem == "6":
                return 6
            if inputItem == "7":
                return 7
            if inputItem == "8":
                return 8
            if inputItem == "9":
                return 9
            if inputItem == "T":
                return 10
            if inputItem == "J":
                return 11
            if inputItem == "Q":
                return 12
            if inputItem == "K":
                return 13
            if inputItem == "A":
                return 14
        
        df['cardValues'] = pd.Series(dtype=int)
        for i, x in df.iterrows():
            df['cardValues'].at[i] = pd.Series(list(df['handOfCards'].iloc[i]))
            df['cardValues'].at[i] = pd.Series(df['cardValues'].at[i]).apply(lambda row: valuePairing(row))

        df['duplicates'] = pd.Series(dtype=str)
        df['duplicatesUnique'] = pd.Series(dtype=str)
        df['handValue'] = pd.Series(dtype=int)
        for i, x in dfCards.iterrows():
            
            df['duplicates'].at[i] = x[x.duplicated(keep=False)]
            df['duplicates'].at[i] = pd.Series(df['duplicates'].iloc[i]).apply(lambda row: valuePairing(row))

            df['duplicatesUnique'].at[i] = {row:list(df['duplicates'].at[i]).count(row) for row in df['duplicates'].at[i]}
            
            p = 0
            for j in df['duplicatesUnique'].iloc[i]:
                p += j * df['duplicatesUnique'].iloc[i][j]
                df['handValue'].at[i] = p

        df['handValue'].fillna(0, inplace=True)
    
    endTime = time.perf_counter()
    print(endTime - startTime)