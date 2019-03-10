#input dữ liệu
#Chương trình giải phương trình bậc hai viết bằng hàm xử lí
import math #tính căn bậc hai
a = float(input('Nhập giá trị a: '))
b = float(input('Nhập giá trị b: '))
c = float(input('Nhập giá trị c: '))
x1 = ''
x2 = ''
#Hàm xử lí
def pt_bac_hai(a, b, c):
    while a != 0:
        total1 = a + b + c #Trường hợp đặc biệt a + b + c = 0
        total2 = a - b + c #Trường hợp đặc biệt a - b + c =0
        if total1 == 0:
            x1 = 1
            x2 = c / a
            print ('Nghiệm thứ nhất là: ', x1)
            print ('Nghiệm thứ hai là: ', x2)
            break
        elif total2 == 0:
            x1 = -1
            x2 = (-c) / a
            print ('Nghiệm thứ nhất là: ', x1)
            print ('Nghiệm thứ hai là: ', x2)
            break
        else:
            delta = (b * b) - (4 * a * c)
            if delta < 0:
                print('Phương trình vô nghiệm')
                break
            elif delta == 0:
                x1 = x2 = -b / (2 * a)
                print('Phương trình có nghiệm kép: ', x1)
                break
            else:
                x1 = (-b + math.sqrt(delta)) / (2 * a)          #Sử dụng #math.sqrt để tính căn bậc hai
                x2 = (-b - math.sqrt(delta)) / (2 * a)
                print('Nghiệm thứ nhất là: ', x1)
                print('Nghiệm thứ hai là: ', x2)
                break
    if a == 0:                                                  #Chuyển sang giải phương trình bậc nhất
        if b == 0:
            if c == 0:
                print ('Phương trình có vô số nghiệm')
                #Cả a , b, c đều bằng 0 thì phương trình có vô số nghiệm với mọi x
            if c != 0:
                print ('Math Error')                            # a = 0, b = 0, c = 0 , Math Error
        else:
            if c == 0:
                x1 = 0
                print ('Phương trình có một nghiệm bằng: ', x1) # a = 0, b != 0, c = 0, phương trình có 1 nghiệm duy nhất bằng 0
            else:
                x1 = (-c) / b
                print ('Phương trình có nghiệm là: ', x1)       # a = 0, b != 0, c != 0, phương trình có nghiệm -c / b

#Kết quả
pt_bac_hai(a, b, c)
