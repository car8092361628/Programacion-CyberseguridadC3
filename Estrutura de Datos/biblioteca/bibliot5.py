# python -m pip install panda
import pandas as pd

data={'Nombre': ['Juan','Ana','Pedro'],
      'Edad': [25,30,22],
      'Ciudad': ['Madrid','Santodomingo','Santiago']}

df=pd.DataFrame(data)
print(df)