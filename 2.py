def mean(val):
    if type(val) == dict :
        mn=sum(val.values()) /len(val)
    else :
        mn = sum(val) /len(val)
    return mn

tmp=[8.8 ,9.1 , 9.9]
st_g= {'Sun' :8.8 , 'john' : 7.5 , 'Rishik' : 9.5}
print( mean(st_g))
print(mean ( tmp))
