import pandas as pd
a=pd.read_csv("a1.csv")
count=0
x=""
top_count=0
for i in a["Average"]:
    if(i>39.99):
        if(i==max(a["Average"])):
<<<<<<< HEAD
            print(f"Congratulations !!! {a.loc[count,"Name"]} has topped with grade {i}")
        else:
            print(f"{a.loc[count,"Name"]} has passed with grade {i}")
        
    else:
        print(f"{a.loc[count,"Name"]} got a KT, good luck for the next time")
    count+=1

print("Note, a student gets KT when his grade is less than 39.9")
=======
            top_count=count
        print(f"Bad luck {a.loc[count,"Name"]} got a KT, good")
    count+=1

print(f"{a.loc[top_count,"Name"]} is the topper with highest grade as {max(a["Average"])}")
>>>>>>> main
