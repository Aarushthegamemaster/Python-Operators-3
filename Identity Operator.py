a = 8
b = 6

if (type(a and b)is int):
    print(a,"and",b, "are integers")
else:
    print(a,"and",b," are not integers")

c = 7.0

if (type(c) is float):
    print(c,"is a float")
else:
    print(c,"is not a float")


d = 89
e = 89

if(d is e):
    print(d, "and",e, "are the same number")
else:
    print(d,"and",e,"are not the same number")