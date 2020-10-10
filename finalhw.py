import pandas as pd
import matplotlib.pyplot as plt

#GRAPH1

data1 = pd.read_csv('cars.csv',delimiter=';',skiprows=[1])

x = data1['Acceleration']
y = data1['Horsepower']

plt.scatter(x,y)
plt.title('Cars: Horsepower VS Acceleration')
plt.xlabel('Horsepower')
plt.ylabel('Acceleration')
plt.show()

#GRAPH2

df = pd.read_csv('countries.csv', delimiter=';',nrows=5,skiprows=[1])
plt.bar(x = df['Country'], 
    height= df['GDP']/10**10)
plt.title('GDP Comparison')
plt.xlabel('Country')
plt.ylabel('GDP')
plt.show()