import random  # برای ساخت عدد تصادفی

secret_number = random.randint(1, 100)  # عدد مخفی بین ۱ تا ۱۰۰
attempts = 0  # شمارنده‌ی تعداد حدس‌ها

guess = int(input("حدس تو چیه بین 1تا 100؟ "))

while guess != secret_number:  # تا وقتی حدس درست نباشه
    attempts += 1  # شمارش حدس‌ها
    
    if guess < secret_number:
        print("برو بالاتر! ")
    elif guess > secret_number:
        print("بیا پایین‌تر! ")

    guess = int(input("دوباره حدس بزن: "))  # گرفتن حدس جدید

# وقتی از حلقه اومد بیرون یعنی حدس درست بوده
attempts += 1
print(f"آفرین! عدد درست {secret_number} بود ")
print(f"تو در {attempts} بار حدس زدی ")
