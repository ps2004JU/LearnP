import pandas as pd
a=pd.read_csv("a1.csv")
count=0
for i in a["Average"]:
    if(i>39.99):
        print(f"{a.loc[count,"Name "]} has passed")
    else:
        print(f"Bad luck {a.loc[count,"Name "]} has failed")
    count+=1
