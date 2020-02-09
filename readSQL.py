#%%
import pandas as pd
import numpy as np
import datetime as dt

#%%

# datetime.datetime
dates = [dt.datetime(2000,1,1),dt.datetime(2000,1,2), dt.datetime(2000,1,3)]

# %%
s = pd.Series(np.random.randn(3), index=dates)

# %%
s.index[0]