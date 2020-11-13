def selectMin(list):
    var=list[0]
    for i in list:
        if var>i:
            var=i
    return var

def triselect(list):
    result=[]
    while len(list)>0:
        var=selectMin(list)
        
    return result

print(selectMin([9,4,5,6]))
