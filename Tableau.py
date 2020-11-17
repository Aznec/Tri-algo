def _init_(height, lenght):

    listtab=[]

    for i in range (height):
        listRow=[]
        for j in range (lenght):
            listRow.append("x")
        listtab.append(listRow)
    return listtab
list = _init_(15,15)

for i in list :
    print(i)