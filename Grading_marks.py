m1 = int(input("Your score in Maths is ="))
m2 = int(input("Your score in English is ="))
m3 = int(input("Your score in  Science is ="))
m4 = int(input("Your score in Hindi is ="))
m5 = int(input("Your score in Art is ="))

total = m1+m2+m3+m4+m5
avg = total/5

if avg>=91 and avg<=100:
    print("Your grade is A1")
elif avg>=81 and avg<=91:
    print("Your grade is A2")
elif avg>=71 and avg<=81:
    print("Your grade is B1")
elif avg>=61 and avg<=71:
    print("Your grade is B2")
elif avg>=51 and avg<=61:
    print("Your grade is C1")
elif avg>=41 and avg<=51:
    print("Your grade is C2")
elif avg>=33 and avg<=41:
    print("Your grade is D")
elif avg>=21 and avg<=33:
    print("Your grade is E1")
elif avg>=0 and avg<=21:
    print("Your grade is E2")
else:
    print("Invalid Input!")