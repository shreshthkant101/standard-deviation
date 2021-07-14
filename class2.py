import csv
import plotly.express as ps
import pandas as pd

data = ''
total = 0
with open("class2.csv") as file:
    data = csv.reader(file)
    fileData = list(data)
    
    fileData.pop(0)

length = len(fileData)

for i in fileData:
    total += float(i[1])

mean =  total / length 

print(str(mean))
 
file2 = pd.read_csv("class2.csv")

scatter = ps.scatter(file2,x="Student Number",y="Marks")

scatter.update_layout(shapes = [
    dict(

        type = "line",
        y0 = mean,
        y1=mean,
        x0 = 0,
        x1 = length

    )
])

scatter.update_yaxes(rangemode = "tozero")

scatter.show()
