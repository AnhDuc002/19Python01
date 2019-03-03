#Input_Math
#Tạo một câu chào ngẫu nhiên
#Tên, giới tính, năm sinh, năm hiện tại

import random
myList = ['Hello', 'Xin chào', 'Chào', 'Hi']
name = 'Hùng'
sex = 'anh'
age = 1990
current_year = [2019, 'Heo']

#Xử lí

chao = random.choice(myList)
tuoi_duong = '%s tuổi' % (current_year[0] - age)
tuoi_am = current_year[1]
tuoi = (tuoi_duong, 'tuổi con %s' % tuoi_am)
cau_chao = '%s %s %s, %s %s à?' % (chao, sex, name, sex, random.choice(tuoi))
print (cau_chao)

