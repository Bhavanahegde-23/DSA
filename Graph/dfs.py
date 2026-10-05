graph ={
    "a" : ["b" ,"c"],
    "b" : ["d"],
    "c": ["e"] ,
    "d" : ["f"] ,
    "e": [] ,
    "f" : []
}

def dfsPrint(graph , source):
    st = [source]
    while st :
        current = st.pop()
        print(current + " ")

        for n in graph[current]:
            st.append(n)


dfsPrint(graph ,"a")

print("\n dfs - rec")
#Recursive

def printdfsRec(graph , source):
    print(source , " ")
    for n in graph[source]:
        printdfsRec(graph ,n)


printdfsRec(graph , "a")