# این فایل فقط حاوی توابع محاسباتی هست ،بدون ورودی و خروجی کاربر
# این فایل مثل یک جعبه‌ابزار (ماژول) هست که فقط ابزار (توابع) توشه. کار اجرا باهاش نیست!
import math
from datetime import date

def add (a,b):
    # جمع دو عدد
    return a+b 

def subtract(a,b):
    # تفریق دو عدد
    return a-b 

def multiply(a,b):
    # ضرب دو عدد
    return a*b

def divide (a,b):
    # تقسیم دو عدد.
    if b==a:
        return"خطا: تقسیم بر صفر مجاز نیست"
    return a/b     #ای خط در حالت عدی زمانی که بی صفر نباشد اجرا میشه

def power (a,b):
    #توان دو عدد
    return a**b


def square_root(n):
    #جذر تابع
    if n<0:
        return"جزر اعداد منفی تعریف نشده!"
    return math.sqrt(n)

def calculate_bmi(weight, height):
    # تابع شاخص توده بدنی (BMI)
    if height <= 0:
        return"قد نمیتونه صفر یا منفی باشد!!"
    bmi =weight/(height**2)
    return round(bmi , 2)

#محاسبه سن
def calculate_age(birth_year):
    current_year = datetime.datetime.now().year
    return current_year - birth_year
