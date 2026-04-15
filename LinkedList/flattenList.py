def flatten_list(lst):
    res =[]
    for i in lst:
        if isinstance(i,list):
            res.extend(flatten_list(i))
        else:
            res.append(i)
    return res

def flatten(lst):
    a = [ ele for i in lst for ele in i]
    return a

a = [[1,2,3],[3,4],[4,5,6]]
print(flatten(a))