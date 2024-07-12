import pandas as pd
import matplotlib.pyplot as plt
mtcars=pd.read_csv('mtcars.csv')
plt.hist(mtcars['mpg'],bins=10,color='skyblue',edgecolor='black')
plt.xlabel('Miles per gallon(mpg)')
plt.ylabel('Frequency')
plt.title('frequency distribution of miles per gallon(mpg)')
plt.grid(True) #Adding grid lines for better readability
plt.show()