import pandas as pd 
import statistics as st
import plotly.figure_factory as pff
import plotly.graph_objects as pgo
import random

df = pd.read_csv("data.csv")
data = df["temp"].tolist()

popoulationMean = st.mean(data)
std = st.stdev(data)
print(popoulationMean, std)

fig = pff.create_distplot([data],["Average of the data"], show_hist = False)
#fig.show()

dataSet = []
for i in range(0,100):
    randomIndex = random.randint(0,len(data))
    value = data[randomIndex]
    dataSet.append(value)
sampleMean = st.mean(dataSet)
std2 = st.stdev(dataSet)
#print(sampleMean,std2)


def randomSetOfMean(counter):
    datalist = []
    for i in range(0,counter):
        randomIndex = random.randint(0,len(data)-1)
        value = data[randomIndex]
        datalist.append(value)
    mean = st.mean(datalist)
    return mean

def setup():
    mean_list = []
    for i in range(0,1000):
        setnum = randomSetOfMean(100)
        mean_list.append(setnum)
    m = st.mean(mean_list)
    standardev = st.stdev(mean_list)
    print(m, standardev)
    fig = pff.create_distplot([mean_list],["Temperature"], show_hist = False)
    fig.show()

setup()

# Mean of both the sample data and the poplation data is always similar.

#SD of the sampling mean =  SD Population / sqrt (number of data in each sample)
# sd of sample data = 5.699 / sqrt( 100 )
# sd of sample data = 5. 699 / 10
## sd of sample data = 0.5699


#SD of the sampling mean = 1/10 *  Population SD