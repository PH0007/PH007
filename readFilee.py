#%%

def getA(a):
    b=a+1
    yield b    

# %%
list1 = [2,3,45,5,6]
for i in list1:
    p =getA(i)

#%%
for i in p:
    print(i)