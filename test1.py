#%%
import pandas as pd

f1= pd.read_csv("csvText.csv",header=None)
#%%
f1.columns= ['name','date','flag','attri']

#%%
f1.date = pd.to_datetime(f1.date)

#%%
f1.set_index('date',inplace=True)

# %%
f1.attri.plot()

#%%
f1.reset_index(inplace=True)
#%%
f1.date= f1.date.apply(pd.Timestamp)

#%%
f1['X1']= f1.attri.shift(-1)

