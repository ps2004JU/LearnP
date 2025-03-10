import pandas as pd
a=pd.read_csv("a1.csv")
count=0
x=""
top_count=0
for i in a["Average"]:
    if(i>39.99):
        if(i==max(a["Average"])):
            top_count=count
        print(f"Bad luck {a.loc[count,"Name"]} got a KT, good")
    count+=1

print(f"{a.loc[top_count,"Name"]} is the topper with highest grade as {max(a["Average"])}")
