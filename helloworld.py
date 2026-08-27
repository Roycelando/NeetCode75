### Quick python refresher


# ternary operator
a = 8
b = 7

c = 10 if a > b else 0
print("the result is: ", c)


# filtering list

nums = [1,2,3,4,5,6,7,8,9,10]

evenNum = [x if x%2 == 0 else "odd" for x in nums]

print(nums[::-1])

def printTheList(aList):
    for e in aList:
        print(e, end=' ')

### Python data scrtuctures
## list 
# insterting to list: insert(index, val)
# list.append(val) - > adds to the end of the list

# appending to a list 
nums[len(nums):] = [11]
nums.append(13)
nums[:0] = [0]
nums.insert(0,-1)

printTheList(nums)


## tuple unpacking
tup = (10,80,2,4,6,8)

x,y,*even = tup
## swapping without using a 3rd value WOW
x, y = y , x
print(f"\nx: {x}, y: {y}")
print(f"\n{even}\n")

tup_one = (1,)*5
print(tup_one)

if 2 in tup_one:
    print("\n two is in there")
if 2 not in tup_one:
    print("\n two in not in there")

val = 13
print(f"[tup] {val} has been counted {tup_one.count(val)} times")

print(f"[list] {val} has been counted {nums.count(val)} times")

myDict = {"a": 1, "b":2, "c":3, "d":4, "e":5}
filteredDict = {k: v for k,v in myDict.items() if k !="a"}

filteredDict.pop("e",None)
print(filteredDict)

for k in myDict:
    print(k, end=' ')

print()
for v in myDict.values():
    print(v, end=' ')

invertedEvenDict = {v:k for k,v in myDict.items() if v%2 == 0}
print()
print(invertedEvenDict,end="\n")


vals = {1,2,3,4,5}
vals2 = {x for x in vals if x%2 ==0}

print(vals.intersection(vals2))
print(vals.union(vals2))
print(vals.difference(vals2))
print(vals2.difference(vals))


moreNums = [x for x in range(10)]

print(list(map(lambda x: x+x,moreNums)))

names = ["Zoe","Royce","alice", "bron"]
names2 = sorted(names,key=lambda x: x.lower())
#names.sort()

print(names2)


