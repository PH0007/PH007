#%%
class car(object):
    def __init__(self):
        self.__a= 'JIM'

    @property
    def na(self):
        return self.__a

    @na.setter
    def na(self,value):
        self.__a = value
        print('XXXXXXXX')
# %%

odi= car()
odi.na ='zzz'
print(odi.na)