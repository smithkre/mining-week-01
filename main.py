import pandas as pd
from scipy.io import arff

data = arff.loadarff('input.arff')
df = pd.DataFrame(data[0])

print(df)