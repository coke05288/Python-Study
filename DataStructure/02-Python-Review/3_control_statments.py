num = 8

# if
if num % 2 == 0:
    print("짝수입니다.")
elif num == 0:
    print("0입니다.")
else:
    print("홀수입니다.")

# while
dan = int(input("구구단을 입력하세요 : "))
n = 1
while n <= 9:
    print("%2d x %2d = %2d" % (dan, n, dan*n))
    n += 1

# for
dan = int(input("구구단을 입력하세요 : "))
for i in range(1, 10):
    print("%2d x %2d = %2d" % (dan, i, dan*i))

print()

list1 = [1, 2, 3, 4, 5]
for i in list1:
    print("%s " % (i), end=" ")

print()

myDict = {"name": "김영준", "age": 25, "score": 24.3}
myDict["address"] = "인천"
for key, value in myDict.items():
    print("\"%s\" : %s" % (key, value))


