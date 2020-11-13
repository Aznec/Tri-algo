list=[0,2,51,854, 14,51,8514]

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
        list.remove(var)
        result.append(var)
    return result
print(triselect(list))