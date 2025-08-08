# این فایل فقط حاوی وروردی و خروجی و ..


import calculator_functions  #وصل ماژول ماشین حساب


print(" خوش اومدی به ماشین حساب هوشمند! ")
print(":لیستی از امکانات ماشین‌حساب ")
print("+  برای جمع")
print("-  برای تفریق")
print("*  برای ضرب")
print("/  برای تقسیم")
print("** برای توان")
print("sqrt برای جذر")
print("bmi برای محاسبه شاخص توده بدنی")
print("age برای محاسبه سن")

operation = input("کدوم عملیات رو می‌خوای انجام بدی؟ بنویس: ").lower()

#  عملیات‌های خاص که فقط یک ورودی می‌خوان
#جزر
if operation == "sqrt":
    num = float(input("عدد رو وارد کن: "))
    result = calculator_functions.square_root(num)

#BMI
elif operation == "bmi":
    weight = float(input("وزن (کیلوگرم): "))
    height = float(input("قد (متر): "))
    result = calculator_functions.calculate_bmi(weight, height)

#مشخص کردن سن

elif operation == "age":
    birth_year = int(input("سال تولد خود را وارد کنید: "))
    # تشخیص شمسی بودن و تبدیل به میلادی
    if birth_year < 1500:
        birth_year += 621 
    result = calculator_functions.calculate_age(birth_year)


# بقیه عملیات‌ها که دو تا عدد لازم دارن
else:
    num1 = float(input("عدد اول رو وارد کن: "))
    num2 = float(input("عدد دوم رو وارد کن: "))

    if operation == "+":
        result = calculator_functions.add(num1, num2)
    elif operation == "-":
        result = calculator_functions.subtract(num1, num2)
    elif operation == "*":
        result = calculator_functions.multiply(num1, num2)
    elif operation == "/":
        result = calculator_functions.divide(num1, num2)
    elif operation == "**":
        result = calculator_functions.power(num1, num2)
    else:
        result = " عملیات نامعتبر!"

print(" نتیجه:", result)
