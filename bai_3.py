#Chương trình in ra n số fibonacy đầu tiên
f0 = 0
f1 = 1
f2 = f1
a = ''
n = int(input("Nhập n: "))
for i in range(n+1):
    f2 = f0 + f1
    a += str(f2) + " "
    f0 = f1
    f1 = f2
print(a)