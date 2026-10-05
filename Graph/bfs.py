import collections
from typing import Deque

graph ={
    "a" : ["c" , "b" ],
    "b" : ["d"],
    "c": ["e"] ,
    "d" : ["f"] ,
    "e": [] ,
    "f" : []
}

def printbfs(graph , source):
    queue = collections.deque([source])

    while queue:
        q  = queue.pop()
        print( q + " ")
        for n in graph[q]:
            queue.appendleft(n)


printbfs(graph , "a")