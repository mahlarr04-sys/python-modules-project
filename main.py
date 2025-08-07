# این فایل فقط حاوی وروردی و خروجی و ..

import calculator_functions  #وصل ماژول ماشین حساب

num1= float(input("عدد اول را وارد کن:"))
num2= float(input("عدد دوم را وارد کن:"))


#اجرای توابع و نمایش نتیجه ها
print(":جمع", calculator_functions.add(num1,num2))
print(":تفریق", calculator_functions.subtract(num1,num2))
print(":ضرب", calculator_functions.multiply(num1,num2))
print(":تقسیم", calculator_functions.divide(num1,num2))