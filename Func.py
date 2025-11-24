# //روش اول  فاکتوریل
# def factorial(n):
#     resalt=1
#     for i in range(1,n+1):
#         resalt *= i
#     return resalt
# print (factorial(5))
# -----------------------------------------------------

# //روش دوم  فاکتوریل
# def factoral (n):
#     if n==1 or n==0:
#         return 1
#     else:
#         return n*factoral(n-1)

# print (factoral(5))
# -----------------------------------------------------

# روش سوم  فاکتوریل
# import math
# def factorial(n):
#     return math.factorial(n)
# print (factorial(5))
# -----------------------------------------------------

# روش ساده تر برای فاکتوریل
import math
print(math.factorial(5))
