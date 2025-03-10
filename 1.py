import pandas as pd
a = pd.read_csv("XX.csv")
count=0
for i in a["Average"]:
    if(i>40.00):
        print(a.loc[count,"Name "], "Has passed")
    else:
        print("Bad luck ",a.loc[count,"Name "],"has failed")
    count+=1
