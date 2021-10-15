import os
import pandas as pd

def rec_select(bird):
    files=[filename for filename in os.listdir('./') if filename.endswith('.xlsx')]
    df=pd.DataFrame()

    for file_name in files:
        curr_df=pd.read_excel(file_name, sheet_name=None, usecols=range(3), converters={'Foreground Species':str,'Background Species':str})
        df=pd.concat([df,pd.concat(curr_df, ignore_index=True)], ignore_index=True)
    df['Background Species'].fillna(value='No record', inplace=True)
    recordings=[]
    for i in range(0,len(df)-1):
        if df.iloc[i,1].lower()==bird.lower() and df.iloc[i,2].lower()=='no record':
            recordings.append(df.iloc[i,0])

    print(recordings)