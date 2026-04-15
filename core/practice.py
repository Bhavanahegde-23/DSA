#Dict - stores key-value pair
import items
d = {'a':12 ,'b':6,'c':8}
d['d'] = 1
x = dict(sorted(d.items() , key= lambda item: item[1] , reverse = True) )
print(x.get('c',0))

#generator
#It produces the values lazily instead of storing them in memory
#used when data is very large
def nums():
    yield 1
    yield 2
    yield 3

g = nums()
print(next(g))
print(next(g))

#decorator : modifies the func behaviour without changing its code

#async
import asyncio

async def task1():
    await asyncio.sleep(2)
    print("task 1 is done")

async def task2():
    await asyncio.sleep(2)
    print("task2 is done")

async def main():
    await asyncio.gather(task1(),task2())

asyncio.run(main())

# API , put post get delete




