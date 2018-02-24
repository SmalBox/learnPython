# -*- coding: utf-8 -*-
#计算人体BMI数值
h = input('请输入身高（单位：米）：')
w = input('请输入体重（单位：千克）：')
height = float(h) #身高
weight = float(w) #体重
bmi = weight/(height*height) #bmi公式：体重除以身高的平方
if bmi > 32:
    print('BMI值:%.2f 严重肥胖' % bmi)
elif bmi >= 28:
    print('BMI值:%.2f 肥胖' % bmi)
elif bmi >=25:
    print('BMI值:%.2f 过重' % bmi)
elif bmi >=18.5:
    print('BMI值:%.2f 正常' % bmi)
else:
    print('BMI值:%.2f 过轻' % bmi)

