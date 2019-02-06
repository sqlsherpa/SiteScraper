
import pandas as pd
import numpy as np

str = 'http://chinaglaze.com/uploads/products/dots/80950.png'

newstr = str.replace('dots','bottle')

print(newstr)



raw_data = {'name': ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'],
                      'age': [20, 19, 22, 21],
                      'favorite_color': ['www.blue/mana', 'red', 'yellow', "green"],
                      'grade': [88, 92, 95, 70]}
df = pd.DataFrame(raw_data, index = ['Willard Morris', 'Al Jennings', 'Omar Mullins', 'Spencer McDaniel'])

dak = df['favorite_color'].str.replace('blue','hahahhh')

print(dak)