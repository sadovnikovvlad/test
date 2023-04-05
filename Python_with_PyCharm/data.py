import numpy.random
import pandas as pd

import matplotlib.pyplot as plt


def my_data():
    data = {"Roll-num": [10, 20, 30, 40, 50, 60, 70],
            "Age": [12, 14, 13, 12, 14, 13, 15],
            "NAME": ['John', 'Camili', 'Rheana', 'Joseph',
                     'Amanti', 'Alexa', 'Siri']}


df = pd.DataFrame(data)
df.Age.hist()
plt.show()
print(df)
