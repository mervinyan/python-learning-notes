print("    Hello, World!  \t\t\n".strip())

print("Hello, world!".split())

print("Hello,  world!".split(" "))

print("www.networksciencelab.com".split("."))

print(", ".join(["alpha", "bravo", "charlie", "delta"]))

print("-".join("1.617.305.1985".split(".")))

print(" ".join("This string\n\r has many\t\tspaces".split()))

print("www.networksciencelab.com".find(".com"))

print("www.networksciencelab.com".count("."))

bigList = [str(i) for i in range(10000000)]
"abc" in bigList

bigSet = set(bigList)
"abc" in bigSet

seq = ["alpha", "bravo", "charlie", "delta"]
print(dict(enumerate(seq)))

myList = [-4, -3, -2, -1, 0, 1, 2, 3, 4]
print([x for x in myList])
print([x for x in myList if x >= 0])
print([x**2 for x in myList])
print([1/x for x in myList if x != 0])
print((x**2 for x in myList))

from collections import Counter
phrase = "a man a plan a canal panama"
cntr = Counter(phrase.split())
print(cntr.most_common())
cntrDict = dict(cntr.most_common())
print(cntrDict)
print(cntrDict['a'])